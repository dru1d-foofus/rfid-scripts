#!/usr/bin/env python
###dru1d@dru1d.ninja###
###Taken from ccdesignworks.com/wiegand_calc.html###

while True:
###Variables and stuff###
	FACILITY_CODE = int(raw_input("Insert FC: "))
	BADGE_ID	  = int(raw_input("Insert BadgeID: "))
	# FAC_PAR_MASK  = 0b10000000000000000000000000
	# FACILITY_MASK = 0b01111111100000000000000000
	# CARD_MASK     = 0b00000000011111111111111110
	# CARD_PAR_MASK = 1;
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
	print("UPPER PARITY: %s" % str(UPPER_PARITY))

####Lower Parity Bit (ODD)
	LOWER_PARITY = 1
	for i in CARD_BINARY[12:24]:
		bit = bin(int(i))
		if bit != 0:
			LOWER_PARITY ^= 1
	print("LOWER PARITY: %s" % str(LOWER_PARITY))

###Final Badge Values###
	BINARY_BADGE = str(LOWER_PARITY) + CARD_BINARY + str(UPPER_PARITY)
	HEX_BADGE = hex(int(BINARY_BADGE,2))

###Print Statements###	
	print("FC (HEX): 0x%s" % str(FCH_PADDED))
	print("Badge ID(HEX): 0x%s" % str((BIH_PADDED)))
	print("Binary Card Data: %s" % BINARY_BADGE)
	print("Hex Card Data: %s" % HEX_BADGE)