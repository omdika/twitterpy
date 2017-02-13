#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'vvJf125eKdfqC8oMV17p2ziPa'
CONSUMER_SECRET = 'uU7EMJzkfoSZROW1d3JqWa1rltvmnZbDnTBjj0GC24kHNCkzrp'
ACCESS_KEY = '811398503167508480-TsCTlFiv5gB3QwAfDtGcyYxPCawx9np'
ACCESS_SECRET = 'hNWhZ45Vr09rHnhId9pZqfZJS9RFh8nSba48Ruq7Dedgj'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
