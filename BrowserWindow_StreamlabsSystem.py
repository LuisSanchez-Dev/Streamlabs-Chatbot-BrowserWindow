ScriptName = "BrowserWindow"
Website = "https://github.com/LuisSanchez-Dev/Streamlabs-Chatbot-BrowserWindow"
Description = "Add your own websites directly to the app!"
Creator = "LuisSanchezDev"
Version = "1.0"

def ScriptToggled(state):
  return

def Init():
  global BrowserWindow
  BrowserWindow = Parent.GetType().Assembly.AnkhBotR2.Windows.BrowserWindow
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
  BrowserWindow("https://github.com/LuisSanchez-Dev/Streamlabs-Chatbot-BrowserWindow","BrowserWindow - Read me").Show()
  return
