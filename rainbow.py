class Rainbow:

    def __init__(self, sign_pixels, name):
        self.npx = sign_pixels
        self.total = len(sign_pixels)
        self.idx = 0
        self.name = name

    def step(self, brightness):
        b_pct = brightness / 100.0
        for i in range(self.total):
            pixel_index = (i * 256 // self.total) + self.idx
            red, green, blue, white = self.wheel(pixel_index & 255, b_pct)
            self.npx[i].color(red, green, blue, white)
        if self.idx == 255:
            self.idx = 0
        else:
            self.idx = self.idx + 1

        self.npx.write()

    def name(self):
        return self.name

    def reset(self):
        self.idx = 0

    def wheel(self, pos, b_pct):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3 * b_pct)
            g = int((255 - pos * 3) * b_pct)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int((255 - pos * 3) * b_pct)
            g = 0
            b = int(pos * 3 * b_pct)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3 * b_pct)
            b = int((255 - pos * 3) * b_pct)
        return r, g, b, 0

