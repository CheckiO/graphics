#!env python
__author__ = 'bryukh'
import unittest
import os
import icons_settings as settings
from svg import SvgReader

PATH = '../icons_tasks/'
ALT_PATH = './icons_tasks'

def suite():
    path = PATH if os.path.exists(PATH) else ALT_PATH
    svgfiles = []
    for dirpath, dirnames, files in os.walk(path):
        svgfiles = [os.path.join(dirpath, file) for file in files if file[-3:] == 'svg']
    test_suite = unittest.TestSuite()
    tests_names = unittest.TestLoader().getTestCaseNames(IconTest)
    for filename in svgfiles:
        svg = SvgReader(filename)
        test_suite.addTests([IconTest(svg, filename, methodName=test_name) for test_name in tests_names])
    return test_suite


class IconTest(unittest.TestCase):
    def __init__(self, svg, filename, *args, **kwargs):
        self.svg = svg
        self.filename = filename
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_size(self):
        size = self.svg.get_size()
        self.assertEqual(size, settings.SIZE, "Wrong size {0}x{1} for file {2}".format(size[0], size[1], self.filename))

    def test_opacity_background(self):
        for elem in self.svg.get_backgrounds():
            for child_elem in elem.getchildren():
                opacity = child_elem.get('fill-opacity')
                self.assertEqual(opacity, '0', "Wrong opacity {0} for file {1}".format(opacity, self.filename))

    def test_colors(self):
        elements_colors = self.svg.get_elements_colors()
        for el in elements_colors:
            self.assertIn(el['color'], settings.COLORS,
                'Wrong color {0} {1} in tag {2} id {3} for file {4}'.format(el['color'],
                    el['type'], el['tag'], el['id'], self.filename))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())