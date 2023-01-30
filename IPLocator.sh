#!/bin/bash
if [ $# -eq 0 ];
then
  echo "$0: Missing Ip"
  exit 1
else
curl -s 'https://ipxapi.com/api/ip?ip='$1 -X GET  -H 'Accept: application/json' -H 'Authorization: Bearer 5456|KjWA7Pp9uCio0vuxJZnT9gR5raJCwqeoMvIK7Jq6' -o Data/#1#$1.txt

echo " "
echo "--------------------------------------"
echo "| Data/#1#$1.txt Created! |"
echo "--------------------------------------"
echo " "

curl -s http://ip-api.com/json/$1?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query -o Data/#2#$1.txt

echo " "
echo "--------------------------------------"
echo "| Data/#2#$1.txt Created! |"
echo "--------------------------------------"
echo " "
fi
