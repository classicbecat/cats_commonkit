#   ____ ____ _  __
#  / ___/ ___| |/ /
# | |  | |   | ' / 
# | |__| |___| . \ 
#  \____\____|_|\_\
# -- Cats_Commonkit --
# (C) 2026 classicbecat
# Licensed under AGPL 3.0.

# 1.0

import os
import time
import sys

def clear():
     if sys.platform == "win32":
          os.system("cls")
     else:
         os.system("clear")
         
def wait(wt):
     time.sleep(wt)
     
def menu_one(menu_text):
     print(f"""
     -----------------
        {menu_text}
     -----------------
     """)
        
def menu_two(menu_text, menu_text_sub):
    print(f"""
   ------------------------
         {menu_text}
         {menu_text_sub}
   ------------------------
    """)
    
menu_two("hello", "hello2")
    
     
     

