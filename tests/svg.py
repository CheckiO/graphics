__author__ = 'bryukh'
from xml.etree import ElementTree


class SVG(object):
    def __init__(self, source):
        with open(source) as file:
            parsed_svg = ElementTree.parse(file)
        self.root = parsed_svg.getroot()
        self.elements = self.root.iter()

    def get_size(self):
        return int(self.root.attrib['width']), int(self.root.attrib['height'])

    def get_backgrounds(self):
        return (el for el in self.elements if el.attrib.get('id', '') == 'Background')