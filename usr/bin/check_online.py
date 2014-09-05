import urllib2
import sys

try:
    # Test the accessibility of Internet by visiting baidu.com
    ret = urllib2.urlopen('http://baidu.com').read()
    if not 'http://www.baidu.com/' in ret:
        sys.exit(1)
except:
    sys.exit(1)

sys.exit(0)
    