#!/usr/bin/python
# -*- coding: utf-8 -*-
from .node_base.auto_node import AutoNode


class VectorSplit(AutoNode):
    """
    Splict a vector to x,y,z
    """

    __identifier__ = 'Data'
    NODE_NAME = 'Vector Split'

    def __init__(self):
        super(VectorSplit, self).__init__()

        self.add_output('x')
        self.create_property("x", 0.0)
        self.add_output('y')
        self.create_property("y", 0.0)
        self.add_output('z')
        self.create_property("z", 0.0)
        self.add_output('w')
        self.create_property("w", 0.0)

        self.add_input("in vector", list)
        self.map = {0: "x", 1: "y", 2: "z", 3: "w"}

    def run(self):
        value = self.get_input_data(0)
        if type(value) is not list:
            self.error("Input data not list")
            return
        for index, data in enumerate(value):
            if index > 3:
                return
            self.set_property(self.map[index], data)


class VectorMaker(AutoNode):
    """
    Create a vector by three float value
    """

    __identifier__ = 'Data'
    NODE_NAME = 'Vector Maker'

    def __init__(self):
        super(VectorMaker, self).__init__()

        self.add_output('out', list)
        self.create_property("out", None)

        self.add_input("x", float)
        self.add_input("y", float)
        self.add_input("z", float)
        self.add_input("w", float)

    def run(self):
        result = []
        for i in range(4):
            data = self.get_input_data(i)
            if data is not None:
                result.append(data)

        self.set_property("out", result)


class DataConvert(AutoNode):
    """
    Convert input to selected object type.
    """

    __identifier__ = 'Data'

    NODE_NAME = 'Data Convert'

    convertion = {
        "eval string": eval,
        "all to int": int,
        "all to float": float,
        "all to string": str,
        "all to list": list,
        "all to set": set,
        "all to dict": dict,
    }

    def __init__(self):
        super(DataConvert, self).__init__()
        self.add_output('out')
        self.create_property("out", None)
        self.add_input("in data")
        self.add_combo_menu('method',
                            'Method',
                            items=list(self.convertion.keys()))

    def run(self):
        method = self.get_property("method")
        try:
            data = self.convertion[method](self.getInputData(0))
            self.set_property("out", data)
        except Exception as error:
            self.error(error)
