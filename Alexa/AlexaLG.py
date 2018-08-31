"""AlexaLG.py

<https://github.com/ddimitriou/alexa-lg>.
"""

from fauxmo.protocols import SSDPServer, Fauxmo
from fauxmo.utils import get_local_ip, module_from_file, make_udp_sock

from LGTV.___init___ import LGTVScan, LGTVClient
from Alexa import alexalg


class AlexaLG:

    tv = {}
    def __init__(self):
        self.lg_scan = LGTVScan

    def run(self):
        server = SSDPServer()
        server.add_device(self.tv['name'], self.tv['ip_address'])

    def scan(self):
        scan_results = self.lg_scan(first_only=True)
        if len(scan_results) == 0:
            raise Exception('Cannot find LGTV')
        alexalg.info(scan_results)
        self.tv = {
            'name': scan_results.model,
            'ip_address': get_local_ip()
        }


if __name__ == '__main__':
    alexa = AlexaLG()
    alexa.scan()
    alexa.run()
