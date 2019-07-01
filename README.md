# BrowserWindow
Display a website like it is from the Streamlabs Chatbot app itself.

## Usage
### 1.- Edit your .py file
Define your own function with the url and the window title.
```python
def OpenReadMe():
  BrowserWindow("https://github.com/LuisSanchez-Dev/Streamlabs-Chatbot-BrowserWindow","BrowserWindow - Read me").Show()
  return
```

### 2.- Edit your UI_Config.json file
Add the button that will trigger your function.
```json
{
    "browserReadMe":{
      "type": "button",
      "label": "Open Read Me",
      "tooltip": "Open read me for information.",
      "function": "OpenReadMe",
      "wsevent": "",
      "group": ""
    }
}
```

### 3.- Go to your Scripts tab and try it out
When clicked it will open a window similar to the ones you use to login.

# Disclaimer
This functionality is already included in the Streamlabs Chatbot application.
I am not responsible for the missuse or maintenance of the fucntionality.
I am just providing you the way to use it.