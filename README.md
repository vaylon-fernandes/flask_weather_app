
#  Flask Weather App
A minimal Weather app built using Flask and Bootstrap

![App image](/images/app_image.jpg)

## Demo

See a live version deployed on heroku [here](https://weatherappfh.herokuapp.com/)


  
## Run Locally

Clone the project

```bash
  git clone https://github.com/vaylon-fernandes/flask_weather_app.git
```

Go to the project directory

```bash
  cd flask_weather_app
```
Create a virtual enviroment. [Read more](https://realpython.com/python-virtual-environments-a-primer/)
```bash 
  venv <environment name>
```
#### Note: Linux user might have to install venv using the following command

Activate the virtual environment 
```bash
   apt-get install python3-venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

#### Running the app 
To run the app, first export the `FLASK_APP` variable, using one of the following commands based on your terminal<br>
Bash command 
```bash
  export FLASK_APP=main
```
CMD command
```bash
  set FLASK_APP=main
```
Powershell command
```powershell
  $env:FLASK_APP = "hello"
```
#### Run command
```bash
flask run
```
This creates a simple server, go to `http://127.0.0.1:5000/` in your browser to view the site <br>
#### Debug mode 
To run the server in Debug mode, export the `FLAK_ENV` variable befor running `flask run`
Bash command 
```bash
  export FLASK_ENV=development
```
CMD command
```bash
  set FLASK_ENV=development
```
Powershell command
```powershell
  $env:FLASK_ENV="development"
```
Run command
```bash
flask run
```
Read more here: https://flask.palletsprojects.com/en/2.0.x/quickstart/#debug-mode

  
