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

import eventlet


def stats_manager(logger, driver):
    logger.debug("Statistics gathering process started.")

    while True:
        try:
            driver.get_stats()
        except NotImplementedError:
            logger.warn("Driver does not implement statisics gathering.")
            break

        eventlet.sleep(60)

    logger.info("Statistics gathering process terminated.")
