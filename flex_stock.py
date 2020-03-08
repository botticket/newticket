def flex_THB(text,word_to_reply,usthbspot,Percent,IQXUSTHB,comment):
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://assets.brandinside.asia/uploads/2019/01/shutterstock-222371167-1.jpg",
        "align": "center",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "backgroundColor": "#000000",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "{}".format(text),
            "margin": "none",
            "size": "xl",
            "weight": "bold",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Position",
                "margin": "sm",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Today",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(usthbspot),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(Percent),
                "size": "md",
                "align": "start",
                "weight": "bold",
                "color": "#000000",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Qtr",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(IQXUSTHB),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "THB",
                "size": "xxs",
                "align": "start",
                "weight": "bold",
                "color": "#FFFFFF",
                "wrap": True
              }
            ]
          },
          {
            "type": "text",
            "text": "{}".format(comment),
            "size": "lg",
            "align": "start",
            "weight": "bold",
            "color": "#000000",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  }
  return bubble

def flex_WTI(text,word_to_reply,wtispot,Percent,IQXWTI,comment):
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7icaWqM8AO9KUzxO6hfd6zhu6_ADj0YXjuUVjRhSJeFgkdKsT",
        "align": "center",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "backgroundColor": "#000000",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "{}".format(text),
            "margin": "none",
            "size": "xl",
            "weight": "bold",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Position",
                "margin": "sm",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "gold",
                "size": "sm",
                "color": "#FFFEFE"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Today",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(wtispot),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(Percent),
                "size": "md",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Qtr",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(IQXWTI),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "G",
                "size": "xxs",
                "align": "start",
                "weight": "bold",
                "color": "#FFFFFF"
              }
            ]
          },
          {
            "type": "text",
            "text": "{}".format(comment),
            "size": "lg",
            "align": "start",
            "weight": "bold",
            "color": "#000000",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  }
  return bubble

def flex_gold(text,word_to_reply,gspot,Percent,IQXGL,comment):
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://siamblockchain.com/wp-content/uploads/2020/01/inbound6085994153059343074.jpg",
        "align": "center",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "backgroundColor": "#000000",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "{}".format(text),
            "margin": "none",
            "size": "xl",
            "weight": "bold",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Position",
                "margin": "sm",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "gold",
                "size": "sm",
                "color": "#FFFEFE"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Today",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(gspot),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(Percent),
                "size": "md",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Qtr",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(IQXGL),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "G",
                "size": "xxs",
                "align": "start",
                "weight": "bold",
                "color": "#FFFFFF"
              }
            ]
          },
          {
            "type": "text",
            "text": "{}".format(comment),
            "size": "lg",
            "align": "start",
            "weight": "bold",
            "color": "#000000",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  }
  return bubble

def flex_tfex(text,word_to_reply,tfex_now,Percent,tfexx,comment):
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://vnn-imgs-f.vgcloud.vn/2019/12/27/19/10-important-hallmarks-of-vietnam-s-stock-market-in-2019.jpg",
        "align": "center",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "backgroundColor": "#000000",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "{}".format(text),
            "margin": "none",
            "size": "xl",
            "weight": "bold",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Position",
                "margin": "sm",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "gold",
                "size": "sm",
                "color": "#FFFEFE"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Today",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(tfex_now),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(Percent),
                "size": "md",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Qtr",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(tfexx),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "F",
                "size": "xxs",
                "align": "start",
                "weight": "bold",
                "color": "#FFFFFF"
              }
            ]
          },
          {
            "type": "text",
            "text": "{}".format(comment),
            "size": "lg",
            "align": "start",
            "weight": "bold",
            "color": "#000000",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  }
  return bubble

def flex_set(text,word_to_reply,set_now,Percent,sett,comment):
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://southerntimesafrica.com/uploads/intro.jpg",
        "align": "center",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "backgroundColor": "#000000",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "{}".format(text),
            "margin": "none",
            "size": "xl",
            "weight": "bold",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Position",
                "margin": "sm",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(word_to_reply),
                "size": "lg",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "gold",
                "size": "sm",
                "color": "#FFFEFE"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Today",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(set_now),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(Percent),
                "size": "md",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Qtr",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(sett),
                "size": "md",
                "align": "end",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "S",
                "size": "xxs",
                "align": "start",
                "weight": "bold",
                "color": "#FFFFFF"
              }
            ]
          },
          {
            "type": "text",
            "text": "{}".format(comment),
            "size": "lg",
            "align": "start",
            "weight": "bold",
            "color": "#000000",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  }
  return bubble

def flex_stock(notice,text,stop,open,buy,price_now,change,target):
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://vnn-imgs-f.vgcloud.vn/2019/12/27/19/10-important-hallmarks-of-vietnam-s-stock-market-in-2019.jpg",
        "align": "center",
        "gravity": "top",
        "size": "full",
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "backgroundColor": "#000000",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "{}".format(notice),
            "margin": "none",
            "size": "xl",
            "weight": "bold",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(text),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Now",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(price_now),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(change),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Buy",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(open),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000",
                "wrap": True
              },
              {
                "type": "text",
                "text": "{}".format(buy),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "none",
            "contents": [
              {
                "type": "text",
                "text": "Stop",
                "margin": "sm",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(stop),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "gold",
                "size": "sm",
                "color": "#FFFEFE"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Target",
                "size": "lg",
                "weight": "bold",
                "color": "#000000"
              },
              {
                "type": "text",
                "text": "{}".format(target),
                "size": "lg",
                "align": "start",
                "weight": "bold",
                "color": "#000000",
                "wrap": True
              },
              {
                "type": "text",
                "text": ".",
                "size": "sm",
                "color": "#FFFEFE"
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xs"
          }
        ]
      }
    }
  }
  return bubble