print (" Vamos a ingresar una direccion IP octeto por octeto a continuacion")
UNO = input ("Primer octeto: ")
DOS = input ("Segundo octeto: ")
TRES = input ("Tercer octeto: ")
CUATRO = input ("Cuarto octeto: ")

ip = (UNO+"."+DOS+"."+TRES+"."+CUATRO)

if ip.startswith("10.") or ip.startswith("172.16.") or ip.startswith("192.168."):
	tipo = "privada"

else:
	tipo = "publica"

print ("La direccion ip es: " + ip)
print ("La red es de tipo " + tipo)

