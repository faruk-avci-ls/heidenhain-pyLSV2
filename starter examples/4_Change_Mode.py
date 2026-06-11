import pyLSV2

ip = "0.0.0.0" 
port = 19000

tnc = pyLSV2.LSV2(ip, port , safe_mode = False)
tnc.connect()
sign = tnc.login(pyLSV2.Login.MONITOR) 

tnc.set_keyboard_access(False)
tnc.send_key_code(pyLSV2.KeyCode.MODE_AUTOMATIC)
tnc.set_keyboard_access(True)

#Change your machine mode 

# MODE_MANUAL
# MODE_SINGLE_STEP
# MODE_AUTOMATIC
# MODE_PGM_EDIT
# MODE_HANDWHELL
# MODE_PGM_SIMULATION