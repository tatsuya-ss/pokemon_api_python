import requests
import random

def get_pokemon_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"✅ ポケモン {pokemon_id} の情報を取得しました！")
        print(f"ID: {data['id']}")
        print(f"名前: {data['name']}")
        print(f"タイプ: {[t['type']['name'] for t in data['types']]}")
        print(f"重さ: {data['weight'] / 10} kg")
    else:
        print(f"❌ エラー: {response.status_code} - ポケモン {pokemon_id} が見つかりません。")

if __name__ == "__main__":
    random_pokemon_id = random.randint(1, 151)  # 1〜151 のランダムなポケモン
    get_pokemon_info(random_pokemon_id)
