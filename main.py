import time
import pigpio
import wiegand
import antenna





def callback(bits, value):
    card_id = int("{:026b}".format(value)[1:25],2)
    if bits < 26:
        print("Tierra No conectada")
        wiegand_decoder.cancel()
    if "{:010d}".format(card_id) == "0000000000":
       print("Antena desconectada")
       wiegand_decoder.cancel()
    else:
        print("Card ID: {:010d}".format(card_id))
pi = pigpio.pi()
wiegand_decoder = wiegand.Decoder(pi, 14, 15, callback)
time.sleep(60)
wiegand_decoder.cancel()


