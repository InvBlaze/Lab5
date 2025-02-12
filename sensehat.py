from sense_hat import SenseHat
import time


def get_sensehat():
    """Returns an instance of the SenseHat."""
    return SenseHat()


def alarm(sense, flash_time):
    """Flashes the SenseHat display red for the duration of flash_time."""
    red = (255, 0, 0)
    off = (0, 0, 0)

    end_time = time.time() + flash_time

    while time.time() < end_time:
        # Turn on red
        sense.clear(red)
        time.sleep(1)  # 1 second on

        # Turn off
        sense.clear(off)
        time.sleep(1)  # 1 second off

    # Ensure the display is off at the end
    sense.clear(off)
