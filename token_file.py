import requests

class Token:

    REFRESH_TOKEN = "< Generate your refresh token >"
    BASE_64_ID_SEC = "< Generate this Base 64 format string with your Client ID and Secret ID >"
    """ For generating the above mentioned variables follow this video < https://youtu.be/-FsFT6OwE1A > """
    URL = "https://accounts.spotify.com/api/token"
    
    def __init__(self):
        pass

    # this method genetrates the access token
    def get_token(self):
        response = requests.post(self.URL, data={"grant_type": "refresh_token","refresh_token": self.REFRESH_TOKEN}, headers={"Authorization": "Basic " + self.BASE_64_ID_SEC})
        response_json = response.json()
        return response_json["access_token"]
