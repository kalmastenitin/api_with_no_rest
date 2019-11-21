import json
from django.core.serializers import serialize
from django.http import HttpResponse

class HttpResponseMixin(object):
    def render_me(self,data,status=200):
        return HttpResponse(data,content_type='application/json',status=status)


class SerializeMixin(object):
    def serialize_me(self,qs):
        json_data = serialize('json',qs)
        pdict = json.loads(json_data)
        final_list = []
        for obj in pdict:
            final_list.append(obj['fields'])
        json_data = json.dumps(final_list)
        return json_data
