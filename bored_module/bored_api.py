import requests

# Make requests to bored api 
def get_response(type,participants,price_min, price_max,accessibility_min,accessibility_max):
    # Get response
    response = requests.get(f"https://www.boredapi.com/api/activity?type={type}&participants={participants}&minprice={price_min}&maxprice={price_max}&minaccessibility={accessibility_min}&maxaccessibility={accessibility_max}")
    # Converting response to JSON format
    data = response.json()
    if len(data) == 1 :
        raise ValueError("No activity found with the specified parameters!")
    return data

    

