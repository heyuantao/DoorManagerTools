#-*- coding: UTF-8 -*-
import json
from data.MegviiDoorManagerCallBackExampleData import call_back_str_array
from utils.Parser import DoorManagerRecordParser

if __name__=="__main__":
    from db import Database
    db = Database()
    for line in call_back_str_array:
        decode_line = line.decode("UTF-8")
        dict_item = json.loads(decode_line)
        parse = DoorManagerRecordParser

        if parse.isUser(dict_item):
            # print("教师 {} 打开了 {}".format(parse.name(dict_item), parse.location(dict_item)))
            item = {"id": parse.uuid(dict_item), "name": parse.name(dict_item), "location": parse.location(dict_item),
                    "type": "user", \
                    "timestamp": parse.timestamp(dict_item), "time": str(parse.time(dict_item))}
            db.add_success_open_record(json.dumps(item))
        elif parse.isGuest(dict_item):
            # print("{} 设置的访客 {} 打开了 {}".format(parse.visitedName(dict_item),parse.name(dict_item),parse.location(dict_item)))
            item = {"id": parse.uuid(dict_item), "name": parse.name(dict_item), "location": parse.location(dict_item),
                    "type": "guest", \
                    "timestamp": parse.timestamp(dict_item), "time": str(parse.time(dict_item)), \
                    "visited": parse.visitedName(dict_item)}
            db.add_success_open_record(json.dumps(item))
        else:
            item = {"id": parse.uuid(dict_item), "location": parse.location(dict_item), \
                    "timestamp": parse.timestamp(dict_item), "time": str(parse.time(dict_item))}
            db.add_failure_open_record(json.dumps(item))
        #print(dict_item)
        #print("发生开门事件在{},记录编号为{}".format(DoorManagerRecordParser.time(dict_item),DoorManagerRecordParser.uuid(dict_item)))
        #if DoorManagerRecordParser.isUser(dict_item):
        #    print("教师 {} 打开了 {}".format(DoorManagerRecordParser.name(dict_item),DoorManagerRecordParser.location(dict_item)))
        #if DoorManagerRecordParser.isGuest(dict_item):
        #    print("{} 设置的访客 {} 打开了 {}".format(DoorManagerRecordParser.visitedName(dict_item),DoorManagerRecordParser.name(dict_item),DoorManagerRecordParser.location(dict_item)))
