import patreon

client_id = "tWe8WLdrzldJNM1W2wwQO47x6w3V-jXKWHxqoKpAEQYkstEXQHJndxUN01qvSw2n"  # Replace with your client ID
client_secret = "nddXb3R832dFtzEo62RBwRX6BIXK86NpeE5dXGrbbTAsUPCEvZYy5A3E8yz8BKSa"  # Replace with your client secret
access_token = "eWl9Ls5o4sebZvXfkmRFRUL-qcSbiHZEgIAbyxPULAA"  # Replace with your access token

api_client = patreon.API(access_token)

# Get the campaign ID
campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()

all_pledges = []

cursor = None
while True:
    pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)

    cursor = api_client.extract_cursor(pledges_response)
    all_pledges += pledges_response.data()
    if not cursor:
        break

latest_supporters = []

for pledge in all_pledges:
    latest_supporters.append(pledge.relationship('patron').attribute('full_name'))