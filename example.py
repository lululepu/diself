import diself

@diself.event
def on_messages(msg):
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