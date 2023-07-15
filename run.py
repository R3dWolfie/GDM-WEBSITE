import requests
import patreon
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

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



@app.route('/')
@app.route('/home')
def home():
    buy_vip_url = '/buy-vip'
    discord_url = 'https://discord.gg/gdm'
    latest_supporters = []

    for pledge in all_pledges:
        latest_supporters.append(pledge.relationship('patron').attribute('full_name'))

    # latest_supporters = get_latest_supporters()
    return render_template('home.html', buy_vip_url=buy_vip_url, discord_url=discord_url, latest_supporters=latest_supporters)


@app.route('/downloads')
def downloads():
    return render_template('downloads.html')


@app.route('/VIP')
def VIP():
    return render_template('VIP.html')


@app.route('/about')
def about():
    return render_template('about.html.')


if __name__ == '__main__':
    print("Fetching patrons...")
    app.run(debug=True, host="0.0.0.0")
