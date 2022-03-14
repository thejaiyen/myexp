import re

# statement = 'Please contact us at: support@datacamp.com'
# match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
# if statement:
#   print("Email address:", match.group()) # The whole matched text
#   print("Username:", match.group(1)) # The username (group 1)
#   print("Host:", match.group(2)) # The host (group 2)


# statement = 'Please contact us at: support@datacamp.com'
# match = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)
# if statement:
#   print("Email address:", match.group('email'))
#   print("Username:", match.group('username'))
#   print("Host:", match.group('host'))


statement = '''
10.88.111.111 - - [11/May/2021:08:54:13 +0000] "GET / HTTP/2.0" 400 471 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
10.88.111.111 - - [11/May/2021:08:54:13 +0000] "GET /favicon.ico HTTP/2.0" 400 482 "https://registry.demo.opsta.in.th/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
'''
# statement = 'ssdasd'

pattern = r'(?P<ip>\d+.\d+.\d+.\d+)\s*-\s*(?P<user>\S*)\s*\[(?P<timestamp>\S*.\W\d*)\]\s*\"(?P<method>\S*)\s*(?P<path>\S*)\s*(?P<http_version>\w*/\d+\.\d+)\"\s*(?P<return_code>\d*)\s*(?P<body_byte>\d*)\s*(?P<http_referer>\S*)\s(?P<http_user_agent>\".*\")'
match = re.search(pattern, statement)
if match != None:
    print(match.group())
    # print(match.group("host"))




