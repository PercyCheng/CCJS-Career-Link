# CCJS-Career-Link
CP3405 Career Link App  

Windows Enviroment Setup: //Run command prompt as administrator  
//$ denotes a command to be entered into a command prompt  
Install Git  
Install python 3.6 or greater  
Download get-pip.py  
$python get-pip.py  
$python -m pip install --upgrade pip  

Project Setup  
(Choosen Directory)$git clone https://github.com/jarodhine/CCJS-Career-Link  
$python -m venv venv  
$venv\Scripts\activate.bat  
$pip install -r requirements.txt  

$python manage.py makemigraton accounts  
$python manage.py migrate  
$python manage.py runserver  

To open the venv $source ~/Desktop/Design_Thinking_III/assignment/CCJS-Career-Link/bin/activate

Mac Environment Setup:  
.Same to Windows, install Git and pip3 first.  
.Create directory to store  
.Run terminal  
.Enter the directory $cd [directory path]  

Project Setup .$git clone https://github.com/jarodhine/CCJS-Career-Link.git  
.$python3 -m venv venv  
.enter CCJS-Career-Link directory  
.$pip3 install -r requirements.txt  

Run the server  
.$python3 manage.py migrate  
.$python3 manage.py runserver  

The successful server status should be: System check identified no issues (0 silenced).  
September 11, 2019 - 11:19:47  
Django version 2.2.4, using settings 'CareerLink.settings'  
Starting development server at http://127.0.0.1:8000/  
Quit the server with CONTROL-C.  
