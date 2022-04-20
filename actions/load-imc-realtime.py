

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
        known = mydb["imc_realtime"]

        mongo_alarm = {}

        for alarm in alarms:
            records = known.count_documents({"u_id": alarm[0]})
            if records == 0:
                mongo_alarm['u_id'] = alarm[0]
                mongo_alarm['u_severity'] = alarm[1]
                mongo_alarm['u_deviceDisplay'] = alarm[2]
                mongo_alarm['u_faultDesc'] = alarm[3]
                mongo_alarm['u_sourceIp'] = alarm[4]
                mongo_alarm['u_faultTime'] = alarm[5]
                mongo_alarm['u_userAckType'] = alarm[6]
                mongo_alarm['u_userAckUserName'] = alarm[7]
                mongo_alarm['u_process'] = 'no'
                write_record = known.insert_one(mongo_alarm)
                mongo_alarm = {}

            else:
                records = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
