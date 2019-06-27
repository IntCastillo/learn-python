# No funciona por exceder el límite de requests de el API

import geocoder

g = geocoder.ip('me')

print(g.latlng)