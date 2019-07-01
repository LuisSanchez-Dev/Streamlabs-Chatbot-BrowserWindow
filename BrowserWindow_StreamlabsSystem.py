
import clr
clr.AddReferenceByName("AnkhBotR2, Version=1.0.2.56, Culture=neutral, PublicKeyToken=null")
from AnkhBotR2.Windows import BrowserWindow

ScriptName = "BrowserWindow"
Website = "https://github.com/LuisSanchez-Dev/Streamlabs-Chatbot-BrowserWindow"
Description = "Add your own websites directly to the app!"
Creator = "LuisSanchezDev"
Version = "1.0"

def ScriptToggled(state):
  return

def Init():
  return

def Execute(data):
  return

def ReloadSettings(jsonData):
  return

def Tick():
  return

def Unload():
  return

def OpenReadMe():
  BrowserWindow("https://www.google.com/","BrowserWindow - Read me").Show()
  return