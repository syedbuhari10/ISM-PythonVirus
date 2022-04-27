import hashlib
import os
from functools import partial
import json
from tkinter import *
from tkinter import filedialog
import sys
import pdb


def sha256_file_hasher(file):
    file_app = open("SHA256.txt", "a")
    with open(file, "rb") as file_read:
        bytes = file_read.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        file_app.write('\n' + str(readable_hash))

def md5_file_hasher(file):
    file_app = open("MD5 Virus Hashes.txt", "a")
    with open(file, "rb") as file_read:
        bytes = file_read.read()
        readable_hash = hashlib.md5(bytes).hexdigest()
        file_app.write('\n' + str(readable_hash))

def sha1_file_hasher(file):
    with open(file, "rb") as file_read:
        bytes = file_read.read()
        readable_hash = hashlib.sha1(bytes).hexdigest()
        record = {
                    "hash": str(readable_hash), 
                    "name": str(file)
                }
        write_json(record)

def write_json(data):
    # pdb.set_trace()
    with open("SHA1 HASHES.json", 'r+') as file:
        file_data = json.load(file)
        # print(len(file_data['data']))
        file_data['data'].append(data)
        # print(len(file_data['data']))
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent=4)


    
sha256_file_hasher(sys.argv[1])
sha1_file_hasher(sys.argv[1])
md5_file_hasher(sys.argv[1])