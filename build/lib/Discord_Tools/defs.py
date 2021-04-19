import logging



class DTGuild:
    def __init__(self , guild_name:str , guild_id=None):
        self.name = guild_name
        self.id = guild_id
        self.properties = {
            "name" : self.name,
            "id"   : self.id
        }
        self.orgproperties = self.properties.copy()

    def edit(self , property:str , change):
        if(property in list(self.properties.keys())):
            self.properties[property] = change
            self.__updatejson()
        else:
            logging.error(f"{property} not a valid property of {self} \nValid Properties = {list(self.properties.keys())}")
        
    
    def __updatejson(self):
        self.name = self.properties.get("name")
        self.id = self.properties.get("id")

    def reset_properties(self):
        self.properties =self.orgproperties.copy()
        self.__updatejson()
    

    

class DTChannel:
    def __init__(self ,guild:DTGuild, channel:str = None , index:int = None , channel_id:int = None):
        if(channel == None and index == None):
            raise ValueError("Atleast one of ['channel','index'] must be specified.")
        self.id = channel_id
        self.guild = guild.name
        self.channel = channel
        self.index = index
        self.properties = {
            "guild"  :  self.guild,
            "channel":  self.channel,
            "id"  :  self.id,
            "index" : self.index
        }
        self.orgproperties = self.properties.copy()

    def edit(self , property:str , change):
        if(property in list(self.properties.keys())):
            self.properties[property] = change
            self.__updatejson()
        else:
            logging.error(f"'{property}' not a valid property of {self} \nValid Properties = {list(self.properties.keys())}")
        
    
    def __updatejson(self):
        self.id = self.properties.get("id")
        self.guild = self.properties.get("guild")
        self.channel = self.properties.get("channel")
        self.index = self.properties.get("index")

    def reset_properties(self):
        self.properties =self.orgproperties.copy()
        self.__updatejson()
    


    