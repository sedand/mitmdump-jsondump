# Usage: mitmdump -s "jsondump.py out.json"
from libmproxy.models import decoded
import json


def start(context, argv):
    if len(argv) != 2:
        raise ValueError('Usage: -s "jsondump.py out.json"')
    context.outfile = open(argv[1],'a')

def response(context, flow):
    with decoded(flow.response):  # automatically decode gzipped responses.
	#print(flow.response.content)
	#print(dir(flow.request))
	#print(dir(flow.response.headers))

	json_data = {}
	json_request = {}
	json_response = {}

	json_request['host'] = flow.request.host
	json_request['port'] = flow.request.port
	json_request['url'] = flow.request.url

	json_response['content'] = unicode(flow.response.content, errors='ignore')
	json_response['headers'] = {}
	for item in flow.response.headers:
		json_response['headers'][item] = flow.response.headers[item]

	json_data['request'] = json_request
	json_data['response'] = json_response
	context.outfile.write(json.dumps(json_data)+'\n')
	context.outfile.flush()
