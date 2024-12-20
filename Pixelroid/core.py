from pyrogram import Client
from Pixelroid import api_id, api_hash, bot_token

class PixelroidBot:
    def __init__(self, api_id: int, api_hash: str, bot_token: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.xemishra = Client(
            name="PornBot",
            api_id=self.api_id,
            api_hash=self.api_hash,
            bot_token=self.bot_token
        )
