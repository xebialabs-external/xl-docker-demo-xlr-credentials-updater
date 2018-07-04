# Create directories
import sys
import json
import base64
import urllib
import urllib.parse
import urllib.request
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

print("Updating credentials")

xlr_username="admin"
xlr_password="admin"
base64string = base64.encodestring(('%s:%s' % (xlr_username, xlr_password)).encode()).decode().replace('\n', '')

def get_configuration_object(server_title, server_type):
    url_encoded_title = urllib.quote_plus(server_title)
    url = "http://xlr:5516/api/v1/config/byTypeAndTitle?configurationType=%s&title=%s" % (server_type, url_encoded_title)
    request = urllib.request.Request(url) 
    request.add_header("Authorization", "Basic %s" % base64string)   
    result = urllib.request.urlopen(request)
    return json.loads(result.read())[0]

def save_configuration_object(config_object):
    headers = {'Content-Type': 'application/json'}
    request = urllib.request.Request("http://xlr:5516/api/v1/config/%s" % (config_object["id"]), json.dumps(config_object), headers)
    request.add_header("Authorization", "Basic %s" % base64string)   
    request.get_method = lambda: 'PUT'
    result2 = urllib.request.urlopen(request)

def update_ci(server_title, server_type, username, properties):
    print("Processing credential [%s] for server type [%s] with title [%s]" % (username, server_type, server_title))
    config_object = get_configuration_object(section, server_type)
    for item in properties:
        config_object[item[0]] = item[1]
    save_configuration_object(config_object)

cp = ConfigParser()
#To avoid parser to convert all keys to lowercase by default
cp.optionxform = str
cp.read(sys.argv[1])

for section in cp.sections():
    update_ci(section, cp.get(section, "type"), cp.get(section, "username"), cp.items(section))

print("Updated credentials")

