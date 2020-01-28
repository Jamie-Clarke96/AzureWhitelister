import json

with open('ipsets.json') as f:
    d = json.load(f)

azureService = "AzureSQL"
region = "northeurope"

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
    rule = rulename + str(j) + "{" + "\n" + "startIpAddress = " + "\"" + ip + "\""  + "\n" + "endIpAddress = " + "\"" + ip + "\""  + "\n" +  "}" + "\n"
    print(rule)
    j = j+1

print(ruleset)


