
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
I addition to the dependancies you wil have to create a [Open Weather Map](https://openweathermap.org/) and get a `API Key`. Read about how to get a 'API Key' in the open weather mao FAQ section [here](https://openweathermap.org/faq)

## Configuring environment Variables
- Firstly Generate a `Secret Key`. This is required by the Flask [Sessions](https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions). 
Do read the section on  ***How to generate good secret keys***  in the flask documentation under 
sessions [here](https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions)
- Next export the secret key and API key to Enviroment Variables using one of the following commands based on your terminal
Bash command 
```bash
  export SECRET_KEY=<your secret key>
  export API_KEY=<your API key>
```
CMD command
```bash
  set SECRET_KEY=<your secret key>
  set API_KEY=<your API key>
```
Powershell command
```powershell
  $env:SECRET_KEY=<your secret key>
  $env:API_KEY=<your API key>
```
The enviroment variables are then read using the [os.environ object](https://www.geeksforgeeks.org/python-os-environ-object/)
## Running the app 
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

## Deploying to Heroku
- There's a good explanation of this given in this [repo](https://github.com/MirelaI/flask_heroku_example)
- Another good read on the topic is on the Real Python [website](https://realpython.com/flask-by-example-part-1-project-setup/) 

## References
- Open Weather Map Current Weather Map API Docs - https://openweathermap.org/current
- Flask Docs - https://flask.palletsprojects.com/en/2.0.x/
- Bootstrap Docs - https://getbootstrap.com/docs/5.0/getting-started/introduction/
