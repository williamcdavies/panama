from strategies.gpt import GPT


class Composer:
    def __init__(self, model="gpt", **kwargs):
        self.model       = model
        self._strategies = {
            "gpt": GPT()
        }
        self.strategy    = self._strategies.get(self.model)
        if self.strategy is None:
            raise ValueError(f"Unknown model: {self.model}")
    

    def read(self) -> str:
        return self.strategy.read()


    def write(self, message):
        self.strategy.write(message)