import requests
target_url = 'https://maker.ifttt.com/trigger/Push7_IFTTT/with/key/esNZA0_q9698h1gw9QaAY6PF0mES-A10n9J-pzquQFa'
r = requests.get(target_url)
print(r)
