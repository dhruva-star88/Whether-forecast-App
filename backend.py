import requests

API_KEY = "1b7f61267ebdece62423c1fac4f3f9c3"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_of_values = 8 * days
    filtered_data = filtered_data[:num_of_values]
    """
    In the following list comprehension, "i" is dictionary, in that "main" is another dict. and from that we extracting
    "temp" key-values. 
    In another list comprehension, "i" is dict. and "whether" is list, In that list index="0" is first element and that 
    is dict. From that we are extracting "main" key-values.
    """
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Bangalore", days=1))
