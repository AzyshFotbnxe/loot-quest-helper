# loot-quest-helper
A very simple helper to assist player enter save codes into loot quest faster.  
Loot Quest is a RPG workshop mode in Overwatch.  
For more details about Loot Quest, please see https://us.forums.blizzard.com/en/overwatch/t/367704  
Special thanks to *Ciege#8558* who provided the core function to make this possible.

## Features

1. Thanks to Ciege, the basic function of this is to input the save code automatically.
2. Local save manager is finished.  
    Store saved codes locally then next time it can be picked out from GUI rather than typing it again

## Usage
To use this, please have Git installed on your device in advance.

Firstly, clone this project to your local repo.
```
git clone https://github.com/sanosenx86/loot-quest-helper.git
```

Then install dependent packages:
``` 
python pip install pyautogui keyboard
```

Then run by execute the main:
```
python gui_main.py
```

## Future features: 
(These ~~will never~~ may not be actually implemented)
* Multithreading  
    Allows user interrupt the input when something goes wrong.
* Customized hotkey binding  
    Allows user to change what key they want to use in both Overwatch and in this helper.
* (Very unlikely to be implemented) Automatically recognize save code from screenshot.  
    Some CV stuff involved.
