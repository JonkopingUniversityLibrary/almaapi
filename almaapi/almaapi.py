import httplib2 as http
import xml.etree.ElementTree as ElementTree


class AlmaAPIException(Exception):
    """Custom docstring"""


class AlmaAPI:

    def __init__(self, api, api_key):
        self.api_url = 'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/' + api + '/'
        self.api_key = '?apikey=' + api_key

    def get(self, *, mms_id=False, query_params=None):
        if mms_id is False:
            return False

        __query_params__ = ''
        if query_params is not None:
            for key, value in query_params.items():
                __query_params__ += '&' + key + '=' + value

        url = self.api_url + mms_id + self.api_key + __query_params__

        (response, content) = http.Http().request(url)

        if response.status != 200:
            root = ElementTree.ElementTree(ElementTree.fromstring(content)).getroot()
            error_message = root[1][0][1].text
            raise AlmaAPIException(str(response.status) + ': ' + error_message)

        return content.decode('utf8')

    def put(self, *, mms_id=False, body=False, query_params=None):
        if mms_id is False or body is False:
            return False

        __query_params__ = ''
        if query_params is not None:
            for key, value in query_params.items():
                __query_params__ += '&' + key + '=' + value

        url = self.api_url + mms_id + self.api_key + __query_params__
        headers = {'Content-type': 'application/xml'}

        (response, content) = http.Http().request(url, 'PUT', headers=headers, body=body)
        if response.status != 200:
            root = ElementTree.ElementTree(ElementTree.fromstring(content)).getroot()
            error_message = root[1][0][1].text
            raise AlmaAPIException(str(response.status) + ': ' + error_message)

        return content.decode('utf8')
