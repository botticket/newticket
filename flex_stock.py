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

def flex_stock(text,price_now,notice,change,open,buy,stop,target,avg):
  Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble = {
    "type": "bubble",
    "size": "giga",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "filler"
            }
          ],
          "flex": 1,
          "backgroundColor": "#3c3c3c"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "filler"
            }
          ],
          "flex": 2
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "image",
              "url": "https://www.montsame.mn/files/5c8768fea4d6e.jpeg",
              "aspectMode": "cover"
            }
          ],
          "borderWidth": "3px",
          "borderColor": "#FFFFFF",
          "cornerRadius": "55px",
          "position": "absolute",
          "offsetTop": "5%",
          "offsetStart": "5px"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "{}".format(text),
                  "weight": "bold",
                  "align": "start",
                  "color": "{}".format(Change_color),
                  "wrap": True,
                  "size": "xxl",
                  "gravity": "center"
                },
                {
                  "type": "text",
                  "text": "{}".format(price_now),
                  "align": "end",
                  "color": "{}".format(Change_color),
                  "gravity": "center",
                  "size": "lg"
                }
              ],
              "paddingStart": "150px",
              "paddingTop": "5px",
              "width": "95%"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "{}".format(notice),
                  "weight": "regular",
                  "align": "start",
                  "color": "#F8F9F9",
                  "wrap": True,
                  "size": "lg",
                  "gravity": "center"
                },
                {
                  "type": "text",
                  "text": "{}".format(change),
                  "align": "end",
                  "color": "{}".format(Change_color),
                  "gravity": "center",
                  "size": "lg"
                }
              ],
              "paddingStart": "150px",
              "paddingTop": "5px",
              "width": "95%"
            }
          ],
          "width": "100%",
          "position": "absolute",
          "flex": 3
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Buy",
                  "weight": "bold",
                  "align": "start",
                  "color": "#959595",
                  "size": "md"
                },
                {
                  "type": "text",
                  "text": "{} | {}".format(open,buy),
                  "weight": "regular",
                  "align": "start",
                  "color": "#000000",
                  "size": "xl",
                  "wrap": True
                }
              ],
              "spacing": "xs"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Target",
                  "weight": "bold",
                  "align": "start",
                  "color": "#959595",
                  "size": "md"
                },
                {
                  "type": "text",
                  "text": "{}".format(target),
                  "weight": "regular",
                  "align": "start",
                  "color": "#000000",
                  "size": "xl",
                  "wrap": True
                }
              ],
              "spacing": "xs"
            }
          ],
          "flex": 3,
          "position": "absolute",
          "width": "50%",
          "paddingTop": "120px",
          "paddingStart": "35px"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Stop",
                  "weight": "bold",
                  "align": "start",
                  "color": "#959595",
                  "size": "md"
                },
                {
                  "type": "text",
                  "text": "{}".format(stop),
                  "weight": "regular",
                  "align": "start",
                  "color": "#000000",
                  "size": "xl",
                  "wrap": True
                }
              ],
              "spacing": "xs"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Avg.",
                  "weight": "bold",
                  "align": "start",
                  "color": "#959595",
                  "size": "md"
                },
                {
                  "type": "text",
                  "text": "{} %".format(avg),
                  "weight": "regular",
                  "align": "start",
                  "color": "#000000",
                  "size": "xl",
                  "wrap": True
                }
              ],
              "spacing": "xs"
            }
          ],
          "flex": 3,
          "position": "absolute",
          "width": "50%",
          "paddingTop": "120px",
          "paddingStart": "35px",
          "offsetEnd": "12px"
        }
      ],
      "height": "270px",
      "paddingAll": "0px"
    }
  }
  return bubble