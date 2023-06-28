class Pixels:

    def __init__(self, npx, *args):
        self._inner_list = args
        self.npx = npx

    def __len__(self):
        return len(self._inner_list)

    def __getitem__(self, idx):
        return self._inner_list[idx]

    def __iter__(self):
        return self._inner_list.__iter__()

    def __contains__(self, value):
        return self._inner_list.__contains__(value)

    def color(self, red, green, blue, white):
        for px in self._inner_list:
            px.color(red, green, blue, white)

    def target(self, red, green, blue, white, steps):
        for px in self._inner_list:
            px.target(red, green, blue, white, steps)

    def step(self):
        for px in self._inner_list:
            px.step()

    def write(self):
        self.npx.write()

