

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
        known = mydb["imc_realtime"]

        list_to_process = []
        mongo_alarm = {}

        myquery = {"u_process": 'no'}
        records = list(known.find(myquery))

        for alarm in records:
            mongo_alarm['u_id'] = alarm['u_id']
            mongo_alarm['u_severity'] = alarm['u_severity']
            mongo_alarm['u_deviceDisplay'] = alarm['u_deviceDisplay']
            mongo_alarm['u_faultDesc'] = alarm['u_faultDesc']
            mongo_alarm['u_sourceIp'] = alarm['u_sourceIp']
            mongo_alarm['u_faultTime'] = alarm['u_faultTime']
            mongo_alarm['u_userAckType'] = alarm['u_userAckType']
            mongo_alarm['userAckUserName'] = alarm['u_userAckUserName']
            mongo_alarm['u_process'] = 'no'
            list_to_process.append(mongo_alarm)
            mongo_alarm = {}

        return (list_to_process)
