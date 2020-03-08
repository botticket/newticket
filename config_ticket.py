from line_notify import LineNotify

def linechat(text):
    
    ACCESS_TOKEN = "aTxnvziRz4xRKn3rMkWmlNSgnMVR7RRGOSloFIx0OQA"

    notify = LineNotify(ACCESS_TOKEN)

    notify.send(text)