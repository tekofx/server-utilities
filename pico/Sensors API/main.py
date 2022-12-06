from microdot import Microdot
import wlan
import dht
ssid = 'Fibra2580'
password = 'd7shu996X29by7Ezw6c3E15i7qj7X38V'

app = Microdot()  
wlan.connect_to_network(ssid, password)

d = dht.DHT11(machine.Pin(2))

@app.route('/')
def index(request):
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    return {"temp":temp,"hum":hum}

app.run(port=80)