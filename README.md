![alt text](65f4a1dd9c51265f49d0.png)   
   
## Description of the project   
This project delves into the exciting realm of full-stack web development by guiding through the creation of a functional Airbnb, a web-based platform that connects travelers with hosts who have accommodations available for rent. The journey begins with a crucial step: building a command-line interpreter to manage your Airbnb entities.   
***   
## Description of the command interpreter   
This command interpreter provides the initial interface for managing objects in Airbnb clone.   
***   
### 1. How to start it   
- Clone the repository from GitHub:   
```
git clone https://github.com/ShenoudaMikhael/AirBnB_clone
```   
- Navigate to the project directory:   
```
cd AirBnB_clone
```   
- Run the command interpreter:   
```
./console.py
```   
   
   
### 2. How to use it   
you can start interacting with it by typing commands at the prompt.   
   
   
### 3. Examples   
- Help Command   
Displays a description of available commands.   
```
(hbnb) help
```   
   
- Create Command   
Creates a new instance object of a class.   
```
(hbnb) create User
```   
   
- Show Command   
Displays the string representation of an instance based on the class name and id.   
```
(hbnb) show User 123-456-789
```   
   
- Destroy Command   
Deletes an instance based on the class name and id.   
```
(hbnb) destroy User 123-456-789
```   
   
- All Command   
Displays all string representation of all instances based or not on the class name.   
```
(hbnb) all User
```   
   
- Update Command   
Updates the attribute value of the specified user object.   
```
(hbnb) update User 123-456-789 email "salsabeelahmed@gmail.com"
```   