import websocket
import threading
import requests
import json
import time


def heartbeat(ws, start):
    while True:
        time.sleep(start["d"]["heartbeat_interval"] / 1000)
        ws.send(json.dumps({"op": 1,"d": None}))

on_message=None
on_ready=None
def event(func):
    global on_message, on_ready
    if func.__name__ == "on_message":
        on_message=func
    elif func.__name__ == "on_ready":
        on_ready=func
    return func

def wsf(token: str):
    """
    Connect to the discord websocket to receive new message/event
    To get new message do this in your code:
    @selfbot.event
    def on_messages(msg):
        print(msg) # print the raw message json
        print(msg.content) # print the message content
        msg.channel.id # Get the channel id
    """
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=10&encoding=json')
    start = json.loads(ws.recv())
    auth={"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "disco","$device": "disco"},"intents": 3276799}}
    ws.send(json.dumps(auth))
    hb=threading.Thread(target=heartbeat, args=(ws, start)).start()
    while True:
        try:
            rp=json.loads(ws.recv())
            event_type=rp["t"]
            
            if event_type == "MESSAGE_CREATE":
                on_message(Client.Message(rp["d"]))
            elif event_type == "READY":
                on_ready()
        except:...


class Client:
    """
    The main Client class
    """
    def __init__(self, token) -> None:
        global tk
        self.token=token
        tk=token
        self.client=requests.get(f"https://discord.com/api/v10/users/@me", headers={'Authorization': self.token}).json()
        for i in self.client:
            exec(f"self.{i}=self.client['{i}']")
        t1=threading.Thread(target=wsf, args=(token,)).start()

    def __str__(self):
        return json.dumps(self.client)

    class TextChannel:
        def __init__(self, id) -> None:
            self.id=id
            self.channel=requests.get(f"https://discord.com/api/v10/channels/{self.id}", headers={'Authorization': tk}).json()
            for i in self.channel:
                exec(f"self.{i}=self.channel['{i}']")
        def send(self, content):
            return Client.Message(requests.post(f"https://discord.com/api/v10/channels/{self.id}/messages", headers={'Authorization': tk} , data={'content': content}).json())
        def __str__(self):
            return json.dumps(self.channel)

    class Message:
        def __init__(self, msg) -> None:
            self.msg=msg
            for i in self.msg:
                try:
                   exec(f"self.{i}=self.msg['{i}']")
                except:pass
            self.channel=Client.TextChannel(self.channel_id)
            self.author=Client.Author(self.author["id"])
            self.guild=Client.Guild(self.guild_id)

        def delete(self):
            requests.delete(f"https://discord.com/api/v10/channels/{self.channel.id}/messages/{self.id}", headers={'Authorization': tk})

        def __str__(self):
            return json.dumps(self.msg | {"channel": json.loads(self.channel.__str__())})

    class Author:
        def __init__(self, id) -> None:
            self.id=id
            self.user=requests.get(f"https://discord.com/api/v10/users/{id}", headers={'Authorization': tk}).json()
            for i in self.user:
                if i == "global":continue
                exec(f"self.{i}=self.user['{i}']")
        def __str__(self):
            return json.dumps(self.user)

    class Guild:
        def __init__(self, gid) -> None:
            self.gid=gid
            self.guild=requests.get(f"https://discord.com/api/v10/guilds/{self.gid}", headers={'Authorization': tk}).json()
            for i in self.guild:
                if i == "global":continue
                exec(f"self.{i}=self.guild['{i}']")
        def __str__(self):
            return json.dumps(self.guild)
