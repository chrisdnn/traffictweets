from TwitterAPI import TwitterAPI
import json

consumer_key = '6a8eiydF31fyJrJ3vJFtmpHV9'
consumer_secret = '8tyZ34jIk2AM3WxN18JimbRC58FRyzTUSX83l7lC7Tz54rrO2H'
access_token_key = ''
access_token_secret = ''
SEARCH_TERM = 'friday'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret, auth_type='oAuth2')

r = api.request('geo/search', {'geocode':'29.437188, -98.500672'})
#r = api.request('statuses/filter', {'locations':'-122.75,36.8,-121.75,37.8'})
#r = api.request('search/tweets', {'q':SEARCH_TERM, 'geocode':'37.781157,-122.398720,1mi'})
#r = api.request('search/tweets', {'q':SEARCH_TERM, 'geocode':'29.437188, -98.500672,25mi'})

#r = api.request('search/tweets', {'q':SEARCH_TERM, 'geocode':'19.433455, -99.146691,15665mi'})
#r = api.request('search/tweets', {'q': SEARCH_TERM})
#for item in r.get_iterator():
for item in r:
        print(json.dumps(item, indent=4, separators=(',',': ')))
    #print('full_name: ' % item['full_name'] % ' place_type: ' % item['place_type'])
#    j = item.json()
#    print(j['resources']['search'])
#    print(item.text)

print('\nQUOTA: %s' % r.get_rest_quota())
