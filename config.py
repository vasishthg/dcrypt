from urllib import parse

TOKEN = "OTI0Mjc2NDc2MTUxNDk2NzE0.YccNjA.9co0tYpbFuYdpQnp2l8InNDv8Ho"
CLIENT_SECRET= "lr3OG8zcNqobSxAcIZrNZHezKx3rCuFG"
REDIRECT_URI = "http://127.0.0.1:5000/oauth/callback"
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=924276476151496714&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify"