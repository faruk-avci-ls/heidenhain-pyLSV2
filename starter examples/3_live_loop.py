import pyLSV2
import time

ip = "0.0.0.0" 
port = 19000

tnc = pyLSV2.LSV2(ip, port, safe_mode = False)

tnc.connect()

while True:
    axis = tnc.axes_location()
    override = tnc.override_state()
    xpos = axis.get('X', 0)
    ypos = axis.get('Y', 0)
    zpos = axis.get('Z', 0)
    print(f"X: {xpos}, Y: {ypos},Z : {zpos}")
    print(f"Feed: {override.feed}% Rapid: {override.rapid}% Speed: {override.spindle}%")
    time.sleep(0.2)

# Sample output from a real Heidenhain TNC600 series machine:
# X: 65.663, Y: -32.719, Z: -2.097472, Feed: 100.0% , Speed:  100.0% , Rapid: 100.0% 
# X: 65.663, Y: -32.719, Z: 0.499594, Feed: 100.0% , Speed:  100.0% , Rapid: 100.0% 
# X: 65.663, Y: -32.719, Z: 5.193796, Feed: 100.0% , Speed:  100.0% , Rapid: 100.0%
