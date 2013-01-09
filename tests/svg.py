__author__ = 'bryukh'
from xml.etree import ElementTree
import re


class SvgReader(object):
    def __init__(self, source):
        with open(source) as file:
            parsed_svg = ElementTree.parse(file)
        self.root = parsed_svg.getroot()
        self.elements = self.root.iter()
        temp_re = re.match("^{.*?}", self.root.tag)
        self.xlmns = temp_re.group() if temp_re else {}

    def get_size(self):
        return int(self.root.attrib['width']), int(self.root.attrib['height'])

    def get_backgrounds(self):
        return (el for el in self.elements if el.attrib.get('id', '') == 'Background')

    def get_elements_colors(self):
        res = []
        colors_attrib = [('fill', 'fill-opacity'), ('stroke', 'stroke-opacity')]
        for el in self.elements:
            for attr in colors_attrib:
                if el.attrib.get(attr[1], '100') != '0' and el.attrib.get(attr[0]):
                    res.append({'color': el.attrib[attr[0]],
                                'type': attr[0],
                                'tag': el.tag.replace(self.xlmns, ''),
                                'id': el.attrib.get('id', '')})
        return res