import json
from netaddr import *
import pprint

with open('ipsets.json') as f:
    d = json.load(f)

azureService = "AzureSQL"
region = "westeurope"

ipsets = d['values']
i = 0
ips = ""
for x in ipsets:
    if((x['properties']['region']) == region and ((x['properties']['systemService']) == azureService)):
         ips = x['properties']['addressPrefixes']

# Create a terraform rule for each IP
ruleset = []
rulename = region + "azuresqlip"
j = 1
for ip in ips:
    iprange = IPNetwork(ip)
    ipfirst = iprange[0]
    iplast = iprange[-1]

    rule = "\t" + rulename + str(j) + " = " "{" + "\n" + "\t" + "\t" + "startIpAddress = " + "\"" + str(ipfirst) + "\""  + "\n" + "\t" + "\t" + "endIpAddress = " + "\"" + str(iplast) + "\""  + "\n" +  "}" + "\n"
    print(rule)
    j = j+1



print(ruleset)


