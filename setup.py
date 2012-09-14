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

import setuptools
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)

ci_cmdclass = {}

try:
    from sphinx.setup_command import BuildDoc

    class local_BuildDoc(BuildDoc):
        def run(self):
            for builder in ['html', 'man']:
                self.builder = builder
                self.finalize_options()
                BuildDoc.run(self)
    ci_cmdclass['build_sphinx'] = local_BuildDoc
except Exception:
    pass

ci_cmdclass['test'] = PyTest

setuptools.setup(
    name="lbaas_devices",
    description="Python LBaaS Gearman Worker and Pool Manager",
    version="1.0",
    author="David Shrewsbury <shrewsbury.dave@gmail.com>, \
        Andrew Hutchings <andrew@linuxjedi.co.uk>",
    packages=setuptools.find_packages(exclude=["*.tests"]),
    entry_points={
        'console_scripts': [
            'lbaas_worker = lbaas_worker.worker:main',
            'lbaas_pool_mgm = lbaas_mgm.mgm:main'
        ]
    },
    cmdclass=ci_cmdclass,
    tests_require=['pytest-pep8'],
    install_requires=['gearman', 'python-daemon'],
)
