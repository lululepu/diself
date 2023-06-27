# diself

![Python version](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This is a selfbot module created by lululepu.

## Description

The selfbot module provides functionality for interacting with the Discord API using a selfbot.

## Installation

Install the selfbot module using `pip`:

```python
pip install diself
```

## Setup

1. Obtain your Discord user token. You can follow the steps below to get your token:
   - Open Discord in your web browser.
   - Press `Ctrl + Shift + I` to open the Developer Tools.
   - Go to the "Network" tab.
   - Send a message in any channel.
   - Look for a network request that starts with `messages` and contains your user ID. Click on it.
   - In the request headers, find the `authorization` field. Your user token is the value after `Bearer`.

2. Create a Python script and import the `selfbot_module`:
```python
import diself
```
3. Instantiate the `Client` class with your Discord user token:

```python
client = diself.Client("YOUR_USER_TOKEN")
```

4. Implement your desired functionality using the provided methods and events.

## Usage

```python
import diself

@diself.event
def on_message(msg):
    print(msg) # print the raw message json
    print(msg.content) # print the message content
    print(msg.channel) # print the message channel
    print(msg.guild) # print the message guild
    chid=msg.channel # Get the channel
    message=chid.send("hey") # Send the message "key" to the channel
    message.delete() # Delete the message

@diself.event
def on_ready():
  print(f"Connected to '{client.username}#{client.discriminator}' ({client.id})") # Print this in the cmd when the client is ready

client = diself.Client("YOUR_USER_TOKEN")
```

## Liscense

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
