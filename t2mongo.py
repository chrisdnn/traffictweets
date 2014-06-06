from TwitterAPI import TwitterAPI
import json
import pymongo
import m_tweetsDAO

consumer_key = '6a8eiydF31fyJrJ3vJFtmpHV9'
consumer_secret = '8tyZ34jIk2AM3WxN18JimbRC58FRyzTUSX83l7lC7Tz54rrO2H'
access_token_key = '80065688-IMt9thIgmN0CM7oNK0tUGAVoC6Nkdr01XNWhl3Eu1'
access_token_secret = 'xUjSwaK5PGAVRhFJj37U1OqJ44iISWqXAwrJOsIRaayKP'
SEARCH_TERM = ''

#sys.stdout.encoding='utf-8'

#api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret, auth_type='oAuth2')
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

## Tweets from San Pedro Garza Garcia
#r = api.request('search/tweets', {'q':SEARCH_TERM, 'geocode':'25.66173253,-100.35253104,5km','count':'450','until':'2015-05-21'})
## with access Token
r = api.request('statuses/filter', {'track':'mty,monterrey,sanpedro,spdp,garzagarcia,calzada del valle,margain,av vasconselos','locations':'-100.598350, 25.547178, -100.036674, 25.856532'})
#r = api.request('statuses/filter',{'track':'mty, monterrey, sanpedro, spdp, garzagarcia, calzada del valle, margain, av vasconselos, cicmty , implansp , somosbicibles , ciac_mty, alertamty_com, regioseguro, choque, alcance, chocar, chocaron, accidente, vial, peatonal, peligro, peligroso, tráfico, trafico, calzada, gomez morin, gómez morín, gómez morin, gomez morín, alfonso reyes, tránsito, transito, robo, robaron, semáforo, semaforo', 'locations':'-100.598350, 25.547178, -100.036674, 25.856532'})

#first, setup mongodb connection
connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)	
dbs = connection.dbtweets
tweetsDAO = m_tweetsDAO.M_tweetsDAO(dbs)

for item in r:
        #print(item['text'].encode('cp1252','ignore').decode('cp1252','ignore') if 'text' in item else item)
        tweetsDAO.insert_tweet(item)
        #print(item)
        #icount += 1

#a_file = open('sampletweet.txt', encoding='utf-8')
#a_string = "'" + a_file.read() + "'"
#a_string = a_file.read()
#print('file read\n' + a_string)
#json_var = json.dumps(a_string)
#json_var3 = json.loads(a_string)
#print('json raw pretty printing:\n ' + json.dumps(json_var3, sort_keys=True, indent=4))
#print('get text: ' + json_var3["text"])
#print('json loads:\n' + json.loads(json_var))
#print('json a_string loads:\n' + json.loads(a_string))
#print('json a_string loads:\n' + json_var)
#print('json_var3:\n' + json_var3)
#print(json.dumps(json_var3, sort_keys=True))
#print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
#var4 = '{"4": 5, "6": 7}'
#json_var4 = json.loads(var4)
#print('print4:\n ' + json.dumps(json_var4, sort_keys=True, indent=4))
#var5 = {"created_at":"Tue Jun 03 01:15:35 +0000 2014","id":473634067120795648,"id_str":"473634067120795648","text":"I need life to slow the fuck down"}
#json_var5 = json.loads(var5)
#print('print5:\n ' + json.dumps(var5, sort_keys=True, indent=4))
#print(json.dumps({'name': 'chris', 'email':'cdunneg@gmail.com'}, sort_keys=True, indent=4))
#json_var2 = {'name': 'chris', 'email':'cdunneg@gmail.com'}
#print(json.dumps(json_var2, sort_keys=True, indent=4))
#tweetsDAO.insert_tweet(a_string)
#print("count: %d" % icount)
#print('\nQUOTA: %s' % r.get_rest_quota())
