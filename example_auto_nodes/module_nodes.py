from .node_base.module_node import (ModuleNode,
                                    get_functions_from_module,
                                    get_functions_from_type)

import os
import sys
import random
import numpy
import numpydoc.docscrape
import inspect
import importlib

from .wrappers import math as _math
from .wrappers import list as _list
from .wrappers import dict as _dict
from .wrappers import str as _str
from .wrappers import tuple as _tuple


class MathModuleNode(ModuleNode):
    """
    Math functions node.
    """

    # set a unique node identifier.
    __identifier__ = 'Module'

    # set the initial default node name.
    NODE_NAME = 'math module'

    module_functions = get_functions_from_module(_math)

    def __init__(self):
        super(MathModuleNode, self).__init__(float, float, module_functions=self.module_functions)
        self.defaultValue = 0.0


class osModuleNode(ModuleNode):
    """
    os module node.
    """

    # set a unique node identifier.
    __identifier__ = 'Module'

    # set the initial default node name.
    NODE_NAME = 'os module'

    module_functions = get_functions_from_module(os, max_depth=2)
    module_functions.pop("os.abort")

    def __init__(self):
        super(osModuleNode, self).__init__(module_functions=self.module_functions)


class sysModuleNode(ModuleNode):
    """
    sys module node.
    """

    # set a unique node identifier.
    __identifier__ = 'Module'

    # set the initial default node name.
    NODE_NAME = 'sys module'

    module_functions = get_functions_from_module(sys, max_depth=2)
    module_functions.pop("sys.exit")
    module_functions.pop("sys.breakpointhook")

    def __init__(self):
        super(sysModuleNode, self).__init__(module_functions=self.module_functions)


class randomModuleNode(ModuleNode):
    """
    random module node.
    """

    # set a unique node identifier.
    __identifier__ = 'Module'

    # set the initial default node name.
    NODE_NAME = 'random module'

    module_functions = get_functions_from_module(random, max_depth=2)

    def __init__(self):
        super(randomModuleNode, self).__init__(module_functions=self.module_functions)


class numpyModuleNode(ModuleNode):
    """
    numpy module node.
    """

    # set a unique node identifier.
    __identifier__ = 'Module'

    # set the initial default node name.
    NODE_NAME = 'numpy module'

    module_functions = get_functions_from_module(numpy, max_depth=2)

    def __init__(self):
        super(numpyModuleNode, self).__init__(module_functions=self.module_functions)
        self.set_icon("example_auto_nodes/icons/numpy.png")

    def get_numpy_args(self, func):
        args = []
        info = numpydoc.docscrape.FunctionDoc(func)
        for i in info["Parameters"]:
            param = str(i)
            if "name" in param:
                args.append(param.split("'")[1])
        return args

    def addFunction(self, prop, func):
        """
        Create inputs based on functions arguments.
        """

        self.func = self.module_functions[func]

        args = []
        if callable(self.func):
            try:
                args = inspect.getfullargspec(self.func).args
            except:
                try:
                    args = self.get_numpy_args(self.func)
                except:
                    if type(self.func).__name__ == "ufunc":
                        args = ["input" + str(i + 1) for i in range(self.func.nin)]

        self.process_args(args)


class StringFunctionsNode(ModuleNode):
    """
    String functions node.
    """

    # set a unique node identifier.
    __identifier__ = 'Data'

    # set the initial default node name.
    NODE_NAME = 'String Functions'

    module_functions = get_functions_from_type(_str)


    def __init__(self):
        super(StringFunctionsNode, self).__init__(module_functions=self.module_functions)


class ListFunctionsNode(ModuleNode):
    """
    List functions node.
    """

    # set a unique node identifier.
    __identifier__ = 'Data'

    # set the initial default node name.
    NODE_NAME = 'List Functions'

    module_functions = get_functions_from_type(_list)

    def __init__(self):
        super(ListFunctionsNode, self).__init__(module_functions=self.module_functions)


class DictFunctionsNode(ModuleNode):
    """
    DIct functions node.
    """

    # set a unique node identifier.
    __identifier__ = 'Data'

    # set the initial default node name.
    NODE_NAME = 'Dict Functions'

    module_functions = get_functions_from_type(_dict)

    def __init__(self):
        super(DictFunctionsNode, self).__init__(module_functions=self.module_functions)


class TupleFunctionsNode(ModuleNode):
    """
    Tuple functions node.
    """

    # set a unique node identifier.
    __identifier__ = 'Data'

    # set the initial default node name.
    NODE_NAME = 'Tuple Functions'

    module_functions = get_functions_from_type(_tuple)

    def __init__(self):
        super(TupleFunctionsNode, self).__init__(module_functions=self.module_functions)


class ImportNode(ModuleNode):
    """
    import function node.
    """

    # set a unique node identifier.
    __identifier__ = 'Module'

    # set the initial default node name.
    NODE_NAME = 'Import'

    def __init__(self):
        super(ImportNode, self).__init__()
        self.add_text_input('module', 'Import Module')
        self.view.widgets['module'].value_changed.connect(self.morph)
        
    def morph(self):
        try:
            name = self.get_property('module')
            self.view.widgets['module'].value_changed.disconnect()
            self.view.widgets['module'].hide()
            mod = importlib.import_module(name)
            self.set_name("Import (%s)" % name)
        except:
            raise Exception("No module Found!")

        module_functions = get_functions_from_type(mod)
        self.buildNode(module_functions)


if __name__ == "__main__":
    s = "[2,2]"
    print(numpy.zeros(eval(s)))
    pass
