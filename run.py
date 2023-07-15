import requests
from flask import Flask, render_template
from patreon import API, OAuth

app = Flask(__name__, template_folder='templates')

client_id = "tWe8WLdrzldJNM1W2wwQO47x6w3V-jXKWHxqoKpAEQYkstEXQHJndxUN01qvSw2n"  # Replace with your client ID
client_secret = "nddXb3R832dFtzEo62RBwRX6BIXK86NpeE5dXGrbbTAsUPCEvZYy5A3E8yz8BKSa"  # Replace with your client secret
access_token = "eWl9Ls5o4sebZvXfkmRFRUL-qcSbiHZEgIAbyxPULAA"  # Replace with your access token

oauth_client = OAuth(client_id, client_secret)
api_client = API(access_token)

def get_latest_supporters():
    latest_supporters = ["Reddie", "Lamnhiem", "Sirrilist"]
    return latest_supporters




@app.route('/')
@app.route('/home')
def home():
    buy_vip_url = '/buy-vip'
    discord_url = 'https://discord.gg/gdm'
    latest_supporters = get_latest_supporters()
    return render_template('home.html', buy_vip_url=buy_vip_url, discord_url=discord_url,
                           latest_supporters=latest_supporters)


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
    get_latest_supporters()
    print(get_latest_supporters())
    app.run(debug=True, host="0.0.0.0")
