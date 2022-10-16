#-*- coding: UTF-8 -*-

from data.MegviiDoorManagerCallBackExampleData import call_back_str_array
import json
import datetime
import pytz

class DoorManagerRecordParser:

    @classmethod
    def isGuest(cls,recordDict):
        if recordDict.__contains__("visitPeronUuid"):
            return True
        else:
            return False

    @classmethod
    def isUser(cls,recordDict):
        if (recordDict.__contains__("personName")) and (not recordDict.__contains__("visitPeronUuid")):
            return True
        else:
            return False
    @classmethod
    def name(cls,recordDict):
        return recordDict['personName']

    @classmethod
    def visitedName(cls,recordDict):
        return recordDict['visitPersonName']

    @classmethod
    def location(cls,recordDict):
        return recordDict['deviceName']

    @classmethod
    def timestamp(cls,recordDict):
        return recordDict['passTimestamp']  #passTimestamp #passTime

    @classmethod
    def time(cls, recordDict):
        time_stamp = recordDict['passTimestamp']
        current_time_zone = pytz.timezone("Asia/Shanghai")
        the_time = datetime.datetime.fromtimestamp(time_stamp/1e3, tz=current_time_zone)
        return  the_time 

if __name__=="__main__":
    for line in call_back_str_array:
        decode_line = line.decode("UTF-8")
        dict_item = json.loads(decode_line)
        print(dict_item)
        print("发生开门事件在{}".format(DoorManagerRecordParser.time(dict_item)))
        if DoorManagerRecordParser.isUser(dict_item):
            print("教师 {} 打开了 {}".format(DoorManagerRecordParser.name(dict_item),DoorManagerRecordParser.location(dict_item)))
        if DoorManagerRecordParser.isGuest(dict_item):
            print("{} 设置的访客 {} 打开了 {}".format(DoorManagerRecordParser.visitedName(dict_item),DoorManagerRecordParser.name(dict_item),DoorManagerRecordParser.location(dict_item)))