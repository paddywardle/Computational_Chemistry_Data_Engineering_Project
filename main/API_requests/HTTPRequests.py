import requests

class HTTPRequests():

    def __init__(self):
        self.session = requests.Session()

    def get(self, url: str, **kwargs):

        try:
            response = self.session.get(url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def put(self, url: str, **kwargs):

        try:
            response = self.session.put(url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
        except:
            print("Other error")

    def post(self, url: str, **kwargs):

        try:
            response = self.session.post(url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
        except:
            print("Other error")