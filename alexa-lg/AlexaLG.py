"""alexa_lg.py

<https://github.com/ddimitriou/alexa-lg>.
"""

from fauxmo.protocols import SSDPServer, Fauxmo
from fauxmo.utils import get_local_ip, module_from_file, make_udp_sock
from LGTV.___init___ import LGTVScan

class alexa_lg:

    def __init__(self, ):
        self.lg_scan = LGTVScan

    def run(self):
        self.lg_scan(first_only=True)
