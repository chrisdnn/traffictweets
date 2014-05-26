from TwitterAPI import TwitterAPI
import json

consumer_key = '6a8eiydF31fyJrJ3vJFtmpHV9'
consumer_secret = '8tyZ34jIk2AM3WxN18JimbRC58FRyzTUSX83l7lC7Tz54rrO2H'
access_token_key = '80065688-IMt9thIgmN0CM7oNK0tUGAVoC6Nkdr01XNWhl3Eu1'
access_token_secret = 'xUjSwaK5PGAVRhFJj37U1OqJ44iISWqXAwrJOsIRaayKP'
SEARCH_TERM = ''

#api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret, auth_type='oAuth2')
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

## Tweets from San Pedro Garza Garcia
#r = api.request('search/tweets', {'q':SEARCH_TERM, 'geocode':'25.66173253,-100.35253104,5km','count':'450','until':'2015-05-21'})
## with access Token
r = api.request('statuses/filter', {'locations':'-100.598350, 25.547178, -100.036674, 25.856532'})

#icount = 0
for item in r:
        #print(json.dumps(item, indent=4, separators=(',',': ')))
        #print('text: ' % item['text'])
        print(item['text'] if 'text' in item else item)
        #icount += 1

#print("count: %d" % icount)
#print('\nQUOTA: %s' % r.get_rest_quota())
