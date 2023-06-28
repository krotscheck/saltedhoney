import machine
import uasyncio


class Runner:

    def __init__(self, letters, programs):
        self.brightness = -1
        self.programs = programs
        self.program = self.programs[0]
        self.letters = letters

        # Define our hardware controls
        self.btn_next = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)
        self.btn_prev = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
        self.led_next = machine.PWM(machine.Pin(11))
        self.led_next.freq(1000)
        self.led_prev = machine.PWM(machine.Pin(15))
        self.led_prev.freq(1000)

        self.pot_brightness = machine.ADC(26)

        self.led_power = machine.Pin(25, machine.Pin.OUT)

    async def run(self):
        # Turn on the power
        self.led_power.toggle()

        # Coroutine: entry point for asyncio program, start coroutine as a task and immediately return
        uasyncio.create_task(self.dimmer_value())
        uasyncio.create_task(self.next_button())
        uasyncio.create_task(self.previous_button())
        uasyncio.create_task(self.update_leds())

        # Main loop
        while True:
            await uasyncio.sleep(.01)

    def set_program(self, idx):
        if idx < 0:
            idx = len(self.programs) - 1
        if idx >= len(self.programs):
            idx = 0

        if idx != self.programs.index(self.program):
            self.program.reset()
            self.program = self.programs[idx]

    async def dimmer_value(self):
        while True:
            raw_pot_value = self.pot_brightness.read_u16()
            self.led_next.duty_u16(raw_pot_value)
            self.led_prev.duty_u16(raw_pot_value)

            new_brightness = int(round(raw_pot_value * 100 / 65536, 1))
            if new_brightness - 1 > self.brightness or new_brightness + 1 < self.brightness:
                self.brightness = new_brightness
            await uasyncio.sleep(.1)

    async def next_button(self):
        # Invoke the next button
        value_previous = self.btn_next.value()

        while True:
            if self.btn_next.value() != value_previous:
                value_previous = self.btn_next.value()
                if value_previous == 0:
                    self.set_program(self.programs.index(self.program) + 1)
            await uasyncio.sleep(.01)

    async def previous_button(self):
        # Invoke the previous button
        value_previous = self.btn_prev.value()

        while True:
            if self.btn_prev.value() != value_previous:
                value_previous = self.btn_prev.value()
                if value_previous == 0:
                    self.set_program(self.programs.index(self.program) - 1)
            await uasyncio.sleep(.001)

    async def update_leds(self):
        # Update the color of the LED's.
        while True:
            #self.letters.color(0, 0, 0, int(255 * self.brightness / 100))
            self.letters.color(0,0,0,int(255 * self.brightness / 100))
            self.program.step(self.brightness)
            await uasyncio.sleep(.001)

