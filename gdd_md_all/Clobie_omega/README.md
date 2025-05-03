# Omega
Omega is a powerful Python Discord bot designed to enhance your server with AI-driven features, tooling, and automation.

In development - see issues here https://github.com/Clobie/omega/issues
If you would like to contribute, please open a PR

# Features
Automod

    Removes profanity
    
    Logs warnings for users
    
AI Assistant

    General AI Chat
    
    "TL;DR" Game Design Document Assistant
    
    Time and Task log assistant
    
Cleanup

    Clean channels by user, message type, number of messages, etc
    
Credit system

    Trade/earn credits
    
Dalle-3

    Generate images
    
Gokapi

    Save attachments to file server
    
    List saved files for download
    
Inviteme

    Generates bot invite link
    
Name color

    React to name color post to get a custom name color
    
QR

    Generates custom QR codes
    
Reactor

    Detect conversation topics and sentiments, and occasionally react with relevant GIFs
    
Spam

    Flag words or phrases that will automatically be deleted
    
Update

    Designate a channel to send bot updates, commits, etc
    
    Automatically updates the bot when a new commit is detected on main branch
    

# Installation

## Postgres install

Install postgresql and initialize it

    sudo yum update
    sudo yum install postgresql-server postgresql-contrib
    sudo postgresql-setup initdb
    sudo systemctl start postgresql
    sudo systemctl enable postgresql

Swap to postgres user

    sudo -i -u postgres

Open psql

    psql

Create user and database

    CREATE DATABASE your_database_name;
    CREATE USER your_username WITH PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;

Quit psql terminal

    \q

Configure for md5 login

    sudo nano /var/lib/pgsql/data/pg_hba.conf

Find the lines that start with host and change the authentication method to md5:

    Example:
    host    all             all             127.0.0.1/32            md5
    host    all             all             ::1/128                 md5

Restart postgres

    sudo systemctl restart postgresql

Exit postgres user

    exit

## Bot installation

Git checkout - Currently, this only works in a home directory such as ~/user - change TBA

    git clone https://github.com/Clobie/omega.git

Go into the project directory

    cd omega

Create a .env file inside omega directory

    sudo nano .env

Fill out these environment variables inside the .env file

    DISCORD_BOT_TOKEN=
    OPENAI_API_KEY=
    GIPHY_API_KEY=
    DB_NAME= 
    DB_USER= 
    DB_PASS= 
    DB_HOST= 
    DB_PORT= 
    BOT_OWNER=
    UPDATE_CHANNEL=
    INVITE_ID=


If you don't have API keys for the above services, you can get them here:

    Discord - https://discord.com/developers/applications
    OpenAPI - https://platform.openai.com/
    Giphy - https://developers.giphy.com/

Run the installer - this installs the services, including the autoupdater
If you skipped the .env step, it will ask for them during the install - this is just annoying, and easier to do beforehand.

    chmod +x omega/install.sh
    ./omega/install.sh

Check that omega and omegaupdater are running

    service omega status
    service omegaupdater status

# License
This project is licensed under the MIT License.

# Support
For support, open an issue on GitHub.
