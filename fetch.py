import requests
import sys
from urllib.parse import urlencode

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = sys.argv[1] 
#'https://disk.yandex.ru/i/vrPoXir2hVCBNw' 

final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']

download_response = requests.get(download_url)
with open(sys.argv[2], 'wb') as f:
    f.write(download_response.content)
