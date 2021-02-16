import requests
import zipfile

print('Updating Oxide...')

url = 'https://umod.org/games/rust/download'
r = requests.get(url, allow_redirects=True)
open('oxide-update.zip', 'wb').write(r.content)

with zipfile.ZipFile('./oxide-update.zip', 'r') as zip_ref:
	zip_ref.extractall('.')
	
print('Oxide is now up to date!')