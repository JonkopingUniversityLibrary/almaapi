import xml.etree.ElementTree as ElementTree
from io import BytesIO as bytes


class AlmaMARCException(Exception):
    """Custom docstring"""


class Record:

    def __init__(self, input, file=False):

        # Parse string or file into XML Object
        def __parse__(i, f):
            if f:
                return ElementTree.parse(i)
            else:
                return ElementTree.ElementTree(ElementTree.fromstring(i))
        self.xml = __parse__(input, file)

        # Set root and type
        root = self.xml.getroot()
        self.type = root.tag

        # Except if type is not Bib MARC or Holding Marc
        if self.type != 'bib' and self.type != 'holding':
            raise AlmaMARCException('Not a MARC XML Object')

        # Map record fields to a list
        self.fields = list(self.xml.findall('.//record/*'))



        # Get the attributes of the XMl Object
        def __get_attributes__(xml):
            record = xml.find('.//record')
            attributes = list(xml.findall('./'))
            attributes.remove(record)

            output = {}
            for attribute in attributes:
                output[attribute.tag] = attribute.text

            return output
        self.attributes = __get_attributes__(self.xml)

    def get_fields(self, field_type='datafield', tag=None):

        array = []

        for field in self.fields:

            # If no tag is specified, grab all fields with the same type
            if not tag:
                if field.tag == field_type:
                    marc_field = Field(field)
                    array.append(marc_field)
            else:
                if field.attrib.get('tag') == tag and field.tag == field_type:
                    marc_field = Field(field)
                    array.append(marc_field)

        return array

    def add_field(self, tag, field_type='datafield', ind1='', ind2='', subfields=None):
        record_root = self.xml.find('.//record')
        new_field = ElementTree.Element(field_type, tag=tag, ind1=ind1, ind2=ind2)

        if subfields is None:
            subfields = []
        for subfield in subfields:
            new_subfield = ElementTree.Element('subfield', code=subfield['code'])
            new_subfield.text = subfield['value']
            new_field.append(new_subfield)

        record_root.append(new_field)
        fields = self.get_fields(tag=tag, field_type=field_type)
        return fields

    def to_string(self):
        fake_file = bytes()
        self.xml.write(fake_file, encoding='utf-8', xml_declaration=False)
        return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + fake_file.getvalue().decode('utf-8')


class Field:

    def __init__(self, reference):
        self.__reference__ = reference
        self.field_type = reference.tag
        self.attributes = reference.attrib
        self.value = reference.text if not list(reference) else None
        self.subfields = []
        for subfield in list(reference):
            self.subfields.append(Subfield(subfield))

    def get_subfield(self, code):
        for subfield in self.subfields:
            if subfield.code == code:
                return subfield
        return None

    def add_subfield(self, code, value):
        field = self.__reference__
        new_subfield = ElementTree.Element('subfield', code=code)
        new_subfield.text = value
        return field.get_subfield(code=code)

    def get_subfields(self):
        return self.subfields

    def set_subfield_value(self, code, value):
        for subfield in self.subfields:
            if subfield.code == code:
                subfield.set_value(value)
                return subfield
        return None


class Subfield:
    def __init__(self, reference):
        self.__reference__ = reference
        self.code = reference.attrib['code']
        self.value = reference.text

    def set_code(self, code):
        self.code = code
        self.__reference__.attrib['code'] = code

    def set_value(self, value):
        self.value = value
        self.__reference__.text = value
