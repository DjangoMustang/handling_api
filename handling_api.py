import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data['data']['data']
        result = user_data[0]['login']['username']

        return result
    else:
        raise Exception ("Failed to fetch user data")

def main():
    pass

if __name__ == "__main__":
    main()