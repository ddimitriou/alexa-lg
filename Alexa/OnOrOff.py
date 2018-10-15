from fauxmo.plugins import FauxmoPlugin
from Alexa.AlexaLG import AlexaLG


class OnOrOff(FauxmoPlugin):

    def __init__(self, name: str, port: int, on_cmd: str, off_cmd: str,
                 state_cmd: str = None) -> None:
        self.lg = AlexaLG()
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd
        self.state_cmd = state_cmd

        super().__init__(name=name, port=port)

    def run_cmd(self, cmd: str) -> bool:
        return getattr(self.lg, cmd)()

    def on(self) -> bool:
        return self.run_cmd(self.on_cmd)

    def off(self) -> bool:
        return self.run_cmd(self.off_cmd)

    def get_state(self) -> str:
        if self.state_cmd is None:
            return "unknown"

        returned_zero = self.run_cmd(self.state_cmd)
        if returned_zero is True:
            return "on"
        return "off"
