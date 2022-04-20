

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
        known = mydb["imc_devices"]

        list_to_process = []
        mongo_alarm = {}

        myquery = {"u_process": 'no'}
        records = list(known.find(myquery))

        for alarm in records:
            mongo_alarm['u_id'] = alarm['u_id']
            mongo_alarm['u_label'] = alarm['u_label']
            mongo_alarm['u_ip'] = alarm['u_ip']
            mongo_alarm['u_mask'] = alarm['u_mask']
            mongo_alarm['u_status'] = alarm['u_status']
            mongo_alarm['u_statusDesc'] = alarm['u_statusDesc']
            mongo_alarm['u_sysName'] = alarm['u_sysName']
            mongo_alarm['u_contact'] = alarm['u_contact']
            mongo_alarm['u_location'] = alarm['u_location']
            mongo_alarm['u_sysOid'] = alarm['u_sysOid']
            mongo_alarm['u_sysDescription'] = alarm['u_sysDescription']
            mongo_alarm['u_devCategoryImgSrc'] = alarm['u_devCategoryImgSrc']
            mongo_alarm['u_topoIconName'] = alarm['u_topoIconName']
            mongo_alarm['u_devPingState'] = alarm['u_devPingState']
            mongo_alarm['u_categoryId'] = alarm['u_categoryId']
            mongo_alarm['u_symbolId'] = alarm['u_symbolId']
            mongo_alarm['u_symbolName'] = alarm['u_symbolName']
            mongo_alarm['u_symbolType'] = alarm['u_symbolType']
            mongo_alarm['u_symbolDesc'] = alarm['u_symbolDesc']
            mongo_alarm['u_symbolLevel'] = alarm['u_symbolLevel']
            mongo_alarm['u_parentId'] = alarm['u_parentId']
            mongo_alarm['u_typeName'] = alarm['u_typeName']
            mongo_alarm['u_process'] = 'no'
            info = json.dumps(mongo_alarm)
            list_to_process.append(info)
            mongo_alarm = {}

        return (list_to_process)
