import yaml

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    print(cfg)

CODE_SUPPORT = cfg['minestrator']['code_support']
API_KEY = cfg['minestrator']['api_key']

BOT_TOKEN = cfg['discord']['bot_token']

SERVER_IP = cfg['server']['ip']
SERVE_NAME = cfg['server']['name']