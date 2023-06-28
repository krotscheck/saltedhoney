import machine
import neopixel

from const import idx_honey_start, idx_salted_start, num_pixels, num_pixels_honey, num_pixels_salted
from pixel import Pixel
from pixels import Pixels


class Sign:
    _npx = neopixel.NeoPixel(machine.Pin(28), num_pixels, bpp=4)

    def __init__(self):
        # First, create a list of all individual pixels. We'll use these instances to construct different collections later.
        self._pixels = [Pixel(self._npx, x) for x in range(num_pixels)]

        # Build the convenience collection of all the individual hexagons
        hex_ranges = [x for x in range(0, idx_honey_start)] + \
                     [x for x in range(idx_honey_start + num_pixels_honey, idx_salted_start)] + \
                     [x for x in range(idx_salted_start + num_pixels_salted, num_pixels)]

        # Build a list of hexagon pixel sets.
        self._hexagons = list()
        for x in range(0, len(hex_ranges), 4):
            hexagon = Pixels(self._npx, *[self._pixels[hex_ranges[x]] for x in range(x, x + 4)])
            self._hexagons.append(hexagon)

        # Build the letter pixels sets for salted
        s_range = [x for x in range(idx_salted_start, idx_salted_start + 10)]
        a_range = [x for x in range(idx_salted_start + 10, idx_salted_start + 10 + 4)] + \
                  [x for x in range(idx_salted_start + 40, idx_salted_start + 42)]
        l_range = [x for x in range(idx_salted_start + 14, idx_salted_start + 14 + 6)] + \
                  [x for x in range(idx_salted_start + 34, idx_salted_start + 40)]
        se_range = [x for x in range(idx_salted_start + 20, idx_salted_start + 22)] + \
                   [x for x in range(idx_salted_start + 30, idx_salted_start + 34)]
        d_range = [x for x in range(idx_salted_start + 22, idx_salted_start + 30)]

        s = Pixels(self._npx, *[self._pixels[x] for x in s_range])
        a = Pixels(self._npx, *[self._pixels[x] for x in a_range])
        l = Pixels(self._npx, *[self._pixels[x] for x in l_range])
        se = Pixels(self._npx, *[self._pixels[x] for x in se_range])
        d = Pixels(self._npx, *[self._pixels[x] for x in d_range])


        # Build the letter pixels sets for honey
        h_range = [x for x in range(idx_honey_start + 16, idx_honey_start + 24)]
        o_range = [x for x in range(idx_honey_start + 12, idx_honey_start + 16)] + \
                  [x for x in range(idx_honey_start + 24, idx_honey_start + 26)]
        n_range = [x for x in range(idx_honey_start + 8, idx_honey_start + 12)] + \
                  [x for x in range(idx_honey_start + 26, idx_honey_start + 30)]
        e_range = [x for x in range(idx_honey_start + 4, idx_honey_start + 8)] + \
                  [x for x in range(idx_honey_start + 30, idx_honey_start + 34)]
        y_range = [x for x in range(idx_honey_start, idx_honey_start + 4)] + \
                  [x for x in range(idx_honey_start + 34, idx_honey_start + 36)]

        h = Pixels(self._npx, *[self._pixels[x] for x in h_range])
        o = Pixels(self._npx, *[self._pixels[x] for x in o_range])
        n = Pixels(self._npx, *[self._pixels[x] for x in n_range])
        e = Pixels(self._npx, *[self._pixels[x] for x in e_range])
        y = Pixels(self._npx, *[self._pixels[x] for x in y_range])

        self._letters = [s, a, l, se, d, h, o, n, e, y]

        self._rows = [
            Pixels(self._npx, *[self._hexagons[x] for x in range(0, 5)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(5, 15)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(15, 26)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(26, 37)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(37, 47)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(47, 56)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(56, 61)]),
            Pixels(self._npx, *[self._hexagons[x] for x in range(61, 63)])
        ]

        self._lines = [
            Pixels(self._npx, *[self._pixels[x] for x in [224, 225]]),
            Pixels(self._npx, *[self._pixels[x] for x in [60, 61]]),
            Pixels(self._npx, *[self._pixels[x] for x in [58, 59, 220, 221, 222, 223]]),
            Pixels(self._npx, *[self._pixels[x] for x in [62, 63, 64, 65, 226, 227]]),
            Pixels(self._npx, *[self._pixels[x] for x in [54, 55, 56, 57, 216, 217, 218, 219, 300, 301]]),
            Pixels(self._npx, *[self._pixels[x] for x in [66, 67, 68, 69, 228, 229, 230, 231]]),
            Pixels(self._npx, *[self._pixels[x] for x in [50, 51, 52, 53, 212, 213, 214, 215, 296, 297, 298, 299]]),
            Pixels(self._npx, *[self._pixels[x] for x in [70, 71, 72, 73, 232, 233, 234, 235]]),
            Pixels(self._npx, *[self._pixels[x] for x in [46, 47, 48, 49, 166, 167, 168, 169, 292, 293, 294, 295]]),
            Pixels(self._npx, *[self._pixels[x] for x in [0, 1, 74, 75, 76, 77, 236, 237, 238, 239, 302, 303]]),
            Pixels(self._npx, *[self._pixels[x] for x in [42, 43, 44, 45, 162, 163, 164, 165, 288, 289, 290, 291]]),
            Pixels(self._npx, *[self._pixels[x] for x in [2, 3, 4, 5, 78, 79, 80, 81, 240, 241, 242, 243, 304, 305, 306, 307]]),
            Pixels(self._npx, *[self._pixels[x] for x in [38, 39, 40, 41, 158, 159, 160, 161, 284, 285, 286, 287]]),
            Pixels(self._npx, *[self._pixels[x] for x in [6, 7, 8, 9, 82, 83, 84, 85, 244, 245, 246, 247, 308, 309, 310, 311]]),
            Pixels(self._npx, *[self._pixels[x] for x in [34, 35, 36, 37, 154, 155, 156, 157, 280, 281, 282, 283, 328, 329]]),
            Pixels(self._npx, *[self._pixels[x] for x in [10, 11, 12, 13, 86, 87, 88, 89, 248, 249, 250, 251, 312, 313, 314, 315]]),
            Pixels(self._npx, *[self._pixels[x] for x in [30, 31, 32, 33, 150, 151, 152, 153, 276, 277, 278, 279, 324, 325, 326, 327]]),
            Pixels(self._npx, *[self._pixels[x] for x in [14, 15, 16, 17, 90, 91, 92, 93, 252, 253, 254, 255, 316, 317, 318, 319]]),
            Pixels(self._npx, *[self._pixels[x] for x in [26, 27, 28, 29, 146, 147, 148, 149, 272, 273, 274, 275, 322, 323]]),
            Pixels(self._npx, *[self._pixels[x] for x in [18, 19, 94, 95, 96, 97, 256, 257, 258, 259, 320, 321]]),
            Pixels(self._npx, *[self._pixels[x] for x in [22, 23, 24, 25, 106, 107, 108, 109, 268, 269, 270, 271]]),
            Pixels(self._npx, *[self._pixels[x] for x in [98, 99, 100, 101, 260, 261, 262, 263]]),
            Pixels(self._npx, *[self._pixels[x] for x in [20, 21, 104, 105, 266, 267]]),
            Pixels(self._npx, *[self._pixels[x] for x in [102, 103, 264, 265]]),
        ]

        self._hypnotoad = [
            Pixels(self._npx, *[self._hexagons[x] for x in [28, 29, 30, 31, 32, 33]]),
            Pixels(self._npx, *[self._hexagons[x] for x in [27, 34, 38, 39, 40, 41, 42, 43, 44, 23, 22, 21, 20, 19, 18, 17]]),
            Pixels(self._npx, *[self._hexagons[x] for x in [26, 35, 37, 45, 24, 16, 6, 7, 8, 9, 10, 11, 12, 13, 48, 49, 50, 51, 52, 53, 54, 55]]),
            Pixels(self._npx, *[self._hexagons[x] for x in [0, 1, 2, 3, 4, 5, 25, 36, 14, 15, 46, 47, 56, 57, 58, 59, 60]]),
            Pixels(self._npx, *[self._hexagons[x] for x in [61, 62]]),
        ]

    def hexagons(self):
        return Pixels(self._npx, *self._hexagons)

    def salted_honey(self):
        '''
        :return: The pixel set of all letters in the words.
        '''
        return Pixels(self._npx, *self._letters)

    def rows_descending(self):
        return Pixels(self._npx, *self._rows)

    def rows_ascending(self):
        inverse = self._rows.copy()
        inverse.reverse()
        return Pixels(self._npx, *inverse)

    def stripes_rtl(self):
        return Pixels(self._npx, *self._lines)

    def stripes_ltr(self):
        inverse = self._lines.copy()
        inverse.reverse()
        return Pixels(self._npx, *inverse)

    def hypnotoad_out(self):
        return Pixels(self._npx, *self._hypnotoad)

    def hypnotoad_in(self):
        inverse = self._hypnotoad.copy()
        inverse.reverse()
        return Pixels(self._npx, *inverse)

    def test(self):
        return Pixels(self._npx, *self._hexagons)

