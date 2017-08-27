"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort regions by the average latency.
http://ec2-reachability.amazonaws.com/
Sample output:
1. us-west-1 [50.18.56.1] - Smallest average latency
2. xx-xxxx-x [xx.xx.xx.xx] - x
3. xx-xxxx-x [xx.xx.xx.xx] - x
...
15. xx-xxxx-x [xx.xx.xx.xx] - Largest average latency
"""

import subprocess


regions = {
            "us-east-1": "50.19.255.254",#59
            "us-west-1": "52.8.191.254",#80
            "eu-west-1": "52.30.63.252",#60
            "us-west-2": "52.10.63.252",#20
            "eu-central-1": "35.156.63.252",
            "eu-west-2": "35.176.0.252",
            "us-gov-west-1": "96.127.32.126",
            "ca-central-1": "35.182.0.251",
            "us-east-2": "18.220.0.252",
            "ap-northeast-1": "54.199.127.255",
            "ap-northeast-2": "13.124.63.251",
            "ap-southeast-1": "13.228.0.251",
            "ap-southeast-2": "52.62.63.252",
            "ap-south-1": "13.126.0.252",
            "sa-east-1": "54.207.127.254"
        }




#given a host get me the average latency
def getAverageLatency(host):
    ping = subprocess.Popen(
        ["ping", "-c", "3", host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    out, error = ping.communicate()
    #print(out)
    #print("\n")

    if not error or error == '':
        # if output is valid, then parse to get times from it
        # print("Successfully pinged: ", host)
        return parseAndCalculateAverageLatency(out)
    else:
        return -1


    return ""


def parseAndCalculateAverageLatency(response):
    lines = response.decode("utf-8").split("\n")
    total_time = 0.0
    total_num_pings = 0

    for line in lines:
        if "time=" in line:
            time_lines = line.split("time=")
            time = time_lines[1].replace(" ms", "")
            total_time += float(time)
            total_num_pings += 1

    if total_num_pings > 0:
        return total_time / total_num_pings
    else:
        return -1


def printLatencies(regions):
    list = []

    for key,value in regions.items():
        avgLatency = getAverageLatency(value)
        tuple = (key, avgLatency)
        list.append(tuple)

    list2 = sorted(list, key=lambda tup: tup[1])

    for tuple in list2:
        region = tuple[0]
        latency = tuple[1]
        ipAddr = regions[region]

        print(region + " [" + ipAddr + "] - " + "{:.5f}".format(latency) )


printLatencies(regions)
