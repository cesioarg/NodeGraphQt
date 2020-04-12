from NodeGraphQt import BaseNode, Port, QtCore
from . utils import update_node_down_stream
import traceback
import hashlib
import copy
import time


class CryptoColors(object):
    """
    Generate random color based on strings
    """

    def __init__(self):
        self.colors = {}

    def get(self, text, Min=50, Max=200):
        if text in self.colors:
            return self.colors[text]
        h = hashlib.sha256(text.encode('utf-8')).hexdigest()
        d = int('0xFFFFFFFFFFFFFFFF', 0)
        r = int(Min + (int("0x" + h[:16], 0) / d) * (Max - Min))
        g = int(Min + (int("0x" + h[16:32], 0) / d) * (Max - Min))
        b = int(Min + (int("0x" + h[32:48], 0) / d) * (Max - Min))
        # a = int(Min + (int("0x" + h[48:], 0) / d) * (Max - Min))
        self.colors[text] = (r, g, b, 255)
        return self.colors[text]


class AutoNode(BaseNode, QtCore.QObject):
    cooked = QtCore.Signal()

    def __init__(self, defaultInputType=None, defaultOutputType=None):
        super(AutoNode, self).__init__()
        QtCore.QObject.__init__(self)
        self._need_cook = True
        self._error = False
        self.matchTypes = [['float', 'int']]
        self.errorColor = (200, 50, 50)
        self.stopCookColor = (200, 200, 200)
        self._cryptoColors = CryptoColors()

        self.create_property('auto_cook', True)
        self.create_property('default_color', self.get_property('color'))
        self.defaultValue = None
        self.defaultInputType = defaultInputType
        self.defaultOutputType = defaultOutputType

        self._cook_time = 0.0
        self._toolTip = self._setup_tool_tip()

    @property
    def auto_cook(self):
        """
        Returns whether the node can update stream automatically.
        """

        return self.get_property('auto_cook')

    @auto_cook.setter
    def auto_cook(self, mode):
        """
        Set whether the node can update stream automatically.

        Args:
            mode(bool).
        """

        if mode is self.auto_cook:
            return

        self.model.set_property('auto_cook', mode)
        if mode:
            self.set_property('color', self.get_property('default_color'))
        else:
            if not self._error:
                self.model.set_property('default_color', self.get_property('color'))
            self.set_property('color', self.stopCookColor)

    @property
    def cook_time(self):
        """
        Returns the last cooked time of the node.
        """

        return self._cook_time

    @cook_time.setter
    def cook_time(self, cook_time):
        """
        Set the last cooked time of the node.

        Args:
            cook_time(float).
        """

        self._cook_time = cook_time
        self._update_tool_tip()

    @property
    def has_error(self):
        """
        Returns whether the node has errors.
        """

        return self._error

    def update_stream(self, forceCook=False):
        """
        Update all down stream nodes.

        Args:
            forceCook(bool): if True, it will ignore the auto_cook and so on.
        """

        if not forceCook:
            if not self.auto_cook or not self.get_input_data:
                return
            if self.graph is not None and not self.graph.auto_update:
                return
        update_node_down_stream(self)

    def get_data(self, port):
        """
        Get node data by port.
        Most time it will called by output nodes of the node.

        Args:
            port(Port).

        Returns:
            node data.
        """

        return self.get_property(port.name())

    def get_input_data(self, port):
        """
        Get input data by input port name/index/object.

        Args:
            port(str/int/Port): input port name/index/object.
        """
        if type(port) is not Port:
            to_port = self.get_input(port)
        else:
            to_port = port
        if to_port is None:
            return copy.deepcopy(self.defaultValue)

        from_ports = to_port.connected_ports()
        if not from_ports:
            return copy.deepcopy(self.defaultValue)

        for from_port in from_ports:
            data = from_port.node().get_data(from_port)
            return copy.deepcopy(data)

    def when_disabled(self):
        """
        Node evaluation logic when node has been disabled.
        """

        num = max(0, len(self.input_ports())-1)
        for index, out_port in enumerate(self.output_ports()):
            self.model.set_property(out_port.name(), self.get_input_data(min(index, num)))

    def cook(self):
        """
        The entry of the node evaluation.
        Most time we need to call this method instead of AutoNode.run'.
        """

        _tmp = self.auto_cook
        self.model.set_property('auto_cook', False)

        if self._error:
            self._close_error()

        _start_time = time.time()
        try:
            self.run()
        except:
            self.error(traceback.format_exc())

        self.model.set_property('auto_cook', _tmp)

        if self._error:
            return

        self.cook_time = time.time() - _start_time

        self.cooked.emit()

    def run(self):
        """
        Node evaluation logic.
        """

        pass

    def on_input_connected(self, to_port, from_port):
        if self.check_port_type(to_port, from_port):
            self.update_stream()
        else:
            self.get_input_data = False
            to_port.disconnect_from(from_port)

    def on_input_disconnected(self, to_port, from_port):
        if not self.get_input_data:
            self.get_input_data = True
            return
        self.update_stream()

    def check_port_type(self, to_port, from_port):
        """
        Check whether the port_type of the to_port and from_type is matched.

        Args:
            to_port(Port).
            from_port(Port).

        Returns:
            bool.
        """

        if to_port.data_type != from_port.data_type:
            if to_port.data_type == 'None' or from_port.data_type == 'None':
                return True
            for types in self.matchTypes:
                if to_port.data_type in types and from_port.data_type in types:
                    return True
            return False

        return True

    def set_property(self, name, value):
        super(AutoNode, self).set_property(name, value)
        self.set_port_type(name, type(value).__name__)
        if name in self.model.custom_properties.keys():
            self.update_stream()

    def set_port_type(self, port, data_type: str):
        """
        Set the data_type of the port.

        Args:
            port(Port): the port to set the data_type.
            data_type(str): port new data_type.
        """

        current_port = None

        if type(port) is Port:
            current_port = port
        elif type(port) is str:
            inputs = self.inputs()
            outputs = self.outputs()
            if port in inputs.keys():
                current_port = inputs[port]
            elif port in outputs.keys():
                current_port = outputs[port]

        if current_port:
            if current_port.data_type == data_type:
                return
            else:
                current_port.data_type = data_type

            current_port.border_color = current_port.color = self._cryptoColors.get(data_type)
            conn_type = 'multi' if current_port.multi_connection() else 'single'
            current_port.view.setToolTip('{}: {} ({}) '.format(current_port.name(), data_type, conn_type))

    def add_input(self, name='input', data_type='None', multi_input=False, display_name=True,
                  color=None):
        new_port = super(AutoNode, self).add_input(name, multi_input, display_name, color)
        if data_type == 'None' and self.defaultInputType is not None:
            data_type = self.defaultInputType
        if type(data_type) is not str:
            data_type = data_type.__name__
        self.set_port_type(new_port, data_type)

        return new_port

    def add_output(self, name='output', data_type='None', multi_output=True, display_name=True,
                   color=None):
        new_port = super(AutoNode, self).add_output(name, multi_output, display_name, color)
        if data_type == 'None' and self.defaultOutputType is not None:
            data_type = self.defaultOutputType
        if type(data_type) is not str:
            data_type = data_type.__name__
        self.set_port_type(new_port, data_type)

        return new_port

    def set_disabled(self, mode=False):
        super(AutoNode, self).set_disabled(mode)
        self.update_stream()

    def _close_error(self):
        """
        Close the node error.
        """

        self._error = False
        self.set_property('color', self.get_property('default_color'))
        self._update_tool_tip()

    def _update_tool_tip(self, message=None):
        """
        Update the node tooltip.

        Args:
            message(str): new node tooltip.
        """

        if message is None:
            tooltip = self._toolTip.format(self._cook_time)
        else:
            tooltip = '<b>{}</b>'.format(self.name())
            tooltip += message
            tooltip += '<br/>{}<br/>'.format(self._view.type_)
        self.view.setToolTip(tooltip)
        return tooltip

    def _setup_tool_tip(self):
        """
        Setup default node tooltip.

        Returns:
            str: new node tooltip.
        """
        tooltip = '<br> last cook used: {}s</br>'
        return self._update_tool_tip(tooltip)

    def error(self, message):
        """
        Change the node color and set error describe to the node tooltip.

        Args:
            message(str): the describe of the error.
        """

        if not self._error:
            self.model.set_property('default_color', self.get_property('color'))

        self._error = True
        self.set_property('color', self.errorColor)
        tooltip = '<font color="red"><br>({})</br></font>'.format(message)
        self._update_tool_tip(tooltip)

    # def __del__(self):
    #     """
    #     Check gc.
    #     """
    #     print("Delete: ", self.name())

