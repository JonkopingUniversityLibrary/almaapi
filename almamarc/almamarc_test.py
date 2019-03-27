import unittest
import os
import io
import almamarc

almamarc_file = os.path.dirname(__file__) + '/almamarc.xml'
normalmarc_file = os.path.dirname(__file__) + '/normalmarc.xml'
almamarc_xml = open(almamarc_file, encoding='utf8').read()
normalmarc_xml = open(normalmarc_file, encoding='utf8').read()


def strip_white_space(string):
    return string.replace(' ', '').replace('\t', '').replace('\n', '')


class RecordSetup(unittest.TestCase):

    record = almamarc.Record(almamarc_file, file=True)

    def test_load_not_alma_marc(self):

        with self.assertRaises(almamarc.AlmaMARCException):
            almamarc.Record(normalmarc_file, file=True)

    def test_that_input_is_same_as_output(self):
        record = almamarc.Record(almamarc_file, file=True)
        self.assertEqual(strip_white_space(record.to_string()), strip_white_space(almamarc_xml))

    def test_that_attributes_is_dict(self):
        self.assertTrue(isinstance(self.record.attributes, dict))

    def test_for_attributes_length(self):
        self.assertEqual(len(self.record.attributes), 16)


class Fields(unittest.TestCase):

    record = almamarc.Record(almamarc_file, file=True)

    def test_adding__and_removing_fields(self):
        tag = 'test'

        # First add a field and test if it was added
        self.record.add_field(tag=tag, subfields={'a': 'test_a'})
        self.assertEqual(self.record.get_fields(tag=tag)[0].get_subfield('a').value, 'test_a')

        # Then remove the field and see if it was removed
        self.record.remove_fields(tag=tag)
        self.assertEqual(len(self.record.get_fields(tag=tag)), 0)

        # Add multiple fields and then remove them and see if they are gone.

        self.record.add_field(tag=tag, subfields={'a': 'test_c'})
        self.record.add_field(tag=tag, subfields={'a': 'test_c'})
        self.record.remove_fields(tag=tag)
        self.assertEqual(len(self.record.get_fields(tag=tag)), 0)


class Subfields(unittest.TestCase):

    record = almamarc.Record(almamarc_file, file=True)


if __name__ == '__main__':
    unittest.main()
