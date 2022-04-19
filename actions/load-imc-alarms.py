

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
            myquery = {"u_id": alarm[10]}
            records = known.find(myquery).count()
            if records == 0:
                new_alarm['id'] = alarm[] alarm[]
                new_alarm['OID'] = alarm[]
                new_alarm['originalType'] = alarm[]
                new_alarm['originalTypeDesc'] = alarm[]
                new_alarm['deviceId'] = alarm[]
                new_alarm['deviceIp'] = alarm[]
                new_alarm['deviceName'] = alarm[]
                new_alarm['alarmLevel'] = alarm[]
                new_alarm['alarmLevelDesc'] = alarm[]
                new_alarm['alarmCategory'] = alarm[]
                new_alarm['faultTime'] = alarm[]
                new_alarm['faultTimeDesc'] = alarm[]
                new_alarm['recTime'] = alarm[]
                new_alarm['recTimeDesc'] = alarm[]
                new_alarm['recStatus'] = alarm[]
                new_alarm['recStatusDesc'] = alarm[]
                new_alarm['recUserName'] = alarm[]
                new_alarm['ackTime'] = alarm[]
                new_alarm['ackTimeDesc'] = alarm[]
                new_alarm['ackStatus'] = alarm[]
                new_alarm['ackStatusDesc'] = alarm[]
                new_alarm['ackUserName'] = alarm[]
                new_alarm['alarmDesc'] = alarm[]
                new_alarm['parentId' =
                new_alarm['somState'] = alarm[]
                new_alarm['remark'] = alarm[]
                new_alarm['holdInfo'] = alarm[]
                new_alarm['repeats'] = alarm[]
                new_alarm['resSourceType'] = alarm[]
                new_alarm['alarmDetail'] = alarm[]
                new_alarm['process'] = 'no'
                write_record = known.insert_one(new_alarm)
                new_alarm = {}

            else:
                records = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
