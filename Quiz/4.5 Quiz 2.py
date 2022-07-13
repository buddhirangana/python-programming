import xml.etree.ElementTree as ET
vehicle_xml_data_as_string = "<motorvehicles><vehicle><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle><vehicle><registration_no>DE2115</registration_no><make>TATA</make><model>Sumo</model></vehicle><vehicle><registration_no>CAR7785</registration_no><make>Kia</make><model>Optima</model></vehicle></motorvehicles>"

root = ET.fromstring(vehicle_xml_data_as_string)
root[2][1].text = "Nissan"
root[2][2].text = "Skyline"
print(root[2][0].text)
