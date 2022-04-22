

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
    def run(self, devices):

        mydb = self.dbclient["arubaimc"]
        known = mydb["imc_devices"]

        mongo_device = {}

        for device in devices:
            if known.count_documents({ 'u_id': device['id'] }, limit = 1) == 0:
                mongo_device['u_id'] = alarm[0]
                mongo_device['u_label'] = alarm[1]
                mongo_device['u_ip'] = alarm[2]
                mongo_device['u_mask'] = alarm[3]
                mongo_device['u_status'] = alarm[4]
                mongo_device['u_statusDesc'] = alarm[5]
                mongo_device['u_sysName'] = alarm[6]
                mongo_device['u_contact'] = alarm[7]
                mongo_device['u_location'] = alarm[8]
                mongo_device['u_sysOid'] = alarm[9]
                mongo_device['u_sysDescription'] = alarm[10]
                mongo_device['u_devCategoryImgSrc'] = alarm[11]
                mongo_device['u_topoIconName'] = alarm[12]
                mongo_device['u_devPingState'] = alarm[13]
                mongo_device['u_categoryId'] = alarm[14]
                mongo_device['u_symbolId'] = alarm[15]
                mongo_device['u_symbolName'] = alarm[16]
                mongo_device['u_symbolType'] = alarm[17]
                mongo_device['u_symbolDesc'] = alarm[18]
                mongo_device['u_symbolLevel'] = alarm[19]
                mongo_device['u_parentId'] = alarm[20]
                mongo_device['u_typeName'] = alarm[21]
                mongo_device['u_process'] = 'no'
                write_record = known.insert_one(mongo_device)
                mongo_device = {}

            else:
                records = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
