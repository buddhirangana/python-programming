import xml.etree.ElementTree as ET 

a = ET.Element('tag1')
b = ET.SubElement(a, 'tag2')
b.text = "Animal"
c = ET.SubElement(a, 'tag3')
c.text = "Domestic"
d = ET.SubElement(a, 'tag4')
d_1 = ET.SubElement(d, 'tag4.1')
d_1.text = "Cat"
d_2 = ET.SubElement(d, 'tag4.2')
d_2.text = "Persian"
e = ET.SubElement(a, 'tag5')
e.text = "Iran"
f = ET.SubElement(a, 'tag6')
f.text = "Male"
g = ET.SubElement(a, 'tag7')
g.text = "2021.05.04"
ET.dump(a)
