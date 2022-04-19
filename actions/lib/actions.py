
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman."
# __email__ = "rick@riickkauffman.com"

from pymongo import MongoClient
from pyhpeimc.auth import *
from st2common.runners.base_action import Action

__all__ = [
    'ArubaImcBaseAction'
]


class ArubaImcBaseAction(Action):
    def __init__(self, config):
        super(ArubaImcBaseAction, self).__init__(config=config)
        self.auth = self._get_auth()

    def _get_auth(self):
        imc_host = self.config['host']
        imc_user = self.config['username']
        imc_password = self.config['password']

        auth = IMCAuth("http://", imc_host, "8080", imc_user, imc_password)

        return auth


class MongoBaseAction(Action):
    def __init__(self, config):
        super(MongoBaseAction, self).__init__(config=config)
        self.dbclient = self._get_db_client()

    def _get_db_client(self):
        # Uncomment dbuser & dbpass if using password protected mongo database
        # dbuser = self.config['dbuser']
        # dbpass = self.config['dbpass']

        # If running stackstorm in a singlehost deployment use this command
        # dbclient =
        # MongoClient('mongodb://%s:%s@localhost:27017/' % (dbuser,dbpass))

        # If using stackstorm in multiple docker containers use this command
        dbclient = MongoClient('mongodb://mongo:27017/')

        return dbclient
