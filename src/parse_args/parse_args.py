class ParseArgs:
    def __init__(self, args):
        self.args = args
        self.options = {}
        self.positional_args = []
        self.parse_args()

    def parse_args(self):
        for arg in self.args:
            if arg.startswith("--"):
                key = arg[2:]
                if "=" in key:
                    key, value = key.split("=")
                    self.options[key] = value
                else:
                    self.options[key] = True
            elif arg.startswith("-"):
                for char in arg[1:]:
                    self.options[char] = True
            else:
                self.positional_args.append(arg)