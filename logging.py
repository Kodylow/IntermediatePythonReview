# Logging
import logging

# only warning, error, critical are printed by default, need to specify config if you want to see debug and info levels
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')


## Different Levels of Logging
logging.debug('This is a debug message.')
logging.info('Info msg')
logging.warning('Warning msg')
logging.error('Error msg')
logging.critical('Critical msg')

# default logger is root, should use your own logger
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info("hello from helper")


# Log Handlers
# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')


# Or you can set up and import your own logging.conf
import logging.conf
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('debug message')

# can use dictConfig instead, this one looks a lot better


# Capturing Stack Traces
import traceback

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
except:
    logging.error("the error is %s", traceback.format_exc())

    
# Rotating File Handler
from logging.handlers import RotatingFileHandler

#roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(100000):
    logger.info('Hello, world!')

# Can do the same thing with TimedRotatingFileHandler that rotates on time
from logging.handlers import TimedRotatingFileHandler

# s, m, h, d, midnight, w0
timed_handler = TimedRotatingFileHandler('timed_test.log', when='s', interval='5', backupCount=5)
logger.addHandler

# if you've got a microservices architecture use the json format for logging
# pip install python-json-logger