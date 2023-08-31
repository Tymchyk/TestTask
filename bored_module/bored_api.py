import requests
import sys

def get_response(type,participants,price_min, price_max,accessibility_min,accessibility_max):
    response = requests.get(f"https://www.boredapi.com/api/activity?type={type}&participants={participants}&minprice={price_min}&maxprice={price_max}&minaccessibility={accessibility_min}&maxaccessibility={accessibility_max}")
    data = response.json()
    if len(data) == 1 :
        print("No activity found with the specified parameters!")
        sys.exit()
    return data


if __name__ == "__main__":
    dict = {'type':'education', 'participants':1, 'price_min': 20, 'price_max':30,'accessibility_min':0.1,"accessibility_max":100}
    data = get_response(**dict)
    print(data)
    

