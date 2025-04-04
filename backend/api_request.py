import requests
import pandas as pd 
BASE_URL = "https://api.cartola.globo.com"

def get_clubs_info():
    """ Return a DataFrame """

    url = f"{BASE_URL}/clubes"
    response = requests.get(url)
    if response.status_code == 200:
        clubs_dada = response.json()
        df_clubs = pd.DataFrame.from_dict(clubs_dada, orient="index") # clubs_data is a json
        df_clubs = df_clubs[["id", "nome", "abreviacao"]]
        return df_clubs
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")

def get_posicoes_info():
    """ Return a DataFrame """

    url = f"{BASE_URL}/posicoes"
    response = requests.get(url)
    if response.status_code == 200:
        posicoes_data = response.json()
        return pd.DataFrame.from_dict(posicoes_data, orient="index")
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
        players_df = players_df[["atleta_id", "clube_id", "posicao_id", "preco_num", "pontos_num", "media_num", "jogos_num", "variacao_num", "status_id", "entrou_em_campo"]]
        return players_df
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")

def get_rodada_info():
    """ Return a DataFrame """

    url = f"{BASE_URL}/mercado/status"
    response = requests.get(url)
    if response.status_code == 200:
        rodada_data = response.json()
        filtered_data = {
            "rodada_atual": rodada_data.get("rodada_atual"),
            "status_mercado": rodada_data.get("status_mercado"),
            "temporada": rodada_data.get("temporada"),
            "fechamento": rodada_data.get("fechamento", {}).get("timestamp")
        }
        return pd.DataFrame([filtered_data])
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")


def get_current_match_info():
    """ Return a DataFrame """

    url = f"{BASE_URL}/partidas"
    response = requests.get(url)
    if response.status_code == 200:
        matches_data = response.json()
        matches_df = pd.DataFrame(matches_data["partidas"])
        matches_df = matches_df[["clube_casa_id", "clube_visitante_id"]]
        return matches_df
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")


def get_match_info(i: int):
    """ Return a DataFrame """

    url = f"{BASE_URL}/partidas/{i}"
    response = requests.get(url)
    if response.status_code == 200:
        matches_data = response.json()
        matches_df = pd.DataFrame(matches_data["partidas"])
        matches_df = matches_df[["clube_casa_id", "clube_visitante_id", "placar_oficial_mandante", "placar_oficial_visitante"]]
        return matches_df
    else:
        #TODO: Raise a real error
        print(f"Failed to retrieve data {response.status_code}")


players_info = get_rodada_info()
print(players_info.head())
