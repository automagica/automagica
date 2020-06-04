import json


class Keybind:
    def __init__(self, name=None, key_combination=[], flow_file_path=None):
        self.name = name
        self.key_combination = key_combination
        self.flow_file_path = flow_file_path

    @property
    def key_combination_label(self):
        return "+".join(self.key_combination)

    def activate(self):
        # from automagica.flow import Flow
        # flow = Flow(self.flow_file_path)
        # flow.run()
        print(self.flow_file_path)
        pass


class KeybindsManager:
    def __init__(self, file_path=None, keybinds=[]):
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)
                keybinds = [Keybind(**val) for _, val in data.items()]

        self.keybinds = keybinds
