import requests
import patreon
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


client_id = None      # Replace with your data
client_secret = None  # Replace with your data
creator_id = None     # Replace with your data

def get_latest_supporters():
    api_url = "https://www.patreon.com/api/external/feed/creator/51105446"
    headers = {"Authorization": "Bearer your_access_token"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        latest_supporters = []
        for item in data["data"]:
            supporter_name = item["attributes"]["full_name"]
            latest_supporters.append(supporter_name)
        return latest_supporters

    return None


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
    app.run(debug=True, host="0.0.0.0")
