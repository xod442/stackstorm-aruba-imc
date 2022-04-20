

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

        mydb = self.dbclient["arubaimc"]
        known = mydb["imc_alarms"]

        list_to_process = []
        alarm = {}

        myquery = {"u_process": 'no'}
        records = list(known.find(myquery))

        for alarm in records:
            new_alarm['u_id'] = alarm['u_id']
            new_alarm['u_OID'] = alarm['u_OID']
            new_alarm['u_originalType'] = alarm['u_originalType']
            new_alarm['u_originalTypeDesc'] = alarm['u_originalTypeDesc']
            new_alarm['u_deviceId'] = alarm['u_deviceId']
            new_alarm['u_deviceIp'] = alarm['u_deviceIp']
            new_alarm['u_deviceName'] = alarm['u_deviceName']
            new_alarm['u_alarmLevel'] = alarm['u_alarmLevel']
            new_alarm['u_alarmLevelDesc'] = alarm['u_alarmLevelDesc']
            new_alarm['u_alarmCategory'] = alarm['u_alarmCategory']
            new_alarm['u_faultTime'] = alarm['u_faultTime']
            new_alarm['u_faultTimeDesc'] = alarm['u_faultTimeDesc']
            new_alarm['u_recTime'] = alarm['u_recTime']
            new_alarm['u_recTimeDesc'] = alarm['u_recTimeDesc']
            new_alarm['u_recStatus'] = alarm['u_recStatus']
            new_alarm['u_recStatusDesc'] = alarm['u_recStatusDesc']
            new_alarm['u_recUserName'] = alarm['u_recUserName']
            new_alarm['u_ackTime'] = alarm['u_ackTime']
            new_alarm['u_ackTimeDesc'] = alarm['u_ackTimeDesc']
            new_alarm['u_ackStatus'] = alarm['u_ackStatus']
            new_alarm['u_ackStatusDesc'] = alarm['u_ackStatusDesc']
            new_alarm['u_ackUserName'] = alarm['u_ackUserName']
            new_alarm['u_alarmDesc'] = alarm['u_alarmDesc']
            new_alarm['u_parentId'] = alarm['u_parentId']
            new_alarm['u_somState'] = alarm['u_somState']
            new_alarm['u_remark'] = alarm['u_remark']
            new_alarm['u_holdInfo'] = alarm['u_holdInfo']
            new_alarm['u_repeats'] = alarm['u_repeats']
            new_alarm['u_resSourceType'] = alarm['u_resSourceType']
            new_alarm['u_alarmDetail'] = alarm['u_alarmDetail']
            new_alarm['u_process'] = 'no'
            info = json.dumps(new_alarm)
            list_to_process.append(info)
            new_alarm = {}

        return (list_to_process)
