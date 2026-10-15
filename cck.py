#   ____ ____ _  __
#  / ___/ ___| |/ /
# | |  | |   | ' / 
# | |__| |___| . \ 
#  \____\____|_|\_\
# -- Cats_Commonkit --
# (C) 2026 classicbecat
# Licensed under AGPL 3.0.

# 2.0-beta

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

def menu_three(menu_text, menu_text_op1, menu_text_op2, menu_text_op3, menu_text_op4):
     print(f"""
---------------------------------------------------------------------------

{menu_text}

 {menu_text_op1}
 {menu_text_op2}
 {menu_text_op3}
 {menu_text_op4}
 
---------------------------------------------------------------------------
""")

def sysinfo():
     print(f"""
     === System Info (CCK) ===
     operating system: {os.name}
     platform: {sys.platform}
     python version: { sys.version.split()[0]}
     cpu cores: {os.cpu_count()}
     """)
     

     

