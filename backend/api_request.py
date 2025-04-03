import requests
import pandas as pd 
BASE_URL = "https://api.cartola.globo.com"

def get_clubs_info():
    """ Return a Response Object """

    url = f"{BASE_URL}/clubes"
    response = requests.get(url)
    if response.status_code == 200:
        clubs_dada = response.json()
        df_clubs = pd.DataFrame.from_dict(clubs_dada, orient="index") # clubs_data is a json
        df_clubs = df_clubs[["id", "nome", "abreviacao"]]
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")


def get_players_info():
    """ Return a DataFrame """

    url = f"{BASE_URL}/atletas/mercado"
    response = requests.get(url)
    if response.status_code == 200:
        players_dada = response.json()
        players_df = pd.DataFrame(players_dada["atletas"]) # players_dada["atletas"] return a list
        players_df = players_df[["apelido", "clube_id", "posicao_id", "preco_num", "media_num", "jogos_num", "variacao_num"]]
        return players_df
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")
    

players_info = get_players_info()
print(players_info.head())
