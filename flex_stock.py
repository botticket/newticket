def flex_stock(text,price_now,notice,change,open,buy,stop,avg,target):
  Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
  trend = ['#EE0000' if '-' in str(avg) else '#23D500'][0]
  bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
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
                "url": "https://media.brstatic.com/2017/03/20172321/stock-market-ticker-charts_573x300.jpg",
                "aspectMode": "cover",
                "size": "sm"
              }
            ],
            "borderWidth": "2px",
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
                    "size": "xl",
                    "gravity": "center"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(price_now),
                    "align": "end",
                    "color": "{}".format(Change_color),
                    "gravity": "center",
                    "size": "md",
                    "offsetEnd": "10%"
                  }
                ],
                "paddingStart": "100px",
                "paddingTop": "1%"
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
                    "size": "md",
                    "gravity": "center"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(change),
                    "align": "end",
                    "color": "{}".format(Change_color),
                    "gravity": "center",
                    "size": "md",
                    "offsetEnd": "10%"
                  }
                ],
                "paddingStart": "100px",
                "paddingTop": "5px",
                "width": "100%"
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
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "{} | {}".format(open,buy),
                    "weight": "regular",
                    "align": "start",
                    "color": "#000000",
                    "size": "lg",
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
                    "text": "Stop",
                    "weight": "bold",
                    "align": "start",
                    "color": "#959595",
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(stop),
                    "weight": "regular",
                    "align": "start",
                    "color": "#000000",
                    "size": "lg",
                    "wrap": True,
                    "offsetBottom": "5%"
                  }
                ],
                "spacing": "md"
              }
            ],
            "flex": 3,
            "position": "absolute",
            "width": "50%",
            "paddingTop": "65%",
            "paddingStart": "8%"
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
                    "text": "Avg",
                    "weight": "bold",
                    "align": "start",
                    "color": "{}".format(trend),
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(avg),
                    "weight": "regular",
                    "align": "start",
                    "color": "{}".format(trend),
                    "size": "lg",
                    "wrap": True
                  }
                ],
                "spacing": "xs"
              }
            ],
            "flex": 3,
            "position": "absolute",
            "width": "50%",
            "paddingTop": "65%",
            "paddingStart": "15%",
            "offsetEnd": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Target",
                "size": "sm",
                "color": "#959595",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "{}".format(target),
                "size": "lg",
                "color": "#000000",
                "wrap": True
              }
            ],
            "offsetStart": "4%",
            "offsetBottom": "5%"
          }
        ],
        "height": "270px",
        "paddingAll": "0px"
      }
    }
  }
  return bubble


def flex_usdcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
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
                "backgroundColor": "#3c3c3c",
                "height": "32%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://kasikornresearch.com/SiteCollectionDocuments/analysis/business/money/HardBaht_Banner.jpg",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
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
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "({}%)".format(chgp),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
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
                    "type": "text",
                    "text": "Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "40%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Open Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} ~ {}".format(start,buy),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "52%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Close Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "64%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Target",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "76%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble

def flex_goldcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
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
                "backgroundColor": "#3c3c3c",
                "height": "32%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://a.c-dn.net/b/1OiQ5h/headline_GOLD_14.JPG",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
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
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "({})".format(chgp),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
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
                    "type": "text",
                    "text": "Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "40%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Open Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} ~ {}".format(start,buy),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "52%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Close Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "64%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Target",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "76%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble

def flex_wticheck(text,price_now,change,chgp,notice,start,buy,stop,target):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
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
                "backgroundColor": "#3c3c3c",
                "height": "32%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://static.posttoday.com/media/content/2014/06/19/09FD4903F4224438B6C49E1817EBE7BF.jpg",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
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
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "({})".format(chgp),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
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
                    "type": "text",
                    "text": "Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "40%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Open Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} ~ {}".format(start,buy),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "52%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Close Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "64%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Target",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "76%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble

def flex_tfexcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
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
                "backgroundColor": "#3c3c3c",
                "height": "32%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://akm-img-a-in.tosshub.com/sites/btmt/images/stories/shares_1280_20180404115810324_660x450_020120061652.jpg",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
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
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "({})".format(chgp),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
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
                    "type": "text",
                    "text": "Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "40%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Open Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} ~ {}".format(start,buy),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "52%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Close Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "64%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Target",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "76%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble

def flex_setcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
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
                "backgroundColor": "#3c3c3c",
                "height": "32%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://d1sr9z1pdl3mb7.cloudfront.net/wp-content/uploads/2018/03/09172121/stock-market.jpg",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
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
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "({}%)".format(chgp),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
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
                    "type": "text",
                    "text": "Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "40%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Open Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} ~ {}".format(start,buy),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "52%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Close Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "64%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Target",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "76%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble



