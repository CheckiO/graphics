#!env python
__author__ = 'bryukh'
import unittest
import all_settings

from base_tests import SvgTest, suite

PATHS = ['icons_interface/',]

class IconInterfaceTest(SvgTest):
    pass

if __name__ == '__main__':
    settings = {
        'size': all_settings.ICONS_INTERFACE_SIZE,
        'colors': all_settings.COLORS
    }
    unittest.TextTestRunner(verbosity=2).run(suite(IconInterfaceTest, PATHS, settings))