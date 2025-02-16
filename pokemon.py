import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"✅ {pokemon_name} の情報を取得しました！")
        print(f"ID: {data['id']}")
        print(f"名前: {data['name']}")
        print(f"タイプ: {[t['type']['name'] for t in data['types']]}")
        print(f"重さ: {data['weight'] / 10} kg")  # デシキログラムなので10で割る
    else:
        print(f"❌ エラー: {response.status_code} - {pokemon_name} が見つかりません。")

if __name__ == "__main__":
    pokemon_name = input("ポケモンの名前を入力してください: ")
    get_pokemon_info(pokemon_name)
