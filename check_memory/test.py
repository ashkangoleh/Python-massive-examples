from guppy import hpy
hp = hpy()
# before = hp.heap()
hp.heap()
print('hp.heap(): ', hp.heap())
from time import time
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,MetaData,Table
from decouple import config
import json
from sqlalchemy.sql import text

DB_USER = 'bc_admin'
DB_PASSWORD = '7aff4f6e979711ec884a17a5405387ef'
DB_ADDRESS = 'venus.arz.team'
DB_NAME = 'blockchair'
DB_PORT = 5532
# import resource
# print('Memory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

# after = hp.heap()
# leftover = after - before
# import pdb; pdb.set_trace()
import re, sys

print(map(sys.stdout.write,(l for l in sys.stdin if re.search(sys.argv[1],l))))