import re
import json

def str2json(income):
    #remove some  " " in last str
    income = re.sub(r' \"-\"+$', r'', income)
    #Regular Expression
    pattern = r'(?P<ip>\d+.\d+.\d+.\d+)\s*-\s*(?P<user>\S*)\s*\[(?P<timestamp>\S*.\W\d*)\]\s*\"(?P<method>\S*)\s*(?P<path>\S*)\s*(?P<http_version>\w*/\d+\.\d+)\"\s*(?P<return_code>\d*)\s*(?P<body_byte>\d*)\s*\"(?P<http_referer>\S*)\"\s\"(?P<http_user_agent>.*)\"'
    match = re.search(pattern, income)
    if match != None:
        x = {
            "timestamp": match.group("timestamp"),
            "ip": match.group("ip"),
            "method": match.group("method"),
            "path": match.group("path"),
            "http_version": match.group("http_version"),
            "return_code": int(match.group("return_code")),
            "body_byte": int(match.group("body_byte")),
            "http_referer": match.group("http_referer"),
            "http_user_agent": match.group("http_user_agent"),
            }
        return (x)
    return None

def main():
    workbook = open('./exam.log')
    data = workbook.readlines()
    workbook.close()
    dict1 = {}
    list1 = []
    for i in data:
        dataj = str2json(i)
        if dataj != None:
            list1.append(dataj)
    with open('./exam.json', 'w') as f:
        f.write(json.dumps({'data': list1}, indent=2))

if __name__ == "__main__":
    main()