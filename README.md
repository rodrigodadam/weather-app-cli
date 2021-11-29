<div align="center">
<h1>Weather APP - CLI</h1>
</div>

<br>

This project was created to complete the third Milestone Project for the Code Institute's Full Stack Developer course.
The project purpose is: build a command-line application that allows your users to manage a common dataset about a particular domain.
For this reason I.ve used the Weather API.


Link to the web-application available [HERE.]()

<br>
<div align="center">

![Home Page]()

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

This is a command-line application using Code Institute Templates to use properly this App after deployment.
The App consisted in a unique command-line data the user can insert the City name and Country Code to check the weather status, if the City and Code do not match, the user need insert the data again until get a correct information the CLI will work. After give all the weather status to the user the program stop works.

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
The project has a simple data validation that check if the City and Country match to give a correct weather information based in the API service data store.
This project has also a REGEX validation to avoid the user inject ane spectial character into th program.

### Features Left To Implement

Refactor the project to OOP principles 
Refactor the project to SOLID principles

Insert a pop up to give confirmation about the message sent.
Change to official D Group Database after aprovation.
Insert a new field with a list of all produts that D Group sells.


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

 - PYTHON Code must pass through the [PEP* Validator](https://github.com/rodrigodadam/weather-app-cli/blob/main/pep8-weatherapp.png)


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

key: DATABASE_URL, (postgress uri)<br>
key: DEBUG, False<br>
key: IP, 0.0.0.0<br>
key: PORT, 5000<br>
key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure)<br>
Enable automatic deployment:<br>

Click the Deploy tab<br>
In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.<br>
Run Locally<br>
Note: The project will not run locally with database connections unless the user sets up an env.py file configuring IP, PORT, DATABASE_URL and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository for security purposes.<br>

Navigate to the GitHub Repository.<br>
Click the Code drop down menu.<br>
Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.<br>
Open your developement editor of choice and open a terminal window in a directory of your choice.<br>
Use the 'git clone' command in terminal followed by the copied git URL.<br>
A clone of the project will be created locally on your machine.<br>
Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:<br>

pip install -r requirements.txt<br>

  <div align="right"><a href="#top">🔝</a></div>
