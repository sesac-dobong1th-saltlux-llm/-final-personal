ranking_data.py : 랭커 유저의 player_id 수집

> ranking_data.csv

match_data.ipynb: ranking_data.csv로 각 플레이어의 match_id 수집 >> matcch_ids.csv
match_ids로 match_data 수집 >> match_data.json

match_data.json

각 match_id 에 따라 request

경기의 시각, 맵 종류

승리팀 5명의 player_ID

패배팀 5명의 player_ID

이후

각 player_ID 에 따라 그 플레이어의 경기정보 (필요한 정보는 characterName + position)

목표: 이긴 팀의 캐릭터 조합과 진 팀의 캐릭터 조합을 학습 후,

      사용자가 적 캐릭터 들과 자신의 팀 캐릭터들을 입력하였을 때 어떤 캐릭터를 골라야 하는지 추천
