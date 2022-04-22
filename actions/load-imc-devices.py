

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

        db = self.dbclient["arubaimc"]


        mongo_device = {}

        for device in devices:
            message = 'processing documents'
            if db.imc_devices.count_documents({ 'u_id': device[0] }, limit = 1) == 0:
                mongo_device['u_id'] = device[0]
                mongo_device['u_label'] = device[1]
                mongo_device['u_ip'] = device[2]
                mongo_device['u_mask'] = device[3]
                mongo_device['u_status'] = device[4]
                mongo_device['u_statusDesc'] = device[5]
                mongo_device['u_sysName'] = device[6]
                mongo_device['u_contact'] = device[7]
                mongo_device['u_location'] = device[8]
                mongo_device['u_sysOid'] = device[9]
                mongo_device['u_sysDescription'] = device[10]
                mongo_device['u_devCategoryImgSrc'] = device[11]
                mongo_device['u_topoIconName'] = device[12]
                mongo_device['u_devPingState'] = device[13]
                mongo_device['u_categoryId'] = device[14]
                mongo_device['u_symbolId'] = device[15]
                mongo_device['u_symbolName'] = device[16]
                mongo_device['u_symbolType'] = device[17]
                mongo_device['u_symbolDesc'] = device[18]
                mongo_device['u_symbolLevel'] = device[19]
                mongo_device['u_parentId'] = device[20]
                mongo_device['u_typeName'] = device[21]
                mongo_device['u_process'] = 'no'
                write_record = db.imc_devices.insert_one(mongo_device)
                mongo_device = {}

            else:
                message = 'Fail to write mongo record, possible duplicate'
        return (message)
