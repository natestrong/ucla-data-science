import json
import os
import webbrowser
from dataclasses import dataclass, asdict

from twython import Twython, TwythonStreamer

TWITTER_JSON = f'{os.path.expanduser("~")}/Documents/twitter.json'


@dataclass
class TwitterCredentials:
    API_Key: str
    API_Secret_Key: str
    Bearer_Token: str
    Access_Token: str = None
    Access_Token_Secret: str = None


class RegisterTwitter:
    def __init__(self):
        with open(TWITTER_JSON) as f:
            self.twitter_Credentials = TwitterCredentials(**json.load(f))

        if not self.twitter_Credentials.Access_Token or not self.twitter_Credentials.Access_Token_Secret:
            temp_client = Twython(self.twitter_Credentials.API_Key, self.twitter_Credentials.API_Secret_Key)
            temp_creds = temp_client.get_authentication_tokens()
            url = temp_creds['auth_url']
            webbrowser.open(url)
            self.PIN_CODE = input("Please enter the PIN code:")

            auth_client = Twython(
                self.twitter_Credentials.API_Key,
                self.twitter_Credentials.API_Secret_Key,
                temp_creds.get('oauth_token'),
                temp_creds.get('oauth_token_secret')
            )
            final_step = auth_client.get_authorized_tokens(self.PIN_CODE)
            self.twitter_Credentials.Access_Token = final_step['oauth_token']
            self.twitter_Credentials.Access_Token_Secret = final_step['oauth_token_secret']

            with open(TWITTER_JSON, 'w') as f:
                json.dump(asdict(self.twitter_Credentials), f)

    def credentials(self) -> tuple:
        return (
            self.twitter_Credentials.API_Key,
            self.twitter_Credentials.API_Secret_Key,
            self.twitter_Credentials.Access_Token,
            self.twitter_Credentials.Access_Token_Secret
        )
