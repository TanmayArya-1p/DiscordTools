from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import speech_recognition as sr
from bs4 import BeautifulSoup
import pyttsx3
import logging
import time
from .defs import DTChannel,DTGuild
from .errors import *
from .util import ElementLocater,Union,RoleParser , RoleSorter


sl_element_list = []
server_list = []
mention_list = []
sl = []
dm_list = []
dm_element_list = []
channel_list = []
channel_element_list = []
message_list=[]
author_list = []
time_stamp_list = []



class DT:    
    def __init__(self,usrnm,pswrd,headless=False):
        op = webdriver.ChromeOptions()
        op.add_experimental_option("excludeSwitches", ["enable-logging"])
        if(headless):
            op.headless = True
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe' , options=op)
        self.usrnm = usrnm
        self.psswrd = pswrd
        self.__login()
        
        
    def __login(self):
        self.driver.get("https://discord.com/login")
        self.driver.maximize_window()
        time.sleep(6)

        username_input = self.driver.find_element_by_name('email')
        username_input.send_keys(self.usrnm)

        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(self.psswrd)
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        while True:
            if("discord.com/login" in str(self.driver.current_url)):
                logging.error("[DT-ERROR]: Interruption Either due to Captcha or Incorrect Credentials")
            else:
                time.sleep(10)
                break
                
    
    def GetGuilds(self , get_icons=False):
        global sl_element_list
        global sl
        global server_list
        global mention_list
        sl = []
        mention_list = []
        sl_return_dict = []
        self.driver.execute_script("window.scrollTo(0, 0)") 
        server_list = ElementLocater(self.driver ,['//*[@id="app-mount"]', './/div[@class="app-1q1i1E"]','.//div[@class="app-2rEoOp"]','.//div[@class="layers-3iHuyZ layers-3q14ss"]','.//div[@class="layer-3QrUeG baseLayer-35bLyl"]','.//div[@class="container-2lgZY8"]','.//nav[1]','.//ul[1]','.//div[@dir="ltr"]','.//div[3]'] ).find_elements(By.XPATH , './/div')
        
        for i in server_list:
            try:
                current_server = ElementLocater(i , ['.//div[2]', './/div[1]', './/div[@class="wrapper-25eVIn"]', './/*[local-name()="svg"]', './/*[local-name()="foreignObject"]', './/div[@class="wrapper-1BJsBx"]']).get_attribute("aria-label")
                current_server_logo = ElementLocater(i , ['.//div[2]', './/div[1]', './/div[@class="wrapper-25eVIn"]', './/*[local-name()="svg"]', './/*[local-name()="foreignObject"]', './/div[@class="wrapper-1BJsBx"]' , './/img[1]']).get_attribute("src")
                if (current_server[3:].startswith("mention, ")):
                    current_server = current_server[12:]
                    mention_list.append(1)
                elif (current_server[3:].startswith("mentions, ")):
                    handler = current_server[1:]
                    current_server = current_server[13:]
                    q= ""
                    while(handler.startswith("m") == False):
                        q = q + handler[0]
                        handler = handler[1:]
                    mention_list.append(int(q))
                else:
                    current_server = current_server[2:]
                    mention_list.append(0)
                sl.append(current_server)
                sl_element_list.append(current_server)  
                sl_return_dict.append((current_server,current_server_logo))
            except:
                #print(f"[DT-ERROR]: {str(i)} Is a Group (Discord Tools Does Not Currently support Group Handling)")    
                sl_element_list.append("GRP")
        if(get_icons):
            return sl_return_dict
        else:
            return sl
       
        
    def NavigateGuild(self, guild:DTGuild):
        time.sleep(1)
        self.NavigateHome()
        global sl_element_list
        global server_list
        global sl
        self.GetGuilds()
        
        if guild.name in sl_element_list:
            logging.info(f"[DT-SUCCESS]{guild.name} is a Valid Guild")
            server_list[sl_element_list.index(guild.name)].click()
        else:
            raise GuildNotFound(f"'{guild.name}' is not a Valid Guild")
            
            
    def GetMentionsDict(self):
        global sl_element_list
        global server_list
        global sl
        self.NavigateHome()
        self.GetGuilds()
        organized_mentions = dict(zip(sl,mention_list))
        return organized_mentions
    
    
    def GetGuildMentions(self,guild_obj:DTGuild):
        guild = guild_obj.name
        d = self.GetMentionsDict()
        servers = d.keys()
        
        if guild in servers:
            return d.get(guild)
            logging.info(f"[DT-SUCCESS]{guild} is a Valid Guild")
        else:
            raise GuildNotFound(f"[DT-ERROR]: {guild} is not a Valid Guild")
        
        
    def GetDMsInView(self):
        global sl_element_list
        global sl
        global server_list
        global mention_list
        global dm_list
        global dm_element_list
        
        dm_list = []
        self.NavigateHome()
        dms_xpath = ['//*[@id="app-mount"]', './/div[@class="app-1q1i1E"]','.//div[@class="app-2rEoOp"]','.//div[@class="layers-3iHuyZ layers-3q14ss"]','.//div[@class="layer-3QrUeG baseLayer-35bLyl"]','.//div[@class="container-2lgZY8"]','.//div[@class="base-3dtUhz"]', './/div[@class="content-98HsJk"]', './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]', './/nav[@class="privateChannels-1nO12o"]', './/div[@class="scroller-1JbKMe thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]', './/div[@class="content-3YMskv"]']
        dm_element_list = (ElementLocater(self.driver , dms_xpath).find_elements(By.XPATH , './/a[@class="channel-2QD9_O container-2Pjhx- clickable-1JJAn8"]'))[1:]
        
        for i in dm_element_list:
            if(str(i.get_attribute("aria-label")).endswith("(direct message)")):
                dm_list.append(str(i.get_attribute("aria-label"))[:-17])
            else:
                dm_list.append(str(i.get_attribute("aria-label"))[:-16])  
        return dm_list
        
        
    def NavigateDM(self,dm):
        global sl_element_list
        global sl
        global server_list
        global mention_list
        global dm_list
        global dm_element_list
        self.NavigateHome()
        self.GetDMsInView()
        self.GetGuilds()
        self.GetMentionsDict()
        
        if(dm in dm_list):
            logging.info(f"[DT-SUCCESS] {dm} Is A Valid DM")
            dm_element_list[dm_list.index(dm)].click()
        else:
            raise DMNotFound(f"[DT-ERROR] {dm} Is Not A Valid DM")
    
    
    def NavigateHome(self):
        home = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//nav[1]').find_element(By.XPATH,'.//ul[1]').find_element(By.XPATH,'.//div[2]').find_element(By.XPATH,'.//div[1]').find_element(By.XPATH,'.//div[1]').find_element(By.XPATH,'.//div[2]')
        home.click()
        time.sleep(1)
        #self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]').find_element(By.XPATH , './/nav[@class="privateChannels-1nO12o"]').find_element(By.XPATH , './/div[@class="scroller-1JbKMe thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]').find_element(By.XPATH , './/div[@class="content-3YMskv"]').find_element(By.XPATH , './/a[1]').click()
        self.driver.execute_script("window.scrollTo(0, 0)") 
        
        
    def GetChannels(self,guild_obj:DTGuild):
        guild = guild_obj.name
        global channel_list
        global channel_element_list
        self.NavigateGuild(guild)
        time.sleep(1)
        channel_list = []
        channel_element_list = (self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH , './/div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]').find_element(By.XPATH , './/nav[@class="container-3w7J-x"]').find_element(By.XPATH , './/div[@class="scroller-RmtA4e thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]').find_element(By.XPATH , './/div[@class="content-3YMskv"]').find_elements(By.XPATH , './/div[@class="containerDefault--pIXnN selected-3LIHYU"]')) + ((self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH , './/div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]').find_element(By.XPATH , './/nav[@class="container-3w7J-x"]').find_element(By.XPATH , './/div[@class="scroller-RmtA4e thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]').find_element(By.XPATH , './/div[@class="content-3YMskv"]').find_elements(By.XPATH , './/div[@class="containerDefault--pIXnN"]')))
    
        for i in channel_element_list:
            try:
                channel_list.append(str(i.find_element(By.XPATH,'.//div[@class="iconVisibility-sTNpHs wrapper-2jXpOf modeSelected-346R90"]').find_element(By.XPATH , './/div[@class="content-1x5b-n"]').find_element(By.XPATH , './/a[@class="mainContent-u_9PKf"]').get_attribute("aria-label")))
            except:
                try:
                    channel_list.append(str(i.find_element(By.XPATH,'.//div[@class="iconVisibility-sTNpHs wrapper-2jXpOf"]').find_element(By.XPATH , './/div[@class="content-1x5b-n"]').find_element(By.XPATH , './/a[@class="mainContent-u_9PKf"]').get_attribute("aria-label")))
                except:
                    pass
        return channel_list
        
        
    def NavigateChannel(self,chnl_obj:DTChannel):
        guild = chnl_obj.guild
        chnl = chnl_obj.channel
        global channel_list
        global channel_element_list
        self.GetChannels(DTGuild(guild))
        f = False
        time.sleep(1)
        for i in channel_list:
            time.sleep(0.2)
            if(chnl in i):
                channel_element_list[channel_list.index(i)].click()
                f=True
                logging.info(f"[DT-SUCCESS] {chnl} Is A Valid Channel")
                break
            else:
                pass
        if(f == False):
            raise ChannelNotFound(f"[DT-ERROR] {chnl} Is Not A Valid Channel")
    
    
    def NavigateChannelByIndex(self,chnl_obj:DTChannel):
        guild = chnl_obj.guild
        ind = chnl_obj.index
        global channel_list
        global channel_element_list
        self.GetChannels(DTGuild(guild))
        
        channel_element_list[ind].click()
            
            
    def Chat(self,msg):
        if(str(self.driver.current_url).startswith("https://discord.com/channels")):
            try:
                try:
                    text_element = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH , './/div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="chat-3bRxxu"]').find_element(By.XPATH , './/div[@class="content-yTz4x3"]').find_element(By.XPATH , './/main[@class="chatContent-a9vAAp"]').find_element(By.XPATH , './/form[@class="form-2fGMdU"]').find_element(By.XPATH , './/div[1]').find_element(By.XPATH , './/div[1]').find_element(By.XPATH , './/div[@class="channelTextArea-rNsIhG channelTextArea-2VhZ6z"]').find_element(By.XPATH , './/div[@class="scrollableContainer-2NUZem webkit-HjD9Er"]').find_element(By.XPATH , './/div[@class="inner-MADQqc sansAttachButton-td2irx"]').find_element(By.XPATH , './/div[@class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"]').find_element(By.XPATH , './/div[@class="markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP"]')
                except:
                    text_element = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH , './/div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="chat-3bRxxu"]').find_element(By.XPATH , './/div[@class="content-yTz4x3"]').find_element(By.XPATH , './/main[@class="chatContent-a9vAAp"]').find_element(By.XPATH , './/form[@class="form-2fGMdU"]').find_element(By.XPATH , './/div[@class="channelTextArea-rNsIhG channelTextArea-2VhZ6z"]').find_element(By.XPATH , './/div[@class="scrollableContainer-2NUZem webkit-HjD9Er"]').find_element(By.XPATH , './/div[@class="inner-MADQqc sansAttachButton-td2irx"]').find_element(By.XPATH , './/div[@class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"]').find_element(By.XPATH , './/div[@class="markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP"]')
                text_element.send_keys(msg)
                text_element.send_keys(Keys.ENTER)
            except:
                raise InvalidChatPerms("You Do Not Have the Priveleges to Chat in This Channel")
        else:
            raise InvalidURL("Current Discord Page is not Keyboard Accessible")
    
    
    def GetMessagesInView(self):
        global message_list
        global author_list
        global time_stamp_list
        message_list=[]
        author_list = []
        time_stamp_list = []

        soup = BeautifulSoup(self.driver.page_source , "html.parser")
        msg_element_list = soup.find( "div" ,{"class":"scrollerInner-2YIMLh"}).find_all("div" , {"role" : "listitem"})
        for i in msg_element_list:
            if(i["class"][0].startswith("message")):
            
                author_list.append(i.find("h2" , {"class" : "header-23xsNx"}).find("span" , {"class" : "headerText-3Uvj1Y"}).find('span').text)
                time_stamp_list.append(i.find("h2" , {"class" : "header-23xsNx"}).find("span").find("time").get("aria-label"))
                message_list.append(i.find_all("div" , {"class" : "markup-2BOw-j messageContent-2qWWxC"})[0].text)
            
        return list(zip(time_stamp_list, author_list , message_list))

    
    def GetLastMessage(self):
        global message_list
        global author_list
        global time_stamp_list
        m_v = self.GetMessagesInView()
        return m_v[len(m_v)-1]
    
    
    def SpamGuild(self,chnl_obj:DTChannel,interval,spam,itr):
        guild = chnl_obj.guild
        chnl_indx = chnl_obj.index
        chnl_name = chnl_obj.channel

        self.NavigateHome()
        if(chnl_indx != None):
            self.NavigateChannelByIndex(chnl_obj)
        else:
            self.NavigateChannel(chnl_obj)
        i = 0
        while i in range(0,itr):
            self.Chat(spam)
            time.sleep(interval)
            i+=1
    
    
    def SpamDM(self,dm_title,interval,spam,itr):
        self.NavigateHome()
        self.NavigateDM(dm_title)
        time.sleep(1)
        i = 0
        while i in range(0,itr):
            self.Chat(spam)
            time.sleep(interval)
            i+=1
    
    def GetMemberCount(self):
        soup = BeautifulSoup(self.driver.page_source , "html.parser")
        l = soup.find("div" , {"aria-label" : "Members"}).find_all("h2")
        role_dict = {}
        total = 0
        for i in l:
            if(i.get("class")[0].startswith("membersGroup")):
                handler = str(i.get("aria-label"))
                otpt = RoleParser(handler)
                total += otpt[1]
                role_dict[otpt[0]] = otpt[1]
        self.total_members = total
        return (total,role_dict)


    def GetAllMembers(self , guild:DTGuild):
        self.NavigateChannelByIndex(DTChannel(guild,index=0))
        soup = BeautifulSoup(self.driver.page_source , "html.parser")
        member_list = []
        for i in soup.find_all("div"):
            try:
                if(i.get("class")[0].startswith("member") and not(i.get("class")[0].startswith("membersGroup"))):
                    member_list.append(i.find("span").text)
            except:
                pass
        member_list = member_list[2:]
        return member_list

    def GetSortedMembers(self,guild:DTGuild):
        mems = list(self.GetAllMembers(guild))
        rd = dict(self.GetMemberCount()[1])
        return dict(RoleSorter(rd,mems))
    