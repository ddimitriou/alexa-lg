
from fauxmo.plugins import FauxmoPlugin
from LGTV.___init___ import LGTVClient


class LGPlugin(FauxmoPlugin):

    def __init__(self):
        super().__init__()
        self.lg_tv_client = LGTVClient

    def off(self) -> bool:
        pass

    def on(self) -> bool:
        pass
