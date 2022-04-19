

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#------------------------------------------------------------------------------#
#                                                                              #
#          ╔═╗┬─┐┬ ┬┌┐ ┌─┐  ╦╔╦╗╔═╗  ╔═╗┌─┐┌─┐┬┌─                              #
#          ╠═╣├┬┘│ │├┴┐├─┤  ║║║║║    ╠═╝├─┤│  ├┴┐                              #
#          ╩ ╩┴└─└─┘└─┘┴ ┴  ╩╩ ╩╚═╝  ╩  ┴ ┴└─┘┴ ┴                              #
#                                                                              #
# __author__ = "@netwookie"                                                    #
# __credits__ = ["Rick Kauffman"]                                              #
# __license__ = "Apache2.0"                                                    #
# __maintainer__ = "Rick Kauffman"                                             #
# __email__ = "rick#rickkauffman.com"                                          #
#                                                                              #
#                                                                              #
#------------------------------------------------------------------------------#
from lib.actions import MongoBaseAction
import json

__all__ = [
    'GetDb'
]


class GetDb(MongoBaseAction):
    def run(self):

        mydb = self.dbclient["app_db"]
        known = mydb["imc_alarms"]

        list_to_process = []
        alarm = {}

        myquery = {"u_process": 'no'}
        records = list(known.find(myquery))

        for alarm in records:
            new_alarm['id'] = alarm['id']
            new_alarm['OID'] = alarm['OID']
            new_alarm['originalType'] = alarm['originalType']
            new_alarm['originalTypeDesc'] = alarm['originalTypeDesc']
            new_alarm['deviceId'] = alarm['deviceId']
            new_alarm['deviceIp'] = alarm['deviceIp']
            new_alarm['deviceName'] = alarm['deviceName']
            new_alarm['alarmLevel'] = alarm['alarmLevel']
            new_alarm['alarmLevelDesc'] = alarm['alarmLevelDesc']
            new_alarm['alarmCategory'] = alarm['alarmCategory']
            new_alarm['faultTime'] = alarm['faultTime']
            new_alarm['faultTimeDesc'] = alarm['faultTimeDesc']
            new_alarm['recTime'] = alarm['recTime']
            new_alarm['recTimeDesc'] = alarm['recTimeDesc']
            new_alarm['recStatus'] = alarm['recStatus']
            new_alarm['recStatusDesc'] = alarm['recStatusDesc']
            new_alarm['recUserName'] = alarm['recUserName']
            new_alarm['ackTime'] = alarm['ackTime']
            new_alarm['ackTimeDesc'] = alarm['ackTimeDesc']
            new_alarm['ackStatus'] = alarm['ackStatus']
            new_alarm['ackStatusDesc'] = alarm['ackStatusDesc']
            new_alarm['ackUserName'] = alarm['ackUserName']
            new_alarm['alarmDesc'] = alarm['alarmDesc']
            new_alarm['parentId'] = alarm['parentId']
            new_alarm['somState'] = alarm['somState']
            new_alarm['remark'] = alarm['remark']
            new_alarm['holdInfo'] = alarm['holdInfo']
            new_alarm['repeats'] = alarm['repeats']
            new_alarm['resSourceType'] = alarm['resSourceType']
            new_alarm['alarmDetail'] = alarm['alarmDetail']
            new_alarm['process'] = 'no'
            info = json.dumps(new_alarm)
            list_to_process.append(info)
            new_alarm = {}

        return (list_to_process)
