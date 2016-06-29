import sys
import xmlrpclib
from pprint import pprint

name, url = sys.argv[1:]
print('%s -> %s' % (name, url))

s = xmlrpclib.ServerProxy("http://localhost:6800/rpc")
r = s.aria2.addUri([url], {"dir":".", "out": name})
pprint(r)
