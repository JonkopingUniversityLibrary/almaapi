import xmljson
from xml.etree.ElementTree import fromstring


class AlmaAnalyticsException(Exception):
    """Custom docstring"""


class AlmaAnalyticsParser:

    def __init__(self, i):
        def __parse_analytics__(xml_string):
            result = xmljson.parker.data(fromstring(xml_string))
            urn_schema = '{urn:schemas-microsoft-com:xml-analysis:rowset}'
            rows = result['QueryResult']['ResultXml'][urn_schema + 'rowset'][urn_schema + 'Row']

            def get_column_count():
                count = 0
                for row in rows:
                    if len(row) > count:
                        count = len(row)
                return count - 1

            column_count = get_column_count()
            temp_table = []

            for row in rows:
                if column_count is 1:
                    temp_row = None
                    for column in row.items():
                        try:
                            column_number = int(column[0].replace(urn_schema + 'Column', ''))
                            value = column[1]

                            if column_number is 1:
                                temp_row = value

                        except ValueError:
                            exit()
                else:
                    temp_row = [None] * column_count
                    for column in row.items():
                        try:
                            column_number = int(column[0].replace(urn_schema + 'Column', ''))
                            value = column[1]

                            if column_number > 0:
                                temp_row[column_number - 1] = value

                        except ValueError:
                            raise(AlmaAnalyticsException('Failed to load column number'))

                temp_table.append(temp_row)
                print(temp_table)

        self.list = __parse_analytics__(i)

    def get_table(self):
        return self.list

    def get_values_from_column(self, column_number):
        temp_list = []
        column_number = column_number - 1
        try:
            for row in self.list:
                temp_list.append(row[column_number])
        except IndexError:
            return None
