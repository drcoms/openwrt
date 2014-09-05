import json
import sys
import os

def arg2dict(args):
    ret = {}
    arg_list = args.split('&')
    for item in arg_list:
        foo = item.split('=')
        if len(foo) < 2: 
            foo.append(True)
        ret[foo[0]] = foo[1]
    return ret

def get_args():
    return arg2dict(os.getenv('QUERY_STRING'))

def printdata(data):
    context = 'Content-Type: application/json\n\n'
    context += json.dumps(data)
    return context
    
def check_login():
    data = {'result':'error','message':'Not login'}
    if os.path.exists('/etc/drcom.conf'):
    	exec(open('/etc/drcom.conf').read())
    else:    
        sys_pass = '123456'
    foo = get_args()
    if not foo.has_key('password'):
        print printdata(data)
        sys.exit(0)
    if foo['password'] != sys_pass:
        print printdata(data)
        sys.exit(0) 
