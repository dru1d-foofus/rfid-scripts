#!/usr/bin/env python
###dru1d@dru1d.ninja###
###Taken from ccdesignworks.com/wiegand_calc.html###

def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)

while True:
###Variables and stuff###
	FACILITY_CODE = int(raw_input("Insert FC: "))
	BADGE_ID	  = int(raw_input("Insert BadgeID: "))
	FAC_PAR_MASK  = 0b10000000000000000000000000
	FACILITY_MASK = 0b01111111100000000000000000
	CARD_MASK     = 0b00000000011111111111111110
	CARD_PAR_MASK = 1;
	FCH = format(FACILITY_CODE, 'x')
	BIH = format(BADGE_ID, 'x')
	FCH_PADDED = "{:02x}".format(int(FCH, 16))
	FCB = format(int(FCH_PADDED,16), '008b')
	BIH_PADDED = "{:04x}".format(int(BIH, 16))
	BIB = format(int(BIH_PADDED,16), '0016b')
	CARD_BINARY = FCB + BIB
	

###Parity Bit Magic###
####Upper Parity Bit (EVEN)
	UPPER_PARITY = 0
	for i in CARD_BINARY[0:12]:
		bit = bin(int(i))
		if bit != 0:
			UPPER_PARITY ^= 1

####Lower Parity Bit (ODD)
	LOWER_PARITY = 1
	for i in CARD_BINARY[12:24]:
		bit = bin(int(i))
		if bit != 0:
			LOWER_PARITY ^= 1

###Final Badge Values###
	BINARY_BADGE = int(str(LOWER_PARITY) + CARD_BINARY + str(UPPER_PARITY), 2)
	HEX_BADGE = hex(BINARY_BADGE)

###Parity Check###
	FACILITY = (BINARY_BADGE & FACILITY_MASK) >> 17
	CARD = (BINARY_BADGE & CARD_MASK) >> 1
	
	FACILITY_PAR = (BINARY_BADGE & FAC_PAR_MASK) >> 25
	CARD_PAR = (BINARY_BADGE & CARD_PAR_MASK)
####Even Parity Check
	FAC_PAR_OK = (bitCount(FACILITY) + FACILITY_PAR) % 2 == 0
####Odd Parity Check
	CARD_PAR_OK = (bitCount(CARD) + CARD_PAR) % 2 ==1




###Print Statements###	
	if FAC_PAR_OK and CARD_PAR_OK:
		print("Both parity bits OK. Success!" + "\n")
		print("FC (HEX): 0x%s" % str(FCH_PADDED))
		print("Badge ID(HEX): 0x%s" % str((BIH_PADDED)))
		print("Binary Card Data: %s" % str(BINARY_BADGE))
		print("Hex Card Data: %s" % HEX_BADGE)
	else:
		if not FAC_PAR_OK:
			print("Facility parity check failed.")
		if not CARD_PAR_OK:
			print("Card parity check failed.")
