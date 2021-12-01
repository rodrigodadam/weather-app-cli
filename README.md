<div align="center">
<h1>Weather APP - CLI</h1>
</div>

<br>

This project was created to complete the third Milestone Project for the Code Institute's Full Stack Developer course.
The project purpose is: build a command-line application that allows your users to manage a common dataset about a particular domain.
For this reason I've used the Weather API.


Link to the cli-application available [HERE.](https://weather-app-cli.herokuapp.com/)

<br>
<div align="center">

![Home Page](https://github.com/rodrigodadam/weather-app-cli/blob/main/images/home.png)

</div>
<br>

# Table of Contents

- [UX]()
  * [Project Goals](#Project-Goals)
  * [Users Experience Plan](#Users-Experience-Plan)
  * [Front-End](#Front-end)


- [Features](#Features)

- [Technologies Used](#Technologies-Used)

- [Resources](#Resources)

- [Deployment](#Deployment)

- [Credits](#Credits)


## Project Goals

From command-line the user can input the City Name and the Country Code to check the Weather status for the day.

## Users Experience Plan

This is a command-line application using Code Institute Templates to properly use this App after deployment.
The App consists of a unique command-line data the user can insert the City name and Country Code to check the weather status, if the City and Code do not match, the user needs to insert the data again until get the correct information the CLI will work. After giving all the weather status to the user the program stops working.

<div align="right"><a href="#top">🔝</a></div>


## Structure Plan


### Front-end

Using a CODE INSTITUTE TEMPLATE for this CLI APP.


<br>

<div align="right"><a href="#top">🔝</a></div>

<br>


## FEATURES

### Existing Features

This project is well-structured to work efficiently.

- As soon you open this webapp you can see some information how use it to give you the correct weather information to an input city.
  - You need input a correct city name as image below.

![City Name](https://github.com/rodrigodadam/weather-app-cli/blob/main/images/structure/cityname.png)

  - After insert a real city name, will be asked to you input a country code. This code is an ISO CODE based in 2 characters only.

![Country Code](https://github.com/rodrigodadam/weather-app-cli/blob/main/images/structure/countrycode.png)


This project has 2 types of validation, one is REGEX validation, used before the input data goes to the endpoint avoiding code injection. Also the second is a data validation that checks if the City and Country match to give correct weather information based in the API service data store.
 
### Features Left To Implement

Insert a option to the client choice the weather forecast for the next days. 

### Problems and Solutions

To deploy this project on HEROKU I need to use the disable_warnings from urllib3 pac. Unfortunately heroku do not work well with OpenWeather API and get a https error.

<div align="right"><a href="#top">🔝</a></div>

## TECHNOLOGIES USED

- [Gitpod](https://www.gitpod.io/) 
- [Git](https://git-scm.com/) 
- [GitHub](https://github.com/)
- [OpenWeatherAPI](https://openweathermap.org/)


<div align="right"><a href="#top">🔝</a></div>

## RESOURCES

### General Resources

- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)
- [OpenWeatherAPI](https://openweathermap.org/)

### Tools

- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
- [PEP8 Online](http://pep8online.com/)

<div align="right"><a href="#top">🔝</a></div>

### Test Strategy

Testing is required on all features and user stories documented in this README. 

 - PYTHON Code must pass through the [PEP* Validator](https://github.com/rodrigodadam/weather-app-cli/blob/main/images/pep8-weatherapp.png)


## Deployment

### Project Creation

To create this project I used the CI Gitpod Full Template by navigating here and clicking the 'Use this template' button.

I was then directed to the create new repository from the template page and entered in my desired repo name, then clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

The following commands were used for version control throughout the project:

git add filename - This command was used to add files to the staging area before committing.

git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

git push - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

Create application:

Navigate to Heroku.com and login<br>
Click on the new button<br>
Select create new app<br>
Enter the app name<br>
Select region<br>

Set up connection to Github Repository:<br>


Click the deploy tab and select GitHub - Connect to GitHub<br>
A prompt to find a github repository to connect to will then be displayed<br>
Enter the repository name for the project and click search<br>
Once the repo has been found, click the connect button<br>

Set environment variables:<br>

Click the settings tab and then click the Reveal Config Vars button and add the following:<br>

key: KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure)<br>
Enable automatic deployment:<br>

Click the Deploy tab<br>
In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.<br>

Navigate to the GitHub Repository.<br>
Click the Code drop down menu.<br>
Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.<br>
Open your developement editor of choice and open a terminal window in a directory of your choice.<br>
Use the 'git clone' command in terminal followed by the copied git URL.<br>
A clone of the project will be created locally on your machine.<br>
Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:<br>

pip install -r requirements.txt<br>

  <div align="right"><a href="#top">🔝</a></div>

CREDITS

— Researches —

To fix some bugs that I do not found inside documentation I used the Community Stackoverflow to help me with this bugs and Google.com

ACKNOWLEDGEMENTS

My Dear Friend Rimom Costa for all support.
My Mentor Anthony for continuous helpful feedback.
All Code Institute Tutor Support.
