

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

__all__ = [
    'LoadDb'
]


class LoadDb(MongoBaseAction):
    def run(self, alarms):

        mydb = self.dbclient["app_db"]
        known = mydb["imc_alarms"]

        new_alarm = {}

        for alarm in alarms:
            myquery = {"u_id": alarm[0]}
            records = known.find(myquery).count()
            if records == 0:
                new_alarm['id'] = alarm[0]
                new_alarm['OID'] = alarm[1]
                new_alarm['originalType'] = alarm[2]
                new_alarm['originalTypeDesc'] = alarm[3]
                new_alarm['deviceId'] = alarm[4]
                new_alarm['deviceIp'] = alarm[5]
                new_alarm['deviceName'] = alarm[6]
                new_alarm['alarmLevel'] = alarm[7]
                new_alarm['alarmLevelDesc'] = alarm[8]
                new_alarm['alarmCategory'] = alarm[9]
                new_alarm['faultTime'] = alarm[10]
                new_alarm['faultTimeDesc'] = alarm[11]
                new_alarm['recTime'] = alarm[12]
                new_alarm['recTimeDesc'] = alarm[13]
                new_alarm['recStatus'] = alarm[14]
                new_alarm['recStatusDesc'] = alarm[15]
                new_alarm['recUserName'] = alarm[16]
                new_alarm['ackTime'] = alarm[17]
                new_alarm['ackTimeDesc'] = alarm[18]
                new_alarm['ackStatus'] = alarm[19]
                new_alarm['ackStatusDesc'] = alarm[20]
                new_alarm['ackUserName'] = alarm[21]
                new_alarm['alarmDesc'] = alarm[22]
                new_alarm['parentId' = alarm[23]
                new_alarm['somState'] = alarm[24]
                new_alarm['remark'] = alarm[25]
                new_alarm['holdInfo'] = alarm[26]
                new_alarm['repeats'] = alarm[27]
                new_alarm['resSourceType'] = alarm[28]
                new_alarm['alarmDetail'] = alarm[29]
                new_alarm['process'] = 'no'
                write_record = known.insert_one(new_alarm)
                new_alarm = {}

            else:
                records = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
