import xml.etree.ElementTree as ElementTree


class AnalyticsParser:

    def __init__(self, i):
        # Parse string or file into XML Object
        def __parse__(xml_string):
            return ElementTree.ElementTree(ElementTree.fromstring(xml_string))
        self.xml = __parse__(i)
        self.root = self.xml.getroot()

    def get_values(self, column_name):
        temp_values = []
        all_fields = list(self.root.findall('.//'))
        for field in all_fields:
            if column_name in field.tag:
                temp_values.append(field.text)
        return temp_values
