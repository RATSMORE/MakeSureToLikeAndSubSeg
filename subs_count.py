import lgpio
import googleapiclient.discovery
import threading
def main():
	api_service_name = "youtube"
	api_version = "v3"
	with open('api.txt') as api_file:
		API_KEY = api_file.readline()

	youtube = googleapiclient.discovery.build(api_service_name, api_version,developerKey = API_KEY)
	request = youtube.channels().list(
		part="statistics",
		forHandle="PewDiePie"
	)
	response = request.execute()
	sub_count = response['items'][0]['statistics']['subscriberCount']
	print(sub_count)
if __name__ == "__main__":
	main()
