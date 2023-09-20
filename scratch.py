import requests

# Define the API URL
api_url = "http://hn.algolia.com/api/v1/search_by_date?tags=story"

try:
    # Send a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Get the latest story (assuming the data is sorted by date)
        latest_story = data['hits'][0]

        # Print the title and URL of the latest story
        print("Latest Story:")
        print("Title:", latest_story['title'])
        print("URL:", latest_story['url'])
    else:
        print("Error: Unable to fetch data from the API")
except Exception as e:
    print("Error:", str(e))
