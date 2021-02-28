# DiscordTools
A package to simulate user experience in Discord programatically using Selenium Web-Scraping(Chrome-Webdriver)

# Documentation 

## **Import** 

```python
from discordtools import DT
```
***

## **Initializing The Discord Tools Class**

```python
USER = DT(Usrnm,Pswrd)
```

After initialising, an instance of the Selenium Chrome Window will open.
***
**Often,Discord prompts the user with a captcha(HCaptcha) or will ask the user to confirm new login location.**

![HCaptcha](data:image/jpeg;base64,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)

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
