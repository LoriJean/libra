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

import argparse
import ConfigParser


class Options(object):
    def __init__(self, title):
        self.title = title
        self._parse_args()
        self._load_config()

    def _parse_args(self):
        parser = argparse.ArgumentParser(
            description='Libra {title}'.format(title=self.title)
        )
        parser.add_argument('config', help='configuration file', type=file)
        parser.add_argument(
            '-d', dest='nodaemon', action='store_true',
            help='do not run in daemon mode'
        )

        self.args = parser.parse_args()

    def _load_config(self):
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(self.args.config)