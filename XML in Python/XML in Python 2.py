import xml.etree.ElementTree as ET

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(a, 'd')

ET.dump(a)
