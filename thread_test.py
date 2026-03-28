import lgpio
import googleapiclient.discovery
import threading
import time

#sub_count = 0
stop = threading.Event() #controls whether API is being called


pi_pins = (17,27,22,5,6,13,26,18,23,24,25)



def get_sub_count(): #just calls the youtube API to get subs
	global sub_count
	while not stop.is_set():
		response = request.execute()
		sub_count = response['items'][0]['statistics']['subscriberCount']
		#sub_count += 1
		print(sub_count)
		time.sleep(15)


def convert_subs():	#takes the value of sub_count and makes screen output
	

	pass

def main():
	api_service_name = "youtube"
	api_version = "v3"
	with open('api.txt') as api_file:
		API_KEY = api_file.readline()
	youtube = googleapiclient.discovery.build(api_service_name, api_version,developerKey = API_KEY)
	global request
	request = youtube.channels().list(
		part="statistics",
		forHandle="THERATSMORE"
	)
	data_thread = threading.Thread(target=get_sub_count)
	data_thread.start()
	while True:
		#print(sub_count)
		convert_subs()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		stop.set()
		print("done")
