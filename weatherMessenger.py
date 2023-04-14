import json
import requests
print("★Visit weatherapi.com to get Your own API\n★Please Note that temperature may vary!\n★And Your internet connection must be stable!")

#Use this api if you dont want to create your own! This may work if api is valid
choice = input("\nWant to continue with default API? (May work or may not)\n y for Yes | n for No: ")
name_of_city = input("\nName of Your City: ")
if choice == "y":
	my_api = '''
8e56db69ef72455f8d4105508231404'''

	web = f"https://api.weatherapi.com/v1/current.json?key={my_api}&q={name_of_city}"
	#print(web)

else:
	api = input("\nEnter Your API Key: ")
	web = f"https://api.weatherapi.com/v1/current.json?key={api}&q={name_of_city}"
#print(web)
	

	

try:
	r = requests.get(web)
	#print("\n", r.text)
	p = json.loads(r.text)
	
	print("\nCurrent Temperature: ", p["current"]["temp_c"], "°C")
	
except KeyError:
	#print("Check your API & City")
	raise KeyError("Check Your API and City!")
	
except:
	print("\nWait for a day to get your API updated to the sever!\n")
	