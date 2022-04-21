

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
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

import urllib3
from lib.actions import ArubaImcBaseAction
from pyarubaimc.plat.device import *
urllib3.disable_warnings()

__all__ = [
    'Devices'
]


class Devices(ArubaImcBaseAction):
    def run(self):
        device_list = []
        # Get Devices
        devices = get_all_devs(self.auth.creds, self.auth.url)

        # Check to see if we only got one entry from IMC in the form of a dict
        if isinstance(devices, dict):
            devices = [devices]

        for item in devices:
            info = [
                    item['id'],
                    item['label'],
                    item['ip'],
                    item['mask'],
                    item['status'],
                    item['statusDesc'],
                    item['sysName'],
                    item['contact'],
                    item['location'],
                    item['sysOid'],
                    item['sysDescription'],
                    item['devCategoryImgSrc'],
                    item['topoIconName'],
                    item['devPingState'],
                    item['categoryId'],
                    item['symbolId'],
                    item['symbolName'],
                    item['symbolType'],
                    item['symbolDesc'],
                    item['symbolLevel'],
                    item['parentId'],
                    item['typeName']
                    ]

            device_list.append(info)
            info = []
        return device_list
