

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

        mydb = self.dbclient["arubaimc"]
        known = mydb["imc_alarms"]

        mongo_alarm = {}

        for alarm in alarms:
            myquery = {"u_id": alarm[0]}
            records = known.find(myquery).count()
            if records == 0:
                mongo_alarm['u_id'] = alarm[0]
                mongo_alarm['u_OID'] = alarm[1]
                mongo_alarm['u_originalType'] = alarm[2]
                mongo_alarm['u_originalTypeDesc'] = alarm[3]
                mongo_alarm['u_deviceId'] = alarm[4]
                mongo_alarm['u_deviceIp'] = alarm[5]
                mongo_alarm['u_deviceName'] = alarm[6]
                mongo_alarm['u_alarmLevel'] = alarm[7]
                mongo_alarm['u_alarmLevelDesc'] = alarm[8]
                mongo_alarm['u_alarmCategory'] = alarm[9]
                mongo_alarm['u_faultTime'] = alarm[10]
                mongo_alarm['u_faultTimeDesc'] = alarm[11]
                mongo_alarm['u_recTime'] = alarm[12]
                mongo_alarm['u_recTimeDesc'] = alarm[13]
                mongo_alarm['u_recStatus'] = alarm[14]
                mongo_alarm['u_recStatusDesc'] = alarm[15]
                mongo_alarm['u_recUserName'] = alarm[16]
                mongo_alarm['u_ackTime'] = alarm[17]
                mongo_alarm['u_ackTimeDesc'] = alarm[18]
                mongo_alarm['u_ackStatus'] = alarm[19]
                mongo_alarm['u_ackStatusDesc'] = alarm[20]
                mongo_alarm['u_ackUserName'] = alarm[21]
                mongo_alarm['u_alarmDesc'] = alarm[22]
                mongo_alarm['u_parentId'] = alarm[23]
                mongo_alarm['u_somState'] = alarm[24]
                mongo_alarm['u_remark'] = alarm[25]
                mongo_alarm['u_holdInfo'] = alarm[26]
                mongo_alarm['u_repeats'] = alarm[27]
                mongo_alarm['u_resSourceType'] = alarm[28]
                mongo_alarm['u_alarmDetail'] = alarm[29]
                mongo_alarm['u_process'] = 'no'
                write_record = known.insert_one(mongo_alarm)
                mongo_alarm = {}

            else:
                records = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
