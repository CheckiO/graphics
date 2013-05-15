#!env python
__author__ = 'bryukh'
import unittest
import os
import all_settings as settings
from svg import SvgReader
from cairosvg import parser

PATHS = ['icons_tasks/',]

def suite(classTest, search_paths, settings):
    paths = [path for path in search_paths if os.path.exists(path)]
    svgfiles = []
    for path in paths:
        for dirpath, dirnames, files in os.walk(path):
            svgfiles.extend([os.path.join(dirpath, file) for file in files if file[-3:] == 'svg'])
    test_suite = unittest.TestSuite()
    tests_names = unittest.TestLoader().getTestCaseNames(classTest)
    for filename in svgfiles:
        svg = SvgReader(filename)
        test_suite.addTests([classTest(svg, filename, settings, methodName=test_name) for test_name in tests_names])
    return test_suite


class SvgTest(unittest.TestCase):
    def __init__(self, svg, filename, settings, *args, **kwargs):
        self.svg = svg
        self.filename = filename
        self.settings = settings
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_size(self):
        size = self.svg.get_size()
        self.assertEqual(size, self.settings['size'], "Wrong size {0}x{1} for file {2}".format(size[0], size[1], self.filename))

    def test_opacity_background(self):
        for elem in self.svg.get_backgrounds():
            for child_elem in elem.getchildren():
                opacity = child_elem.get('fill-opacity')
                self.assertEqual(opacity, '0', "Wrong opacity {0} for file {1}".format(opacity, self.filename))

    def test_colors(self):
        elements_colors = self.svg.get_elements_colors()
        for el in elements_colors:
            self.assertIn(el['color'], self.settings['colors'],
                'Wrong color {0} {1} in tag {2} id {3} for file {4}'.format(el['color'],
                    el['type'], el['tag'], el['id'], self.filename))