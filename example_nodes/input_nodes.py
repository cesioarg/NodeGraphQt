from NodeGraphQt import BaseNode, QtCore


class DataInputNode(BaseNode):
    """
    Input node data.
    """

    __identifier__ = 'Inputs'
    NODE_NAME = 'Basic Input'

    def __init__(self):
        super(DataInputNode, self).__init__()
        self.add_output('out')
        self.add_text_input('out', 'Data Output', text='0.4', tab='widgets')
        self.view.widgets['out'].value_changed.connect(self.update_streams)
    
    def run(self):
        self.metacode()

    def metacode(self):
        for outPort in self.output_ports():
            for to_port in outPort.connected_ports():
                nodeName = to_port.node().name().replace(' ', '_')
                code = "%s_%s = %s" % (nodeName, to_port.name(),
                                       self.get_property('out'))
                print (code)
                return code

class TickTimeNode(BaseNode):
    """
    Every second that passes adds a tick.
    """

    __identifier__ = 'Inputs'
    NODE_NAME = 'Tick Time'

    def __init__(self):
        super(TickTimeNode, self).__init__()
        self.add_output('out')
        self.add_text_input('out', 'Ticks', text='0', tab='widgets')
        self.view.widgets['out'].value_changed.connect(self.update_streams)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

    def tick(self):
        if not self.disabled():
            current = int(self.get_property('out'))
            current += 1
            self.view.widgets['out'].value_changed.emit('out', str(current))


class TextFileInputNode(BaseNode):
    """
    Text File Input node data.
    """

    __identifier__ = 'Inputs'
    NODE_NAME = 'Text File'

    def __init__(self):
        super(TextFileInputNode, self).__init__()
        self.add_output('out')
        self.create_property('out', None)
        self.add_text_input('path', 'Text File Path', text='', tab='widgets')
        self.view.widgets['path'].value_changed.connect(self.update_streams)

    def run(self):
        if not self.disabled():
            path = self.get_property('path')
            if os.path.exists(path):
                with open(path, 'r') as fread:
                    data = fread.read()
                    self.set_property('output', data)
            else:
                print('No existe %s' % path)
                self.set_property('output', '')
