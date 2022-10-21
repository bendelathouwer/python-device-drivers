import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
scoop = rm.open_resource('TCPIP0::169.254.226.8::INSTR')
print(scoop.query("*IDN?"))

