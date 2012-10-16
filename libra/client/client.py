# Copyright 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from libraapi import LibraAPI
from clientoptions import ClientOptions


def main():
    options = ClientOptions()
    args = options.run()

    api = LibraAPI(args.os_username, args.os_password, args.os_tenant_name,
                   args.os_auth_url, args.os_region_name)

    if args.command == 'list':
        api.list_lb()
    elif args.command == 'status':
        api.get_lb(args.lbid)
    elif args.command == 'modify':
        api.modify_lb(args)
    elif args.command == 'create':
        api.create_lb(args)

    return 0
