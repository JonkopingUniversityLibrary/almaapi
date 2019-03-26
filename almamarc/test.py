import unittest
import os
import io
import almamarc


def strip_white_space(string):
    return string.replace(' ', '').replace('\t', '').replace('\n', '')


class AlmaMARCTest(unittest.TestCase):

    filename = os.path.dirname(__file__) + '/test_file.xml'
    xml_string = open(filename, encoding='utf8').read()
    record = almamarc.Record(filename, file=True)

    def test_that_input_is_same_as_output(self):
        filename = os.path.dirname(__file__) + '/test_file.xml'
        record = almamarc.Record(filename, file=True)
        self.assertEqual(strip_white_space(record.to_string()), strip_white_space(self.xml_string))

    def test_adding_field(self):
        self.record.add_field(tag='test', field_type='datafield', subfields={'a': 'test_a'})
        self.assertEqual(self.record.get_fields(tag='test')[0].get_subfield('a').value, 'test_a')


if __name__ == '__main__':
    unittest.main()
