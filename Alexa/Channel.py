from fauxmo.plugins import FauxmoPlugin
from Alexa.AlexaLG import AlexaLG


class Channel(FauxmoPlugin):

    def __init__(self, name: str, port: int, on_cmd: str, off_cmd: str,
                 state_cmd: str = None) -> None:
        self.lg = AlexaLG()
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd
        self.state_cmd = state_cmd
        self.state = False
        super().__init__(name=name, port=port)

    def on(self) -> bool:
        self.lg.channel_up()
        self.state = True
        return True

    def off(self) -> bool:
        self.lg.channel_down()
        self.state = False
        return True

    def get_state(self) -> str:
        if self.state:
            return 'on'
        return 'off'
