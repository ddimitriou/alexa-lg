import logging
import logging.handlers

__author__ = 'Dimitri Dimitriou'
__email__ = 'dimitriou.d.a@gmail.com'
__version__ = 'v0.0.1'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)s:%(lineno)-8d %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("alexalg")
syslog_handler = logging.handlers.SysLogHandler()
logger.addHandler(syslog_handler)
