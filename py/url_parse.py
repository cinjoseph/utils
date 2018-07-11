import re

def parse_url(url):
    pattern  = r"(?P<proto>\w+)://((?P<user>\w+)?(:(?P<passwd>\S+))?@)?"
    pattern += r"(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-z0-9.-]+)(:(?P<port>\d{1,5}))?"
    pattern += r"(?P<path>[a-zA-Z0-9\-\/._~%!$&'()*+]+)?"
    pattern += r"(\?(?P<query>[a-zA-Z0-9&=%]+))?"
    reg = re.compile(pattern)
    match = reg.match(url)
    if match == None:
        return None
    result = match.groupdict()
    query = result['query']
    args = {}
    if query:
        for k, v in [query.split('=', 1) for query in query.split('&')]:
            args[k] = v
    else:
        args = {}
    result['args'] = args
    return result


if __name__ == '__main__':
    s = "https://user:secret@baidu.com/?arg1=val1&arg2=val2jk1jkajsdf=="
    result = parse_url(s)
    print "*******Test1*******"
    print s
    print result

    s = "https://:secret@baidu.com/?arg1=val1&arg2=val2jk1jkajsdf=="
    result = parse_url(s)
    print "*******Test2*******"
    print s
    print result

    s = "https://secret@baidu.com/?arg1=val1&arg2=val2jk1jkajsdf=="
    result = parse_url(s)
    print "*******Test3******* this is error test"
    print s
    print result



