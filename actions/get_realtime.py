

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
from pyarubaimc.alarms import *
urllib3.disable_warnings()

__all__ = [
    'AlarmData'
]


class AlarmData(ArubaImcBaseAction):
    def run(self):
        alarm_list = []
        # The word admin tells IMC you want all of the alarms
        realtime = get_realtime_alarm('admin', self.auth.creds, self.auth.url)

        # Check to see if we only got one entry from IMC in the form of a dict
        if isinstance(realtime, dict):
            realtime = [realtime]

        for item in realtime:
            info = [
                    item['id'],
                    item['severity'],
                    item['deviceDisplay'],
                    item['faultDesc'],
                    item['sourceIp'],
                    item['faultTime'],
                    item['userAckType'],
                    item['userAckUserName']
                    ]

            alarm_list.append(info)
            info = []
        return alarm_list
