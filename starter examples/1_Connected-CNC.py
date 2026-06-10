import pyLSV2

ip =   "0.0.0.0"   #your cnc machines ip
port = 19000   

tnc = pyLSV2.LSV2(ip, port, safe_mode = False )  
tnc.connect()   
 
axis = tnc.axes_location() 

xpos = axis.get('X', 0)   
print(f"Live X Axis Position = {xpos}") 

tnc.disconnect()     