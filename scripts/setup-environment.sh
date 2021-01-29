#! /bin/sh

echo "Installing tools."
sudo yum install python3 -y
sudo yum install pip

echo "Installing Python libraries."

pip install -U discord.py
pip install requests
pip install beautifulsoup4
pip install python-dotenv

chmod +x run.sh
