import httplib2 as http


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

        return content.decode('utf8')

    def put(self, mms_id, body):
        url = self.api_url + mms_id + self.api_key + self.query_params
        headers = {'Content-type': 'application/xml'}

        (response, content) = http.Http().request(url, 'PUT', headers=headers, body=body)

        return content.decode('utf8')