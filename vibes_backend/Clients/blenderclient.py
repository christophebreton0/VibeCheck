from vibes_backend.SystemCore.baseclient import BaseClient


class BlenderCLient(BaseClient):

    def __init__(self):
        super().__init__(id_t="blender", name="BlenderClient")

    def main_loop(self) -> None:
        pass
