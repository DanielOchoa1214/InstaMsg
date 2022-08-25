import pywhatkit as pwk


def sendMsg(phone, hour, minute, msg):
    pwk.sendwhatmsg(phone, msg, hour, minute, 10, True, 2)
