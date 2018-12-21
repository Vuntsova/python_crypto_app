import json
import requests
from datetime import datetime

global_url = 'https://api.coinmarketcap.com/v2/global/'
request = requests.get(global_url)
results = request.json()
#print('Hey')
#print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes']['USD']['total_market_cap'])
global_volume = int(results['data']['quotes']['USD']['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

last_updated_str = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print('there are currently '+ active_currencies_string + ' active cryptocurrencies and ' + active_markets_string + ' active markets')
print('The global cap of all crypto is ' + global_cap_string + ' and the 24th global volume us ' + global_volume_string)
print('Bitcoin\'s total percentige of the global cao is ' + str(bitcoin_percentage) + '%.')
print()
print('Last Updated on: ' + str(last_updated_str))
