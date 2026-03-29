import lgpio
import threading
import time
import googleapiclient.discovery

digit_pins = (17,27,22,5)
segment_pins = (6,13,26,23,24,25,12,16)

seven_seg_outputs = {'0':'11111100','1':'01100000','2':'11011010','3':'11110010','4':'01100110','5':'10110110','6':'10111110','7':'11100000','8':'11111110','9':'11110110','k':'01101110','m':'11101100'}

segment_output = ['0','0','0','0']

stop = threading.Event()

sub_count = 0


def main():
	#Set up the API and gpio pins
	with open('cfg.txt') as cfg_file:
		API_KEY = cfg_file.readline()
		yt_handle = cfg_file.readline()
	youtube = googleapiclient.discovery.build("youtube","v3",developerKey = API_KEY)
	global request
	request = youtube.channels().list(part="statistics", forHandle=yt_handle)
	global h
	h = lgpio.gpiochip_open(0)
	for segp in segment_pins:
		lgpio.gpio_claim_output(h,segp,0)
	for digitp in digit_pins:
		lgpio.gpio_claim_output(h,digitp,1)

	data_thread = threading.Thread(target=get_sub_count)
	data_thread.start()
	try:
		while True:
			convert_subs()
			draw_subs()
#			print(segment_output)
			#time.sleep(1)
	except KeyboardInterrupt:
		for segp in segment_pins:
			lgpio.gpio_write(h,segp,0)
		lgpio.gpiochip_close(h)
		stop.set()
		
def get_sub_count():
	global sub_count
	while not stop.is_set():
		response = request.execute()
		sub_count = response['items'][0]['statistics']['subscriberCount']
		stop.wait(10) #delay between calls
	stop.set()

def convert_subs():
	global sub_count
	subs_num = int(sub_count)
	if subs_num < 1000:
		segment_output[0] = 0
		segment_output[1] = int(subs_num / 100)
		segment_output[2] = int(subs_num % 100 / 10)
		segment_output[3] = int(subs_num % 10)
	else:
		segment_output[0] = sub_count[0]
		segment_output[1] = sub_count[1]
		segment_output[2] = sub_count[2]
		if subs_num < 1000000:
			segment_output[3] = 'k'
		else:
			segment_output[3] = 'm'

def draw_subs():
	global h
	global sub_count
	decimal_place =(len(str(sub_count))%3)-1
	for i in range(4):
		curr_digit = str(segment_output[i])
		for dpin in digit_pins:
			lgpio.gpio_write(h,dpin,1)
		digit_pattern = seven_seg_outputs[curr_digit]
		for j, seg_pin in enumerate(segment_pins):
			lgpio.gpio_write(h,seg_pin,int(digit_pattern[j]))
		if i == decimal_place and int(sub_count) >= 1000:
			lgpio.gpio_write(h,16,1)
		lgpio.gpio_write(h, digit_pins[i], 0)
		time.sleep(0.002)
#	print("drew digit")
main()
