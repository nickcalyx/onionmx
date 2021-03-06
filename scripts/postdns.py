#!/usr/bin/env python

import dns.resolver
import re
import sys

myresolver = dns.resolver.Resolver()

name = raw_input("")
if name == 'get *':
    print("200 :")
    sys.exit(0)
try:
    domain=name.split("@")[1]
except:
    print("200 :")
    sys.exit(0)

#VARIABLES
myresolver.nameservers = ['127.0.0.1']
myresolver.port = 53
srv_lookup='_onion-mx._tcp.'
onion_transport='smtptor'
myself='MYDOMAIN\.net'

# magic
record=srv_lookup+domain

if not re.search(myself,record):
  try:
      answers=myresolver.query(record, 'SRV', tcp=True)
      for rdata in answers:
          if re.search('onion\.$',str(rdata.target)):
              print "200 %s:[%s]" % (onion_transport,str(rdata.target).rstrip('.'))
          else:
              print("200 smtp:")
  except:
      print("200 smtp:")
else:
    print("200 :")
    sys.exit(0)
