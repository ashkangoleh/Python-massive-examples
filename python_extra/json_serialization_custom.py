from collections.abc import MutableMapping
import json
import datetime


class JSONSerializer(json.JSONEncoder):
    def encode(self, obj):
        # Convert dictionary keys that are datatime.dates into strings.
        if isinstance(obj, MutableMapping):
            for key in list(obj.keys()):
                if isinstance(key, datetime.date):
                    # strkey = key.strftime('%Y-%m-%d')
                    strkey = key.strftime('%s')
                    obj[strkey] = obj.pop(key)

        return super().encode(obj)


test_dict = {datetime.date(2022, 7, 10): 'OK'}

print(json.dumps(test_dict, cls=JSONSerializer))  # -> {"2022-07-11": "OK"}

with open('dump.json', 'w') as w:
    json.dump(test_dict, w, cls=JSONSerializer)  