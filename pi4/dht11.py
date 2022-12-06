
import Adafruit_DHT

class DHT11:
    def __init__(self,pin:int):
        self.dht_sensor=Adafruit_DHT.DHT11
        self.dht_pin=pin
    
    def read(self)->tuple[int,int]:
        """ Return humidity and temperature
        Returns:
            (int,int): humidity and temperature
        """           
        return Adafruit_DHT.read_retry(self.dht_sensor,self.dht_pin)
    
    def read_str(self):
        humidity, temperature = self.read()
        return "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(humidity, temperature)

dht=DHT11(4)
print(dht.read_str())