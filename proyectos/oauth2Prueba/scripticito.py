#!/usr/bin/env python
#
#Title: Script de pruebas
#Autor: Jose Joaquin Escobar Gomez
# 
# class Prueba():
#     """docstring for Prueba."""
#     def __init__(self, arg):
#         print "empezando"
#
#     def hola(args):
#         print "Hola mundo."
#
# prueba = Prueba(0)
# prueba.hola()


openstack --debug -v --os-auth-url=https://keystone.ifca.es:5000/ --os-username escobarj --os-password TFG4st@ck token issue
START with options: [u'--debug', u'-v', u'--os-auth-url=https://keystone.ifca.es:5000/', u'--os-username', u'escobarj', u'--os-password', u'TFG4st@ck', u'token', u'issue']
options: Namespace(auth_type='', auth_url=u'https://keystone.ifca.es:5000/', cacert=None, cert='', cloud='', debug=True, default_domain='default', default_domain_id='', default_domain_name='', deferred_help=False, domain_id='', domain_name='', endpoint='', insecure=None, interface='', key='', log_file=None, os_beta_command=False, os_compute_api_version='', os_identity_api_version='', os_image_api_version='', os_network_api_version='', os_object_api_version='', os_project_id=None, os_project_name=None, os_volume_api_version='', password=***'TFG4st@ck', project_domain_id='', project_domain_name='', project_id='', project_name='', region_name='', timing=False, token='***', trust_id='', url='', user_domain_id='', user_domain_name='', user_id='', username=u'escobarj', verbose_level=3, verify=None)
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'compute_api_version': u'2', u'orchestration_api_version': u'1', u'database_api_version': u'1.0', u'metering_api_version': u'2', 'auth_url': u'https://keystone.ifca.es:5000/', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], u'image_api_version': u'2', 'verify': True, u'dns_api_version': u'2', u'object_store_api_version': u'1', u'status': u'active', u'container_infra_api_version': u'1', 'verbose_level': 3, 'region_name': '', 'api_timeout': None, u'baremetal_api_version': u'1', 'auth': {}, 'default_domain': 'default', u'container_api_version': u'1', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, 'timing': False, 'password': u'***', u'application_catalog_api_version': u'1', 'cacert': None, u'key_manager_api_version': u'v1', 'deferred_help': False, u'identity_api_version': u'2.0', u'volume_api_version': u'2', 'username': u'escobarj', 'cert': None, u'secgroup_source': u'neutron', 'debug': True, u'interface': None, u'disable_vendor_agent': {}}
defaults: {u'auth_type': 'password', u'status': u'active', u'compute_api_version': u'2', 'key': None, u'database_api_version': u'1.0', 'api_timeout': None, u'baremetal_api_version': u'1', u'image_api_version': u'2', u'container_infra_api_version': u'1', u'metering_api_version': u'2', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', u'orchestration_api_version': u'1', 'cacert': None, u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', u'application_catalog_api_version': u'1', u'key_manager_api_version': u'v1', 'verify': True, u'identity_api_version': u'2.0', u'volume_api_version': u'2', 'cert': None, u'secgroup_source': u'neutron', u'container_api_version': u'1', u'dns_api_version': u'2', u'object_store_api_version': u'1', u'interface': None, u'disable_vendor_agent': {}}
cloud cfg: {'auth_type': 'password', 'beta_command': False, u'compute_api_version': u'2', u'orchestration_api_version': u'1', u'database_api_version': u'1.0', u'metering_api_version': u'2', 'auth_url': u'https://keystone.ifca.es:5000/', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], u'image_api_version': u'2', 'verify': True, u'dns_api_version': u'2', u'object_store_api_version': u'1', u'status': u'active', u'container_infra_api_version': u'1', 'verbose_level': 3, 'region_name': '', 'api_timeout': None, u'baremetal_api_version': u'1', 'auth': {}, 'default_domain': 'default', u'container_api_version': u'1', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, 'timing': False, 'password': u'***', u'application_catalog_api_version': u'1', 'cacert': None, u'key_manager_api_version': u'v1', 'deferred_help': False, u'identity_api_version': u'2.0', u'volume_api_version': u'2', 'username': u'escobarj', 'cert': None, u'secgroup_source': u'neutron', 'debug': True, u'interface': None, u'disable_vendor_agent': {}}
compute API version 2, cmd group openstack.compute.v2
network API version 2, cmd group openstack.network.v2
image API version 2, cmd group openstack.image.v2
volume API version 2, cmd group openstack.volume.v2
identity API version 2.0, cmd group openstack.identity.v2
object_store API version 1, cmd group openstack.object_store.v1
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'compute_api_version': u'2', u'orchestration_api_version': u'1', u'database_api_version': u'1.0', u'metering_api_version': u'2', 'auth_url': u'https://keystone.ifca.es:5000/', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], u'image_api_version': u'2', 'verify': True, u'dns_api_version': u'2', u'object_store_api_version': u'1', u'status': u'active', u'container_infra_api_version': u'1', 'verbose_level': 3, 'region_name': '', 'api_timeout': None, u'baremetal_api_version': u'1', 'auth': {}, 'default_domain': 'default', u'container_api_version': u'1', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, 'timing': False, 'password': u'***', u'application_catalog_api_version': u'1', 'cacert': None, u'key_manager_api_version': u'v1', 'deferred_help': False, u'identity_api_version': u'2.0', u'volume_api_version': u'2', 'username': u'escobarj', 'cert': None, u'secgroup_source': u'neutron', 'debug': True, u'interface': None, u'disable_vendor_agent': {}}
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'compute_api_version': u'2', u'orchestration_api_version': u'1', u'database_api_version': u'1.0', u'metering_api_version': u'2', 'auth_url': u'https://keystone.ifca.es:5000/', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], u'image_api_version': u'2', 'verify': True, u'dns_api_version': u'2', u'object_store_api_version': u'1', u'status': u'active', u'container_infra_api_version': u'1', 'verbose_level': 3, 'region_name': '', 'api_timeout': None, u'baremetal_api_version': u'1', 'auth': {}, 'default_domain': 'default', u'container_api_version': u'1', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, 'timing': False, 'password': u'***', u'application_catalog_api_version': u'1', 'cacert': None, u'key_manager_api_version': u'v1', 'deferred_help': False, u'identity_api_version': u'2.0', u'volume_api_version': u'2', 'username': u'escobarj', 'cert': None, u'secgroup_source': u'neutron', 'debug': True, u'interface': None, u'disable_vendor_agent': {}}
command: token issue -> openstackclient.identity.v2_0.token.IssueToken
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'compute_api_version': u'2', u'orchestration_api_version': u'1', u'database_api_version': u'1.0', u'metering_api_version': u'2', 'auth_url': u'https://keystone.ifca.es:5000/', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], u'image_api_version': u'2', 'verify': True, u'dns_api_version': u'2', u'object_store_api_version': u'1', u'status': u'active', u'container_infra_api_version': u'1', 'verbose_level': 3, 'region_name': '', 'api_timeout': None, u'baremetal_api_version': u'1', 'auth': {}, 'default_domain': 'default', u'container_api_version': u'1', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, 'timing': False, 'password': u'***', u'application_catalog_api_version': u'1', 'cacert': None, u'key_manager_api_version': u'v1', 'deferred_help': False, u'identity_api_version': u'2.0', u'volume_api_version': u'2', 'username': u'escobarj', 'cert': None, u'secgroup_source': u'neutron', 'debug': True, u'interface': None, u'disable_vendor_agent': {}}
Using auth plugin: password
Using parameters {'username': u'escobarj', 'password': u'***', 'auth_url': u'https://keystone.ifca.es:5000/'}
Get auth_ref
REQ: curl -g -i -X GET https://keystone.ifca.es:5000/ -H "Accept: application/json" -H "User-Agent: osc-lib/1.3.0 keystoneauth1/2.18.1 python-requests/2.12.5 CPython/2.7.12"
Starting new HTTPS connection (1): keystone.ifca.es
https://keystone.ifca.es:5000 "GET / HTTP/1.1" 300 603
RESP: [300] Date: Tue, 11 Apr 2017 17:53:54 GMT Server: Apache/2.4.18 (Ubuntu) Vary: X-Auth-Token X-Distribution: Ubuntu Content-Length: 603 Keep-Alive: timeout=5, max=100 Connection: Keep-Alive Content-Type: application/json
RESP BODY: {"versions": {"values": [{"status": "stable", "updated": "2016-04-04T00:00:00Z", "media-types": [{"base": "application/json", "type": "application/vnd.openstack.identity-v3+json"}], "id": "v3.6", "links": [{"href": "https://keystone.ifca.es:5000/v3/", "rel": "self"}]}, {"status": "stable", "updated": "2014-04-17T00:00:00Z", "media-types": [{"base": "application/json", "type": "application/vnd.openstack.identity-v2.0+json"}], "id": "v2.0", "links": [{"href": "https://keystone.ifca.es:5000/v2.0/", "rel": "self"}, {"href": "http://docs.openstack.org/", "type": "text/html", "rel": "describedby"}]}]}}

Making authentication request to https://keystone.ifca.es:5000/v2.0/tokens
https://keystone.ifca.es:5000 "POST /v2.0/tokens HTTP/1.1" 200 507
run(Namespace(columns=[], formatter='table', max_width=0, noindent=False, prefix='', print_empty=False, variables=[]))
+---------+---------------------------------------------------------------------------------------------------+
| Field   | Value                                                                                             |
+---------+---------------------------------------------------------------------------------------------------+
| expires | 2017-04-11T18:53:54+0000                                                                          |
| id      | gAAAAABY7RgyVfoQ1cK0qPoLeo2fG24MWpmsvL-R9jgzBc9Q_WX6Q-qrJiSvIM9-bHoI2IewssI4MhPUJVSK_Oyp-         |
|         | aYpB1RDbBA6__OPlOs91dOXX3TqQxZjIlJL-1IYaWraWytQUCXyBhQt77E0-ZNIOw2d_TmBmw                         |
| user_id | 8ee94e6e92d34167ad3d485dd4b52366                                                                  |
+---------+---------------------------------------------------------------------------------------------------+
clean_up IssueToken:
END return value: 0
