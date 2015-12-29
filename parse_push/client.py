import json
import requests

from .config import APPLICATION_ID, REST_API_KEY, API_URL, API_VERSION


class Client:

    def __init__(self, application_id=None, rest_api_key=None, api_url=None, api_version=None):
        """
        You can pass application_id and rest_api_key at initiation
        or it will use the the values from config.py as default.

        :param application_id:
            The APPLICATION_KEY from Parse
        :param rest_api_key:
            The REST_API_KEY from Parse
        :param api_url:
            The API_URL for Parse
        :param api_version:
            The API_VERSION for Parse
        :return:
            None
        """
        if application_id is None and rest_api_key is None:
            self.application_id = APPLICATION_ID
            self.rest_api_key = REST_API_KEY

        if api_url is None and api_version is None:
            self.api_url = API_URL
            self.api_version = API_VERSION

    def get_base_url(self):
        return "{}/{}".format(self.api_url, self.api_version)

    def request(self, method, url_path, data):
        url = "{}/{}".format(self.get_base_url(), url_path)
        headers = {
            "X-Parse-Application-Id": self.application_id,
            "X-Parse-REST-API-Key": self.rest_api_key,
            "Content-Type": "application/json"
        }
        return requests.request(method=method, url=url, headers=headers, data=json.dumps(data))

    def push(self, kind, token, data):
        """
        EXAMPLE:
            {
                "where": {
                    "deviceType": "ios",
                    "deviceToken" "abcdefghijklmnopqrstuvwxyz1234567890",
                },
                "data": {
                    "title": "Django Push",
                    "text": "Hello World!",
                    "action": {
                        "kind": "PORTFOLIO",
                        "id": "12345"
                    },
                    "object": {
                        "foo": "bar"
                    }
                }
            }
            :param kind:
                One of  "ios", "android", "winrt", "winphone", "dotnet".
            :param token:
                The device token.
            :param data:
                Arbitrary dict object that will be serialized into JSON
        """
        dict_ = {
            'where': {
                'deviceType': kind,
                'deviceToken': token,
            },
            'data': data
        }
        return self.request(method="post", url_path="push", data=dict_)


def get_client():
    """
    Helper for getting a preconfigured client.
    :return: Client object
    """
    return Client(application_id=APPLICATION_ID, rest_api_key=REST_API_KEY, api_url=API_URL, api_version=API_VERSION)
