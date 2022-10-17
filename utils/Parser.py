#-*- coding: UTF-8 -*-


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

