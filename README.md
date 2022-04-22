# Universim Discord Bot

Discord bot for Universim, a Minecraft server hosted with Minestrator.

## Installation

### Source

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
git clone git@github.com:Obeeron/UniversimBot.git
cd UniversimBot
pip3 install -r requirements.txt
```

Then rename *config.sample.yml* to *config.yml* and complete it.

### Docker

```bash
mkdir UniversimBot
cd UniversimBot
wget https://raw.githubusercontent.com/Obeeron/UniversimBot/master/docker-compose.yml
```

Then rename *config.sample.yml* to *config.yml* and complete it.

## Run

### Source

```python
python3 main.py
```

### Docker

```bash
docker-compose up -d
```

## Usage

### Commands

- ```!servinfo```  
  > Sends the server status, its ip, and the number of players

## Config

config.yml
```yaml
minestrator:
  api_key: yourApiKey
  code_support: XXXXX

discord:
  bot_token: yourBotToken

server:
  name: serverName
  ip: serverIp
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
