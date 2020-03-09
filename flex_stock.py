def flex_THB(text,word_to_reply,usthbspot,Percent,IQXUSTHB,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "lg",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "xl",
                "weight": "bold",
                "color": "{}".format(Change_color)                
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "start",
                "gravity": "bottom",
                "weight": "bold",
                "color": "{}".format(Change_color),
                "wrap": True
              }
            ]
          } ,
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Today",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} {}".format(usthbspot, Percent),
                    "flex": 3,
                    "size": "lg",
                    "color": "{}".format(Change_color),
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Start",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(IQXUSTHB),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Target",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(comment),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  return bubble

def flex_WTI(text,word_to_reply,wtispot,Percent,IQXWTI,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "lg",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "xl",
                "weight": "bold",
                "color": "{}".format(Change_color)
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "start",
                "gravity": "bottom",
                "weight": "bold",
                "color": "{}".format(Change_color),
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Today",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} {}".format(wtispot, Percent),
                    "flex": 3,
                    "size": "lg",
                    "color": "{}".format(Change_color),
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Start",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(IQXWTI),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Target",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(comment),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  return bubble

def flex_gold(text,word_to_reply,gspot,Percent,IQXGL,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "lg",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "xl",
                "weight": "bold",
                "color": "{}".format(Change_color)
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "start",
                "gravity": "bottom",
                "weight": "bold",
                "color": "{}".format(Change_color),
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Today",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} {}".format(gspot, Percent),
                    "flex": 3,
                    "size": "lg",
                    "color": "{}".format(Change_color),
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Start",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(IQXGL),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Target",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(comment),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  return bubble

def flex_tfex(text,word_to_reply,tfex_now,Percent,tfexx,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "lg",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "xl",
                "weight": "bold",
                "color": "{}".format(Change_color)
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "start",
                "gravity": "bottom",
                "weight": "bold",
                "color": "{}".format(Change_color),
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Today",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} {}".format(tfex_now, Percent),
                    "flex": 3,
                    "size": "lg",
                    "color": "{}".format(Change_color),
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Start",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(tfexx),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Target",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(comment),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  return bubble

def flex_set(text,word_to_reply,set_now,Percent,sett,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "lg",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "xl",
                "weight": "bold",
                "color": "{}".format(Change_color)
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "start",
                "gravity": "bottom",
                "weight": "bold",
                "color": "{}".format(Change_color),
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Today",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} {}".format(set_now, Percent),
                    "flex": 3,
                    "size": "lg",
                    "color": "{}".format(Change_color),
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Start",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(sett),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Target",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(comment),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  return bubble

def flex_stock(text,notice,price_now,change,open,buy,stop,target):
  Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "lg",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "xl",
                "weight": "bold",
                "color": "{}".format(Change_color)
              },
              {
                "type": "text",
                "text": "{}".format(notice),
                "size": "lg",
                "align": "start",
                "gravity": "bottom",
                "weight": "bold",
                "color": "{}".format(Change_color),
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Today",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} {}".format(price_now, change),
                    "flex": 3,
                    "size": "lg",
                    "color": "{}".format(Change_color),
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Buy",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{} ~ {}".format(open, buy),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Stop",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "Target",
                    "flex": 1,
                    "size": "sm",
                    "color": "#010101"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "color": "#666666",
                    "wrap": True
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  return bubble