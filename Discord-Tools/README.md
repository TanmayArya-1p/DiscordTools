## **Installation** 

```python
from discordtools import DT
```
***

## **Initializing The Discord Tools Class**

```python
from discordtools import DT

user = DT(Usrnm,Pswrd)
```

After initialising, an instance of the Selenium Chrome Window will open.
***
**Often,Discord prompts the user with a captcha(HCaptcha) or will ask the user to confirm new login location.**

![HCaptcha](https://i.imgur.com/gkScXkE.png)

![NewLoginLocation](https://i.imgur.com/3IRNoBF.png)

**If Such interruption is faced , DiscordTools will wait until the interruption is no longer seen and prompts when faced with one in the terminal.**

![TerminalPrompt](https://i.imgur.com/c3zIjda.png)
 
***
## **Attributes of** `DT(Usrnm,Pswrd)` 

***
`.usrnm`

Returns Username of User used to initialize class.
***
`.pswrd`

Returns Password of User used to initialize class
***

## **Methods of** `DT(Usrnm,Pswrd)`

***
`.GetGuilds()`

Returns List of Servers the User is a part of.

### **Example Output** :
```
["server1","server2"]
```
***
***
`.GetMentionsDict()`

Returns a Dictionary with the number of unread mentions in each Guild.

### **Example Output** :
```
{"server1" : 1 , "server2" : 2}
```
***
`.GetGuildMentions(guild)`

**args: `guild` - Guild Name(String)**


Returns the number of unread mentions in `guild`.
***
`.GetDMsInView()`

Returns a list of title of DMs in View.
(Only Works with **DMs in View** beacuase Discord works with lazy loading)
***

`.NavigateGuild(guild)`

**args: `guild` - Guild Name(String)**

Navigates to `guild` in the Selenium Chrome instance.
***

`.NavigateDM(dm)`

**args: `dm` - DM Name(String)**

Navigates to DM in the Selenium Chrome instance.
***

`.NavigateHome()`

Navigates to 
[Discord Home](discord.com/channel/@me).
***
`.GetChannels(guild)`

**args: `guild` - Guild Name(String)**

Returns a List of Channels in `guild`.
### **Example Output** :
```
["chatroom","media","memes"]
```

***
`.NavigateChannel(guild,chnl)`

**args: `guild` - Guild Name(String) , `chnl` - Channel Name(String)**


Navigates to `chnl` in `guild` in the Selenium Chrome Instance.
`chnl` can be a substring of a channel name due to unicode restrictions.
***
`.NavigateChannelByIndex(guild,ind)`

**args: `guild` - Guild Name(String) , `ind` - Channel Index(Integer)**


Navigates to the channel by index(`ind`) in `guild`.
***
`.Chat(msg)`

**args: `msg` - Message to Chat(String)**

Sends Keys of `msg` to the Input Field of the DM or a channel of a guild
***
`.GetMessagesInView()`

Returns a List of of Tuples of Messages in the open channel or DM.

### **Structure of Tuple**:
`(timestamp,author,msg)`
***
`.GetLastMessage()`

Returns a Tuple of the last message sent in a channel or DM in sthe structure mentioned above.
***
`.SpamGuild(guild,chnl_indx,interval , spam ,itr)`

**args: `guild` - Guild Name(String), `chnl_indx` - Index of Channel(Integer), `interval` - Interval between each message in seconds(Float), `spam` - Message to Spam(String), `itr` - No of Times to Spam(Integer)**

Spams `spam` in the given `chnl_indx` of `guild` - Spams `itr` times

***

`.SpamDM(dm_title,interval,spam,itr)`

**args: `dm_title` - DM Name(String), `interval` - Interval between each message in seconds(Float), `spam` - Message to Spam(String), `itr` - No of Times to Spam(Integer)**


Spams `spam` in the given DM by `dm_title`  - Spams `itr` times
***

# Other Methods That Can Be Imported

***
`DMStartVoice(DM_title)`


Starts Voice Recognition Messaging in the Direct Message of `DM_title`

### Example
```py
from Discord_Tools.main import DMStartVoice

DMStartVoice("foo")
```
The User Must Follow their message content after `chat`

For Instance, 

Saying  `chat hello` after Calling the Method will send `hello` in the mentioned `DM_title`

***

`GuildStartVoice(guild,chnl_indx)`


Starts Voice Recognition Messaging in the `guild` within the channel of index `chnl_indx`.

### Example
```py
from Discord_Tools.main import GuildStartVoice

GuildStartVoice("bar" , 0)
```
The User Must Follow their message content after `chat`

For Instance, 

Saying  `chat hello` after Calling the Method will send `hello` in the mentioned channel of `chnl_indx`

***