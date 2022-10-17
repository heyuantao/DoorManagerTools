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

    @classmethod
    def uuid(cls, recordDict):
        time_stamp = recordDict['passTimestamp']
        device_uuid = recordDict['deviceUuid']
        record_unique_id = "{}:{}".format(device_uuid,time_stamp)
        return record_unique_id

if __name__=="__main__":
    from db import Database
    db = Database()
    for line in call_back_str_array:
        decode_line = line.decode("UTF-8")
        dict_item = json.loads(decode_line)
        parse = DoorManagerRecordParser
        # print("发生开门事件在{},记录编号为{}".format(parse.time(dict_item), parse.uuid(dict_item)))
        if parse.isUser(dict_item):
            # print("教师 {} 打开了 {}".format(parse.name(dict_item), parse.location(dict_item)))
            item = {"id": parse.uuid(dict_item), "name": parse.name(dict_item), "location": parse.location(dict_item),
                    "type": "user", \
                    "timestamp": parse.timestamp(dict_item)}
            db.add_success_open_record(json.dumps(item))
        elif parse.isGuest(dict_item):
            # print("{} 设置的访客 {} 打开了 {}".format(parse.visitedName(dict_item),parse.name(dict_item),parse.location(dict_item)))
            item = {"id": parse.uuid(dict_item), "name": parse.name(dict_item), "location": parse.location(dict_item),
                    "type": "guest", \
                    "timestamp": parse.timestamp(dict_item), "visited": parse.visitedName(dict_item)}
            db.add_success_open_record(json.dumps(item))
        else:
            item = {"id": parse.uuid(dict_item), "location": parse.location(dict_item), \
                    "timestamp": parse.timestamp(dict_item)}
            db.add_failure_open_record(json.dumps(item))
        #print(dict_item)
        #print("发生开门事件在{},记录编号为{}".format(DoorManagerRecordParser.time(dict_item),DoorManagerRecordParser.uuid(dict_item)))
        #if DoorManagerRecordParser.isUser(dict_item):
        #    print("教师 {} 打开了 {}".format(DoorManagerRecordParser.name(dict_item),DoorManagerRecordParser.location(dict_item)))
        #if DoorManagerRecordParser.isGuest(dict_item):
        #    print("{} 设置的访客 {} 打开了 {}".format(DoorManagerRecordParser.visitedName(dict_item),DoorManagerRecordParser.name(dict_item),DoorManagerRecordParser.location(dict_item)))
