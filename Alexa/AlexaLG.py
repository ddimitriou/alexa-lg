"""AlexaLG.py

<https://github.com/ddimitriou/alexa-lg>.
"""
import sys

from fauxmo import fauxmo
from LGTV.___init___ import LGTVScan, LGTVClient
from ws4py.exc import HandshakeError
from time import sleep


class AlexaLG:

    def __init__(self, setup=False):
        if setup:
            scan_results = LGTVScan(first_only=True)
            if len(scan_results) == 0:
                raise Exception('Cannot find LGTV')
            self.client = LGTVClient(scan_results['address'])
            self.client.connect()
            sleep(15)
        else:
            self.client = LGTVClient()

    def on(self):
        self.client.on()
        return 'on'

    def off(self):
        self.client.connect()
        self.client.exec_command('off', {})
        sleep(5)
        self.client.run_forever()
        return 'off'

    def status(self):
        try:
            self.client.connect()
        except HandshakeError as e:
            return 'off'

        return 'on'

    def open_netflix(self):
        self.client.connect()
        self.client.exec_command('startApp', {'appid': 'netflix'})
        sleep(5)
        self.client.run_forever()

    def close_netflix(self):
        self.client.connect()
        self.client.exec_command('closeApp', {'appid': 'netflix'})
        sleep(5)
        self.client.run_forever()

    def channel_up(self):
        self.client.connect()
        self.client.exec_command('inputChannelUp', {})
        sleep(5)
        self.client.run_forever()

    def channel_down(self):
        self.client.connect()
        self.client.exec_command('inputChannelDown', {})
        sleep(5)
        self.client.run_forever()



if __name__ == '__main__':
    if len(sys.argv) > 1:
        # means we want to setup
        alexa = AlexaLG(True)
    fauxmo.main('./Alexa/config.json')
