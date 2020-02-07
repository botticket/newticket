richdata = {
  "size": {
    "width": 2500,
    "height": 843
  },
  "selected": True,
  "name": "Menu",
  "chatBarText": "Menu",
  "areas": [
    {
      "bounds": {
        "x": 8,
        "y": 13,
        "width": 818,
        "height": 398
      },
      "action": {
        "type": "message",
        "text": "IQXUSTB"
      }
    },
    {
      "bounds": {
        "x": 843,
        "y": 17,
        "width": 810,
        "height": 386
      },
      "action": {
        "type": "message",
        "text": "IQXGL"
      }
    },
    {
      "bounds": {
        "x": 1669,
        "y": 25,
        "width": 823,
        "height": 386
      },
      "action": {
        "type": "message",
        "text": "IQXWTI"
      }
    },
    {
      "bounds": {
        "x": 386,
        "y": 453,
        "width": 389,
        "height": 378
      },
      "action": {
        "type": "message",
        "text": "SET"
      }
    },
    {
      "bounds": {
        "x": 1686,
        "y": 453,
        "width": 386,
        "height": 382
      },
      "action": {
        "type": "message",
        "text": "TFEX"
      }
    },
    {
      "bounds": {
        "x": 2174,
        "y": 496,
        "width": 241,
        "height": 212
      },
      "action": {
        "type": "message",
        "text": "UPDATE"
      }
    }
  ]
}

from config import line_secret, line_access_token

import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(line_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = line_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(line_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())



CreateRichMenu(ImageFilePath='Resource/richmenu.jpg',Rich_json=richdata,channel_access_token=line_access_token)