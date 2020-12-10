import threading
import time
import requests
import os
import shutil

os.system("clear")

img = ["https://images.unsplash.com/photo-1601758174039-617983b8cdd9?ixid=MXwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=686&q=80",
       "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?ixid=MXwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
       "https://images.unsplash.com/photo-1607550315608-257a07a8b132?ixid=MXwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
      ]

os.mkdir("/home/kali/Desktop/real2")

for img_url in img:
   get = requests.get(img_url)
   name = img_name = img_url.split("/")[3]
   result = name.split("?")[0] 
   name = f"{result}.jpg"
   with open(name, 'wb') as f:
      content = f.write(get.content)
      shutil.move(name, '/home/kali/Desktop/real2')
      print("{} has been downloaded".format(result))
