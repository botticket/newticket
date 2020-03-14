richdata ={
  "size": {
    "width": 2500,
    "height": 843
  },
  "selected": True,
  "name": "menu",
  "chatBarText": "menu",
  "areas": [
    {
      "bounds": {
        "x": 8,
        "y": 13,
        "width": 810,
        "height": 406
      },
      "action": {
        "type": "message",
        "text": "IQUSTB"
      }
    },
    {
      "bounds": {
        "x": 847,
        "y": 17,
        "width": 806,
        "height": 398
      },
      "action": {
        "type": "message",
        "text": "IQXGL"
      }
    },
    {
      "bounds": {
        "x": 1678,
        "y": 17,
        "width": 814,
        "height": 402
      },
      "action": {
        "type": "message",
        "text": "IQXWTI"
      }
    },
    {
      "bounds": {
        "x": 403,
        "y": 449,
        "width": 381,
        "height": 390
      },
      "action": {
        "type": "message",
        "text": "SET"
      }
    },
    {
      "bounds": {
        "x": 1703,
        "y": 449,
        "width": 378,
        "height": 390
      },
      "action": {
        "type": "message",
        "text": "TFEX"
      }
    },
    {
      "bounds": {
        "x": 1042,
        "y": 445,
        "width": 390,
        "height": 390
      },
      "action": {
        "type": "message",
        "text": "Hello Bot"
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