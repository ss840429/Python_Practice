# Please get the fbchat library from https://github.com/ss840429/fbchat
# which is fixed some bug

import fbchat


# Subclass FBBack.Client and override required methods

class EchoBot(fbchat.Client):

    def __init__(self, email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        #if you are not the author, echo
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
 
        print(metadata)
        sticker_id = metadata['delta'].get('stickerId')

        if not sticker_id:
        	print("%s said: %s"%(author_name, message))
        else:
        	print("%s send a sticker: %s"%(author_name, sticker_id))
   
        if str(author_id) != str(self.uid):
            self.send(author_id, message, sticker_id=sticker_id)





bot = EchoBot("email@email", "password")
bot.listen()