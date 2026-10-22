import json
import pprint

import requests

p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://api.coingecko.com/api/v3/search/trending')

result = requests.get('https://status.cryptoapis.io')

data = json.loads(result.text)

p.pprint(data)


