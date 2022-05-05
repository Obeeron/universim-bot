import requests
import config

# ===========================
#      MINESTRATOR API
# ===========================
def getServerContents():
    header = {'Authorization': config.API_KEY }
    response = requests.get(f"https://rest.minestrator.com/api/v1/server/content/{config.CODE_SUPPORT}", headers=header)
    data = response.json()["data"]
    if data == None:
        return None
    return data[0]