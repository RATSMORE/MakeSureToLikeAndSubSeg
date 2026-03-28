import lgpio


'''
17 D1
27 D2
22 D3
5  D4



'''

output_digits = ('11111101')

try:
	h = lgpio.gpiochip_open(0)

	gpio_pins = (17,27,22,5,6,13,26,23,24,25,12,16)

	digit_pins = (17,27,22,5)
	segment_pins = (6,13,26,23,24,25,12,16)

	for pins in gpio_pins:
		lgpio.gpio_claim_output(h,pins)
	for segments in segment_pins:
		
		lgpio.gpio_write(h,segments,int(output_digits[segment_pins.index(segments)]))

	lgpio.gpio_write(h, digit_pins[0], 0)
	while True:
		pass

except KeyboardInterrupt:
	for pins in gpio_pins:
		lgpio.gpio_write(h,pins,0)
		lgpio.gpio_free(h,pins)
	lgpio.gpiochip_close(h)
