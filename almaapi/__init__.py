import httplib2 as http
import xml.etree.ElementTree as ElementTree


class AlmaAPIException(Exception):
    """Custom docstring"""


class AlmaAPI:

    def __init__(self, api, api_key, query_params=None):
        self.api_url = 'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/' + api + '/'
        self.api_key = '?apikey=' + api_key
        self.query_params = ''

        if query_params is not None:
            for key, value in query_params.items():
                self.query_params += '&' + key + '=' + value

    def get(self, mms_id):
        url = self.api_url + mms_id + self.api_key + self.query_params

        (response, content) = http.Http().request(url)

        if response.status != '200':
            # print(response)
            root = ElementTree.ElementTree(ElementTree.fromstring(content)).getroot()
            error_message = root[1][0][1].text
            raise AlmaAPIException(str(response.status) + ': ' + error_message)

        return content.decode('utf8')

    def put(self, mms_id, body):
        url = self.api_url + mms_id + self.api_key + self.query_params
        headers = {'Content-type': 'application/xml'}

        (response, content) = http.Http().request(url, 'PUT', headers=headers, body=body)
        if response.status != '200':
            root = ElementTree.ElementTree(ElementTree.fromstring(content)).getroot()
            error_message = root[1][0][1].text
            raise AlmaAPIException(str(response.status) + ': ' + error_message)

        return content.decode('utf8')
