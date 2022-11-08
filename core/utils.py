from pathlib import Path
import os
from string import ascii_letters, digits
from random import choices, seed
from time import time
from urllib import response
import requests
# import environ

# Loading an Environment Variable File with dotenv
# from dotenv import load_dotenv
# load_dotenv()



seed = time()

BASE_DIR = Path(__file__).resolve().parent.parent

# with open(BASE_DIR / "env.json") as env_file:
#     env = json.loads(env_file.read())






def get_random_string(count: int) -> str:
    return ''.join(choices(ascii_letters + digits, k=count))


def send_sms(to: str, message: str) -> response:
    """
    This helper function sends sms messages to a specified phone number

    Args:"""  """
        to (str): The phone number to send message to
        message (str): the message body

    Returns:
        response: a sms message object 
        {
        0": 200,
        "data": {
                "status": "success",
                "message": "Message Sent",
                "message_id": "d0173d84-2f01-4a5f-a0dc-375beea5b806",
                "cost": 4.99,
                "currency": "NGN",
                "gateway_used": "direct_corporate"
            }
        }
    """
    # SMS_API_TOKEN = env("SMS_API_TOKEN")
    SMS_API_TOKEN = os.environ.get("SMS_API_TOKEN")

    print(SMS_API_TOKEN)
    

    sms_url = 'https://www.bulksmsnigeria.com/api/v2/sms/create'
    params = {
        'api_token': SMS_API_TOKEN,
        'to': to,
        'from': 'Bloodfuse',
        'body': message,
        'gateway': '0',
        'append_sender': '0',
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(sms_url, headers=headers, params=params)
    return response.json()



if __name__ == '__main__':
    message = "what \nabout now \n \nhmm\n still test"
    test_sms = send_sms('+2347050595335', message)
    print(test_sms)

