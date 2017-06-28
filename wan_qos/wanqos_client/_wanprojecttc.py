# Copyright 2017 Huawei corp.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from neutronclient._i18n import _

from neutronclient.common import extension
from neutronclient.common import exceptions

from wan_qos.common import constants


class WanProjectTc(extension.NeutronClientExtension):
    resource = constants.WAN_PROJECT_TC
    resource_plural = '%ss' % constants.WAN_PROJECT_TC
    path = constants.WAN_PROJECT_TC_PATH
    object_path = '/%s' % path
    resource_path = '/%s/%%s' % path
    versions = ['2.0']


class WanProjectTcShow(extension.ClientExtensionShow, WanProjectTc):
    shell_command = 'wan-project-tc-show'


class WanProjectTcList(extension.ClientExtensionList, WanProjectTc):
    shell_command = 'wan-project-tc-list'
    list_columns = ['id', 'project', 'min', 'max']
    pagination_support = True
    sorting_support = True


class WanProjectTcCreate(extension.ClientExtensionCreate, WanProjectTc):
    shell_command = 'wan-project-tc-create'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--min',
            dest='min',
            help=_('Set committed rate. (mbit / kbit)'))
        parser.add_argument(
            '--max',
            dest='max',
            help=_('Set maximum rate. (mbit / kbit)'))
        parser.add_argument(
            'project', metavar='<project>',
            help=_("Set the project to limit all it's networks"))

    def args2body(self, parsed_args):

        body = {
            'project': parsed_args.project
        }

        if parsed_args.min:
            body['min'] = parsed_args.min
        else:
            if not parsed_args.max:
                raise exceptions.BadRequest('Either min or max must be set')

        if parsed_args.max:
            body['max'] = parsed_args.max

        return {self.resource: body}


class WanProjectTcDelete(extension.ClientExtensionDelete, WanProjectTc):
    shell_command = 'wan-project-tc-delete'


class WanProjectTcUpdate(extension.ClientExtensionUpdate, WanProjectTc):
    shell_command = 'wan-project-tc-update'

    def add_known_arguments(self, parser):
        pass

    def args2body(self, parsed_args):
        body = {}
        return {self.resource: body}
