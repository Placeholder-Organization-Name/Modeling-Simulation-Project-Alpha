import sys
import requests
f = open(sys.argv[1])
url = 'https://ssd.jpl.nasa.gov/api/horizons_file.api'
r = requests.post(url, data={'format':'text'}, files={'input': f})
print(r.text)
f.close()
