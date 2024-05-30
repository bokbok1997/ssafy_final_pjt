import json
from dotenv import load_dotenv
import os
import requests

# load .env
load_dotenv()

tmdb_api = os.environ.get('TmdbAPI')
tmdb_long_api = os.environ.get('TmdbLongAPI')

# print(tmdb_api)

# Top rate (인기순위? 탑 평점순) json 얻기 위한 로직
# for i in range(1, 11) :
#     url = f"https://api.themoviedb.org/3/movie/top_rated?language=ko-KOR&page={i}"

#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer " + tmdb_long_api
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json()

#     # print(response.text)
#     # print(data)
#     # print(data['results'][0])
#     with open(f'./data{i}.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)

for i in range(1,4) :

    url = f"https://api.themoviedb.org/3/movie/now_playing?language=ko-KOR&page={i}&region=KR"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjY4OGYyMTAyODU4MGU0ZDU0ZjA1NjVkYjlhODk1ZCIsInN1YiI6IjY2M2Q4YjQ0ODQyZjg2NzZkMmE0MjJiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.C0Mv2SarBvyrKZlciAE-UO-TIxordQuTTyJTLJguDxE"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    print(response.text)

    with open(f'./latest_data{i}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)