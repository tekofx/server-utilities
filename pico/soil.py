from machine import ADC, Pin, I2C
import utime

# use variables instead of numbers:


class Soil:
    def __init__(self):
        self.soil = ADC(Pin(26))  # Soil moisture PIN reference

        # Calibraton values
        self.min_moisture = 336
        self.max_moisture = 30000

        self.readDelay = 3  # delay between readings

    def read(self) -> float:
        raw = self.read_raw()
        moisture = (raw - self.min_moisture) / (self.max_moisture - self.min_moisture)

        return moisture

    def read_raw(self) -> int:
        return self.soil.read_u16()


if __name__ == "__main__":
    soil = Soil()
    while True:

        moisture = soil.read()
        raw = soil.read_raw()
        # print values
        print(f"moisture: {moisture} (adc: {raw})")

        utime.sleep(2)  # set a delay between readings
