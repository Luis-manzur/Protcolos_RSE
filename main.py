import time
import pigpio
import wiegand
import antenna





def callback(bits, value):
   card_id = int("{:026b}".format(value)[1:25],2)
   print("Card ID: {:010d}".format(card_id))
pi = pigpio.pi()
wiegand_decoder = wiegand.Decoder(pi, 14, 15, callback)
wiegand_status = antenna.Status_Reader(14,15)
wiegand_status.status()
time.sleep(60)
wiegand_decoder.cancel()


