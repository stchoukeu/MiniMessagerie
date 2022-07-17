import requests

# affichage du numero cvs du site
r = requests.get('http://www.example.com')
print(r.status_code)

# le résultat attendu est "200"