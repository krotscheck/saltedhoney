import uasyncio

from rainbow import Rainbow
from glimmer import Glimmer
from runner import Runner
from sign import Sign

s = Sign()

# Build the list of programs to be managed...
programs = [
    # Glimmer program, random fade of different LED's
    # Hue program, single color hue range.
    # Field of Stars

    Rainbow(s.stripes_ltr(), "Rainbow- Stripes Left to Right"),
    Rainbow(s.stripes_rtl(), "Rainbow- Stripes Right to Left"),
    Rainbow(s.rows_descending(), "Rainbow- Vertical Descending"),
    Rainbow(s.rows_ascending(), "Rainbow- Vertical Ascending"),
    Rainbow(s.hypnotoad_out(), "Rainbow- Hypnotoad Out"),
    Rainbow(s.hypnotoad_in(), "Rainbow- Hypnotoad In"),
    Rainbow(s.test(), "Rainbow- Test Pattern"),
    Glimmer(s.test(), 230, 0, 0, "Glimmer- Red"),
    Glimmer(s.test(), 50, 140, 50, "Glimmer- Aqua"),
    Glimmer(s.test(), 50, 50, 140, "Glimmer- Purple"),
    Glimmer(s.test(), 140, 50, 50, "Glimmer- Pink"),
    Glimmer(s.test(), 255, 103, 64, "Glimmer- Peach"),
    Glimmer(s.test(), 230, 100, 0, "Glimmer- Honey"),
    Glimmer(s.test(), 230, 230, 230, "Glimmer- White"),
    Glimmer(s.test(), 101, 67, 33, "Glimmer- Nature"),
]

# Start event loop and run entry point coroutine
main = Runner(s.salted_honey(), programs)
uasyncio.run(main.run())

