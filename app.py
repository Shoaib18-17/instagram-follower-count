from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace with your Instagram API credentials
INSTAGRAM_ACCESS_TOKEN = 'YOUR_INSTAGRAM_ACCESS_TOKEN'
USER_ID = 'YOUR_INSTAGRAM_USER_ID'

@app.route('/instagram/followers', methods=['GET'])
def get_followers():
    url = f'https://graph.instagram.com/{USER_ID}?fields=followers_count&access_token={INSTAGRAM_ACCESS_TOKEN}'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)