from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time
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


def Union(lst1, lst2): 
    final_list = lst1 + lst2 
    return final_list 

class DT:    
    def __init__(self,usrnm,pswrd):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')
        self.usrnm = usrnm
        self.psswrd = pswrd
        self.login()
        
        
    def login(self):
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
                print("[DT-ERROR]: Interruption Either due to Captcha or Incorrect Credentials")
            else:
                time.sleep(10)
                break
                
    
    def GetGuilds(self):
        global sl_element_list
        global sl
        global server_list
        global mention_list
        sl = []
        mention_list = []
        self.driver.execute_script("window.scrollTo(0, 0)") 
        server_list = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//nav[@class="wrapper-1Rf91z guilds-1SWlCJ"]').find_element(By.XPATH,'.//ul[@class="tree-3tCaw8"]').find_element(By.XPATH,'.//div[@class="scroller-2TZvBN none-2Eo-qx scrollerBase-289Jih"]').find_element(By.XPATH,'.//div[3]').find_elements(By.XPATH , './/div[@class="listItem-2P_4kh"]')
        
        for i in server_list:
            try:
                current_server = i.find_element(By.XPATH , './/div[2]').find_element(By.XPATH , './/div[@class="blobContainer-239gwq"]').find_element(By.XPATH , './/div[@class="wrapper-25eVIn"]').find_element(By.XPATH , './/*[local-name()="svg"]').find_element(By.XPATH , './/*[local-name()="foreignObject"]').find_element(By.XPATH , './/div[@class="wrapper-1BJsBx"]').get_attribute("aria-label")
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
            except:
                print(f"[DT-ERROR]: {str(i)} Is a Group (Discord Tools Does Not Currently support Group Handling)")    
                sl_element_list.append("GRP")
        return sl
       
        
    def NavigateGuild(self, guild):
        global sl_element_list
        global server_list
        global sl
        self.GetGuilds()
        
        if guild in sl_element_list:
            print(f"[DT-SUCCESS]{guild} is a Valid Guild")
            server_list[sl_element_list.index(guild)].click()
        else:
            print(f"[DT-ERROR]: {guild} is not a Valid Guild")
            
            
    def GetMentionsDict(self):
        global sl_element_list
        global server_list
        global sl
        self.GetGuilds()
        organized_mentions = dict(zip(sl,mention_list))
        return organized_mentions
    
    
    def GetGuildMentions(self,guild):
        d = self.GetMentionsDict()
        servers = d.keys()
        
        if guild in servers:
            return d.get(guild)
            print(f"[DT-SUCCESS]{guild} is a Valid Guild")
        else:
            print(f"[DT-ERROR]: {guild} is not a Valid Guild")
        
        
    def GetDMsInView(self):
        global sl_element_list
        global sl
        global server_list
        global mention_list
        global dm_list
        global dm_element_list
        
        dm_list = []
        self.NavigateHome()
        #self.driver.execute_script("window.scrollTo(0, 0)") 
        #home_button = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//nav[@class="wrapper-1Rf91z guilds-1SWlCJ"]').find_element(By.XPATH,'.//ul[@class="tree-3tCaw8"]').find_element(By.XPATH,'.//div[@class="scroller-2TZvBN none-2Eo-qx scrollerBase-289Jih"]').find_element(By.XPATH,'.//div[@class="tutorialContainer-1v44GL"]').find_element(By.XPATH,'.//div[@class="listItem-2P_4kh"]').find_element(By.XPATH,'.//div[@class="listItemWrapper-3X98Pc"]').click()
        #friends_button = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]').find_element(By.XPATH , './/nav[@class="privateChannels-1nO12o"]').find_element(By.XPATH , './/div[@class="scroller-1JbKMe thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]').find_element(By.XPATH , './/div[@class="content-3YMskv"]').find_element(By.XPATH , './/a[1]').click()
        dm_element_list = (self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]').find_element(By.XPATH , './/nav[@class="privateChannels-1nO12o"]').find_element(By.XPATH , './/div[@class="scroller-1JbKMe thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]').find_element(By.XPATH , './/div[@class="content-3YMskv"]').find_elements(By.XPATH , './/a[@class="channel-2QD9_O container-2Pjhx- clickable-1JJAn8"]'))[1:]
        
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
            print(f"[DT-SUCCESS] {dm} Is A Valid DM")
            dm_element_list[dm_list.index(dm)].click()
        else:
            print(f"[DT-ERROR] {dm} Is Not A Valid DM")
    
    
    def NavigateHome(self):
        self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//nav[@class="wrapper-1Rf91z guilds-1SWlCJ"]').find_element(By.XPATH,'.//ul[@class="tree-3tCaw8"]').find_element(By.XPATH,'.//div[@class="scroller-2TZvBN none-2Eo-qx scrollerBase-289Jih"]').find_element(By.XPATH,'.//div[@class="tutorialContainer-1v44GL"]').find_element(By.XPATH,'.//div[@class="listItem-2P_4kh"]').find_element(By.XPATH,'.//div[@class="listItemWrapper-3X98Pc"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH,'.//div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="sidebar-2K8pFh hasNotice-1XRy4h"]').find_element(By.XPATH , './/nav[@class="privateChannels-1nO12o"]').find_element(By.XPATH , './/div[@class="scroller-1JbKMe thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]').find_element(By.XPATH , './/div[@class="content-3YMskv"]').find_element(By.XPATH , './/a[1]').click()
        self.driver.execute_script("window.scrollTo(0, 0)") 
        
        
    def GetChannels(self,guild):
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
        
        
    def NavigateChannel(self,guild,chnl):
        global channel_list
        global channel_element_list
        self.GetChannels(guild)
        f = False
        time.sleep(1)
        for i in channel_list:
            time.sleep(0.2)
            if(chnl in i):
                channel_element_list[channel_list.index(i)].click()
                f=True
                print(f"[DT-SUCCESS] {chnl} Is A Valid Channel")
                break
            else:
                pass
        if(f == False):
            print(f"[DT-ERROR] {chnl} Is Not A Valid Channel")
    
    
    def NavigateChannelByIndex(self,guild,ind):
        global channel_list
        global channel_element_list
        self.GetChannels(guild)
        
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
                print("[DT-ERROR] You Do Not Have the Priveleges to Chat in This Channel")
        else:
            print("[DT-ERROR] Current Discord Page is not Keyboard Accessible for the Chat Text-Box")
    
    
    def GetMessagesInView(self):
        global message_list
        global author_list
        global time_stamp_list
        message_list=[]
        author_list = []
        time_stamp_list = []
        
        message_element_list = self.driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH , './/div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="chat-3bRxxu"]').find_element(By.XPATH , './/div[@class="content-yTz4x3"]').find_element(By.XPATH , './/main[@class="chatContent-a9vAAp"]').find_element(By.XPATH , './/div[@class="messagesWrapper-1sRNjr group-spacing-0"]').find_element(By.XPATH , './/div[1]').find_element(By.XPATH , './/div[@class="scrollerContent-WzeG7R content-3YMskv"]').find_element(By.XPATH , './/div[@class="scrollerInner-2YIMLh"]').find_elements(By.XPATH , './/div[@role="listitem"]')
        for i in message_element_list:
            try:
                author_list.append(i.find_element(By.XPATH , './/div[@class="contents-2mQqc9"]').find_element(By.XPATH , './/h2[@class="header-23xsNx"]').find_element(By.XPATH , './/span[@class="headerText-3Uvj1Y"]').find_element(By.XPATH , './/span[@role="button"]').text)
                time_stamp_list.append(i.find_element(By.XPATH , './/div[@class="contents-2mQqc9"]').find_element(By.XPATH , './/h2[@class="header-23xsNx"]').find_element(By.XPATH , './/span[1]').find_element(By.XPATH , './/span[1]').get_attribute("aria-label"))
                message_list.append(i.find_element(By.XPATH , './/div[@class="contents-2mQqc9"]').find_element(By.XPATH , './/div[@class="markup-2BOw-j messageContent-2qWWxC"]').text)      
            except:
                pass
        return list(zip(time_stamp_list, author_list , message_list))
    
    
    def GetLastMessage(self):
        global message_list
        global author_list
        global time_stamp_list
        m_v = self.GetMessagesInView()
        return m_v[len(m_v)-1]
    
    
    def SpamGuild(self,guild,chnl_indx,interval,spam,itr):
        self.NavigateHome()
        self.NavigateChannelByIndex(guild,chnl_indx)
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


