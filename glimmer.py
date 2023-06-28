import time
from colorsys import hls_to_rgb, rgb_to_hls
from random import randrange



class Glimmer:

    total_steps = 20

    def __init__(self, sign_pixels, red, green, blue, name):
        self.npx = sign_pixels
        self.total = len(sign_pixels)
        self.idx = 0
        (self.hue, self.lightness, self.saturation) = rgb_to_hls(red / 255, green / 255, blue / 255)
        self.name = name
        self.b_pct = 1

    def set_targets(self):
        # Pick a destination white index
        print(self.b_pct)
        for i in range(self.total):
            delta = (randrange(-20, 20) / 100)
            (r, g, b) = hls_to_rgb(self.hue, self.lightness + delta, self.saturation)
            self.npx[i].target(int(r * 255 * self.b_pct), int(g * 255 * self.b_pct), int(b * 255 * self.b_pct), 0, self.total_steps)

    def step(self, brightness):
        self.b_pct = brightness / 100.0
        if self.idx == 0:
            self.set_targets()

        self.npx.step()

        if self.idx == self.total_steps:
            self.idx = 0
        else:
            self.idx = self.idx + 1

        self.npx.write()

    def name(self):
        return self.name

    def reset(self):
        self.idx = 0
