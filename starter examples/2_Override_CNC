import pyLSV2

ip = "0.0.0.0" 
port = 19000

tnc = pyLSV2.LSV2(ip, port, safe_mode = False)
tnc.connect()

override = tnc.override_state()

print(f"Feed: {override.feed}% Rapid: {override.rapid}% Speed: {override.spindle}%")


