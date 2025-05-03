![banner](https://github.com/user-attachments/assets/60378b38-7776-4bed-a78b-9c3d6e0fd507)
## Made for the Pirate Software - Game Jam 16

#### Play [BURNER PHONE DX](https://codefizz.itch.io/burner-phone-dx) in your browser!  
#### Our required [Game Design Document](https://docs.google.com/document/d/1SHjlmuTUBG7k_oTGKtTy5QzmAeL_i38akRReEu16uHc/edit?usp=sharing) for submission


## Before running the project
Setting up a virtual environment is a good idea (helpful resource below)  
Install the project requirements
```
pip install -r requirements.txt
```
## Running the project on your machine
Simply run the `main.py` file located in `src/`
```
python3 main.py
```
## Assembling the project for web
Install pygbag (not in requirements.txt as it is not needed to run the project)
```
pip install pygbag
```
To run a web build of the project locally run this command inside the `src/` folder
```
pygbag --template custom.tmpl .
```
Then go to http://localhost:8000/ to test the web build  
A web build has been created in a new folder `build/`  
Just compress the `web/` directory inside of `build/` and upload this compressed file to Itch.io

## Resources
Virtual Environments:  
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/  

Pygame-ce:  
https://github.com/pygame-community/pygame-ce  
https://pyga.me/docs/  
  
Pygbag:  
https://github.com/pygame-web/pygbag  
https://pygame-web.github.io/wiki/pygbag/  
https://pygame-web.github.io/wiki/pygbag-code/#handling-persistent-data-across-sessions  
