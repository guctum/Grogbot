# Grogbot
## Features
- Dad jokes - using the command !joke returns a dad joke in whatever channel the command came from.

## Planned Features
- Web Scraper - allow users to specify a category of games and cheaper ones will be returned from the Steam website
- Music Bot - might look into spinning together a music functionality of this bot since people in my server already use a music bot
- Polls - my group uses weekly polls, so this will let that be packaged under one bot if I decide to implement it

## Setup
My development environment is using Python 3.9 - others can likely be used but this is what I use
### Discord Developer
- Navigate to the Discord Developer portal - https://discord.com/developers/applications
- Click 'New Application'
- Go through the process of creating an application on Discord
- After an application is created, add a bot user to the application and make note of the token in the Bot section of the created app
### Required Libraries
- discord.py
- python-dotenv
- beatufiulsoup4
- Use the command pip install {library} within the venv setup (I use a venv setup from IntelliJ)
### How To Run This Locally
- Ensure Python 3 and pip are installed
- Install the libraries listed in above section
- Create a .env file and add your discord token to it
    - this token is the token generated in the Bot section - place this in the .env file
        - see the .env.example file for an example of what it looks like
    - Ensure the .env file will not be checked into version control if a VCS system is being used
        - Discord will likely notice the token and change it, so better to skip the headache
        - Shouldn't be an issue, if using this repo .env files are already in the .gitignore file
    - Run the command 'python bot.py' and the bot should spin up!
### Bonus - Cloud Server for 24/7 Hosting!
I have this running on a free tier EC2 instance from AWS
#### Steps To Create Cloud Environment
- Navigate to the AWS Management Console - https://console.aws.amazon.com/?nc2=h_m_mc
- If you have an account, sign in to the console
    - If you don't have an account, sign up for one as it will cost nothing
- Navigate to EC2 instances, and create a new instance
- Work through all the options, I don't set security instances on simple servers for Discord bots but generally speaking create security rules for important items
    - For the AMI, I use Amazon Linux 2
    - Create a new key pair and make sure to download the .pem file
- After the server has launched, SSH into the session - this can be done from various options, standalone terminal or even directly from the EC2 console
- After remoting into the session, run the following commands:
    - sudo yum install python3 -y
    - python3 -m venv bot/env
    - cd bot
    - sudo yum install git
    - git clone {wherever the repo exists}
    - sudo yum install pip
    - source ~/bot/env/bin/activate
    - Install the libraries from the Required Libraries section
    - screen
    - python3 bot.py
- After running the final command, the SSH session can be closed without the bot shutting down upon closing the SSH session 