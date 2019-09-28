'''
Created on 19 jun. 2019

@author: Guim
'''
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
config.sections()
threads = config['BASIC']['ThreadsON']
listThreads = threads.split("::")

for thread in listThreads:
    print(config[thread]["Home"])