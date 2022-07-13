import xml.etree.ElementTree as ET

tree = ET.parse('vehicle.xml')
root = tree.getroot()

for element in root.iter(tag='registratiob_no'):
    print(element.text)
