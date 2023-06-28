class Pixel:

    def __init__(self, npx, idx):
        self.idx = idx
        self.current = [0, 0, 0, 0]
        self.steps = [0, 0, 0, 0]
        self.npx = npx

    def color(self, red, green, blue, white):
        self.current = [red, green, blue, white]
        self.npx[self.idx] = (red, green, blue, white)

    def target(self, red, green, blue, white, steps):
        red_steps = -((self.current[0] - red) / steps)
        green_steps = -((self.current[1] - green) / steps)
        blue_steps = -((self.current[2] - blue) / steps)
        white_steps = -((self.current[3] - white) / steps)

        self.steps = [red_steps, green_steps, blue_steps, white_steps]

    def step(self):
        red_next = min(255, max(0, int(self.current[0] + self.steps[0])))
        green_next = min(255, max(0, int(self.current[1] + self.steps[1])))
        blue_next = min(255, max(0, int(self.current[2] + self.steps[2])))
        white_next = min(255, max(0, int(self.current[3] + self.steps[3])))

        self.color(red_next, green_next, blue_next, white_next)

    def write(self):
        self.npx.write()


