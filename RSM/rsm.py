import xml.etree.ElementTree as ET

class RSM:
    def __init__(self, file):
        self.file = file
        et = ET.parse(file)
        print(et.getroot().tag)
