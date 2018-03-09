#!/usr/bin/env python
###Taken from Lampshader's reddit post###

def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)

#debugging comments
#raw = 0x21a6616
#raw = 35284502
while True:	
	raw = int(raw_input("Insert hex value for 26-bit Wiegand HID card (I.E. 0x21a6616): "), 16)
	FAC_PAR_MASK  = 0b10000000000000000000000000
	FACILITY_MASK = 0b01111111100000000000000000
	CARD_MASK     = 0b00000000011111111111111110
	CARD_PAR_MASK = 1;


	facility = (raw & FACILITY_MASK) >> 17
	card = (raw & CARD_MASK) >> 1

	fac_par = (raw & FAC_PAR_MASK) >> 25 
# even parity
	fac_par_ok = (bitCount(facility) + fac_par) % 2 == 0

	card_par = raw & CARD_PAR_MASK
# odd parity
	card_par_ok = (bitCount(card) + card_par) % 2 == 1

	if fac_par_ok and card_par_ok:
	    print("Both parity bits ok, successful read.")
	    print("Facility:", facility)
	    print("Card:", card)
	else:
	    if not fac_par_ok:
	        print("Facility parity check failed!")
	    if not card_par_ok:
	        print("Card parity check failed!")
