import urllib3

http = urllib3.PoolManager()
url = "https://busquedas.gruporeforma.com/reforma/BusquedasComs.aspx"
r = http.request('GET', url)
print(r.data)

