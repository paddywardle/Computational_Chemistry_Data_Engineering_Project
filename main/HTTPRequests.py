from urllib import response
import requests

class HTTPRequests():

    def __init__(self):
        self.session = ''

    def create_session(self):

        self.session = requests.Session()

    def get(self, url, **kwargs):

        try:
            if self.session != '':
                response = self.session.get(url, kwargs)
                response.raise_for_status()
                return response
            response = response.get(url, kwargs)
            return response
            response.raise_for_status()
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

    def put(self, url, **kwargs):

        try:
            if self.session != '':
                response = self.session.put(url, kwargs)
                response.raise_for_status()
                return response
            response = response.put(url, kwargs)
            return response
            response.raise_for_status()
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

    def post(self, url, **kwargs):

        try:
            if self.session != '':
                response = self.session.post(url, kwargs)
                response.raise_for_status()
                return response
            response = response.post(url, kwargs)
            return response
            response.raise_for_status()
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

    def post(self, url, **kwargs):

        try:
            if self.session != '':
                response = self.session.post(url, kwargs)
                response.raise_for_status()
                return response
            response = response.post(url, kwargs)
            return response
            response.raise_for_status()
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

