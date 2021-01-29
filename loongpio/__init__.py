import digitalio as _digitalio
import pulseio as _pulseio
import busio as _busio
import time as _time
from typing import Union as _Union, Optional as _Optional

from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin as _Pin

_LsPin = _Union[_Pin, int]

class DigitalInputOutput(object):
    @staticmethod
    def lspin_to_libgpiod_pin(pin: _LsPin) -> _Pin:
        if type(pin) is int:
            __pin = _Pin(pin)
        elif type(pin) is _Pin:
            __pin = pin
        else:
            raise TypeError('Invalid pin: ' + str(pin))
        return __pin

    def __init__(self, pin: _LsPin) -> None:
        self._io = _digitalio.DigitalInOut(DigitalInputOutput.lspin_to_libgpiod_pin(pin))

class DigitalInput(DigitalInputOutput):
    def __init__(self, pin: _LsPin) -> None:
        super().__init__(pin)
        self._io.direction = _digitalio.Direction.INPUT

    @property
    def value(self) -> bool:
        return self._io.value

    def wait_until(self, value: bool) -> None:
        while self.value == (not value):
            _time.sleep(0.01)

    def wait_until_high(self) -> None:
        wait_until(True)

    def wait_until_low(self) -> None:
        wait_until(False)

class DigitalOutput(DigitalInputOutput):
    def __init__(self, pin: _LsPin):
        super().__init__(pin)
        self._io.direction = _digitalio.Direction.OUTPUT

    @property
    def value(self) -> bool:
        return self._io.value

    @value.setter
    def value(self, value: bool) -> None:
        self._io.value = value

    def on(self) -> None:
        self.value = True

    def off(self) -> None:
        self.value = False

class PWMOutput(object):
    def __init__(self, pin: int, frequency: int = 500, duty_cycle: int = 0) -> None:
        self._output = _pulseio.PWMOut(pin, frequency=frequency, duty_cycle=duty_cycle)

    @property
    def duty_cycle(self) -> int:
        return self._output.duty_cycle

    @duty_cycle.setter
    def duty_cycle(self, value: int) -> None:
        self._output.duty_cycle = value

    @property
    def frequency(self) -> int:
        return self._output.frequency

    @duty_cycle.setter
    def frequency(self, value: int) -> None:
        self._output.frequency = value

    def __del__(self) -> None:
        self._output = None

class Button(DigitalInput):
    def __init__(self, pin: _LsPin, is_active_low: bool = False) -> None:
        super().__init__(pin)
        self.is_active_low = is_active_low

    def wait_until_press(self) -> None:
        self.wait_until(not self.is_active_low)

    @property
    def is_pressed(self) -> bool:
        return self.is_active_low != self.value

Button.wait_for_press = Button.wait_until_press

class LED(DigitalOutput):
    def __init__(self, pin: _LsPin) -> None:
        super().__init__(pin)

class PWMLED(PWMOutput):
    def __init__(self, pin: int, frequency: int = 500) -> None:
        super().__init__(pin, frequency)

    @property
    def value(self) -> float:
        return self.duty_cycle / 65535.0

    @value.setter
    def value(self, value: float) -> None:
        self.duty_cycle = int(value * 65535.0)

class Servo(PWMOutput):
    def __init__(self, pin: int) -> None:
        super().__init__(pin, 50)

    # 0 -> 0.05
    # 1 -> 0.1

    @property
    def value(self) -> float:
        return (self.duty_cycle / 65535.0 - 0.025) * 20.0

    @value.setter
    def value(self, value: float) -> None:
        self.duty_cycle = int((value * 0.05 + 0.025) * 65535.0)

    @property
    def angle(self) -> float:
        return self.value * 180.0

    @angle.setter
    def angle(self, angle: float) -> None:
        self.value = angle / 180.0

    def min(self) -> None:
        self.angle = 0

    def mid(self) -> None:
        self.angle = 90

    def max(self) -> None:
        self.angle = 180

class TonalBuzzer(PWMOutput):
    @staticmethod
    def spn_to_freq(spn: str) -> float:
        try:
            note = (spn[:-1] if len(spn) > 1 else spn)
            octave = (int(spn[-1]) if len(spn) > 1 else 4)
            offset = {
                'C': 0, 'C#': 1, 'Db': 1, 'D': 2,
                'D#': 3, 'Eb': 3, 'E': 4, 'F': 5,
                'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
                'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10,
                'B': 11 }[note]
            base = (octave + 1) * 12
            freq = 440.0 * (2 ** ((base + offset - 69) / 12.0))
            return freq
        except:
            raise ValueError('Invalid Scientific Pitch Notation %s. Valid examples: C4, C#4, Db5' % spn)

    def __init__(self, pin: int) -> None:
        super().__init__(pin)

    def play(self, tone: _Union[float, str]) -> None:
        if type(tone) in [float, int]:
            freq = tone
        elif type(tone) is str:
            freq = TonalBuzzer.spn_to_freq(tone)
        else:
            raise TypeError('Invalid tone: ' + str(tone))

        self.frequency = freq
        self.duty_cycle = 32767

    def stop(self) -> None:
        self.duty_cycle = 0

class DHT11(object):
    def __init__(self, pin: _LsPin) -> None:
        raise NotImplementedError('DHT11 is not supported yet')

class DistanceSensor(object):

    def __init__(self, trigger: _LsPin, echo: _LsPin) -> None:
        try:
            import adafruit_hcsr04
        except ImportError:
            raise RuntimeError('Adafruit_HCSR04 module is not installed. Run `apt install python3-adafruit-circuitpython-hcsr04` as root to install.') from ImportError
        self._sonar = adafruit_hcsr04.HCSR04(
            trigger_pin=DigitalInputOutput.lspin_to_libgpiod_pin(trigger),
            echo_pin=DigitalInputOutput.lspin_to_libgpiod_pin(echo))

    @property
    def distance(self) -> _Optional[float]:
        try:
            return self._sonar.distance
        except RuntimeError:
            return None

class BH1750(object):
    def __init__(self, scl: _LsPin, sda: _LsPin) -> None:
        try:
            import adafruit_bh1750
        except ImportError:
            raise RuntimeError('Adafruit_BH1750 module is not installed. Run `apt install python3-adafruit-circuitpython-bh1750` as root to install.') from ImportError
        self._sensor = adafruit_bh1750.BH1750(_busio.I2C(
            scl=DigitalInputOutput.lspin_to_libgpiod_pin(scl),
            sda=DigitalInputOutput.lspin_to_libgpiod_pin(sda)))

    @property
    def lux(self) -> float:
        return self._sensor.lux
