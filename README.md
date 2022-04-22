# Universim Discord Bot

Discord bot for Universim, a Minecraft server hosted with Minestrator.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Run

```python
python3 main.py
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