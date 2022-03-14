import time
import pigpio
import wiegand
import antenna
import RPi.GPIO as GPIO 


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.IN) 




def callback(bits, value):
    card_id = int("{:026b}".format(value)[1:25],2)
    if "{:010d}".format(card_id) == "0000000000":
        if GPIO.input(2) == 1:
            print("No hay corriente en la antena.")
        else:
            print("Problemas con la antena, fuente de poder funciona perfectamente")
        wiegand_decoder.cancel()
    elif bits < 26:
        print("Cable de tierra para la lectura no conectado.")
        wiegand_decoder.cancel()
    else:
        print("Card ID: {:010d}".format(card_id))
pi = pigpio.pi()
wiegand_decoder = wiegand.Decoder(pi, 14, 15, callback)
time.sleep(60)
wiegand_decoder.cancel()


