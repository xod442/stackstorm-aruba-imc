

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
        mongo_alarm = {}

        myquery = {"u_process": 'no'}
        records = list(known.find(myquery))
        # set lowercase variable names for servicenow
        for alarm in records:
            mongo_alarm['u_id'] = str(alarm['u_id'])
            mongo_alarm['u_deviceip'] = str(alarm['u_deviceIp'])
            mongo_alarm['u_faulttimedesc'] = str(alarm['u_faultTimeDesc'])
            mongo_alarm['u_recstatusdesc'] = str(alarm['u_recStatusDesc'])
            mongo_alarm['u_alarmdesc'] = str(alarm['u_alarmDesc'])
            list_to_process.append(mongo_alarm)
            mongo_alarm = {}

        return (list_to_process)
