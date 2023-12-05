import requests

ip_address = input("Enter an IP address: ")
url = f"http://ip-api.com/json/{ip_address}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"== IP Information ==")
    print(f"IP Address: {data['query']}")
    print(f"Continent: {data['continent']} ({data['continentCode']})")
    print(f"Country: {data['country']} ({data['countryCode']})")
    print(f"Region: {data['regionName']} ({data['region']})")
    print(f"City: {data['city']}")
    print(f"Zip Code: {data['zip']}")
    print(f"Latitude: {data['lat']}")
    print(f"Longitude: {data['lon']}")
    print(f"Timezone: {data['timezone']}")
    print(f"Currency: {data['currency']}")
    print(f"ISP: {data['isp']}")
    print(f"Organization: {data['org']}")
    print(f"AS Number: {data['as']}")
    print(f"AS Name: {data['asname']}")
    print(f"Reverse DNS: {data['reverse']}")
    print(f"Mobile: {data['mobile']}")
    print(f"Proxy: {data['proxy']}")
    print(f"Hosting: {data['hosting']}")
else:
    print("Failed to retrieve IP information.")
