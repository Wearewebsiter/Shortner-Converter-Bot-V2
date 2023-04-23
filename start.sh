echo "Cloning Repo...."
git clone https://github.com/Wearewebsiter/Link-Shortner-Converter.git /Link-Shortner-Converter
cd /Link-Shortner-Converter
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
