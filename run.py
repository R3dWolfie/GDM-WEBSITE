import requests
import patreon
from flask import Flask, render_template
import threading

app = Flask(__name__, template_folder='templates')

client_id = "tWe8WLdrzldJNM1W2wwQO47x6w3V-jXKWHxqoKpAEQYkstEXQHJndxUN01qvSw2n"  # Replace with your client ID
client_secret = "nddXb3R832dFtzEo62RBwRX6BIXK86NpeE5dXGrbbTAsUPCEvZYy5A3E8yz8BKSa"  # Replace with your client secret
access_token = "eWl9Ls5o4sebZvXfkmRFRUL-qcSbiHZEgIAbyxPULAA"  # Replace with your access token

api_client = patreon.API(access_token)

# Get the campaign ID
campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()

latest_supporters = []
cursor = None


def fetch_supporters():
    global latest_supporters, cursor

    while True:
        pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)
        cursor = api_client.extract_cursor(pledges_response)
        latest_supporters += pledges_response.data()
        if not cursor:
            break


def start_fetching():
    thread = threading.Thread(target=fetch_supporters)
    thread.start()


@app.route('/')
@app.route('/home')
def home():
    buy_vip_url = '/buy-vip'
    discord_url = 'https://discord.gg/gdm'
    supporters = [pledge.relationship('patron').attribute('full_name') for pledge in latest_supporters]

    return render_template('home.html', buy_vip_url=buy_vip_url, discord_url=discord_url, latest_supporters=supporters)


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
    start_fetching()
    print("Fetching patrons...")
    app.run(debug=True, host="0.0.0.0")
