import requests
import random

def get_pokemon_info(pokemon_id):
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    species_response = requests.get(species_url)
    pokemon_response = requests.get(pokemon_url)

    if species_response.status_code == 200 and pokemon_response.status_code == 200:
        species_data = species_response.json()
        pokemon_data = pokemon_response.json()

        # 日本語名を取得
        japanese_name = "不明"
        for name in species_data["names"]:
            if name["language"]["name"] == "ja":
                japanese_name = name["name"]
                break

        # 日本語のタイプを取得
        types = []
        for t in pokemon_data["types"]:
            type_url = t["type"]["url"]  # タイプの詳細URL
            type_data = requests.get(type_url).json()  # タイプの詳細情報を取得
            for name in type_data["names"]:
                if name["language"]["name"] == "ja":
                    types.append(name["name"])
                    break

        # 重さ（デシキログラムをkgに変換）
        weight_kg = pokemon_data["weight"] / 10

        # 結果を表示
        print(f"✅ ポケモン: {japanese_name}（ID: {pokemon_id}）")
        print(f"タイプ: {', '.join(types)}")
        print(f"重さ: {weight_kg} kg")

    else:
        print(f"❌ エラー: ポケモン ID {pokemon_id} が見つかりません。")

if __name__ == "__main__":
    random_pokemon_id = random.randint(1, 151)  # 1〜151 のランダムなポケモン
    get_pokemon_info(random_pokemon_id)
