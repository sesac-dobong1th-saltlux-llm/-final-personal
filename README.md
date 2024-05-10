
ranking_data.py : 랭커 유저의 player_id 수집
> ranking_data.csv

match_data.ipynb: ranking_data.csv로 각 플레이어의 match_id 수집
                  >> matcch_ids.csv
                  match_ids로 match_data 수집
                  >> match_data.json


match_data.json

각 match_id 에 따라 request

경기의 시각, 맵 종류

승리팀 5명의 player_ID

패배팀 5명의 player_ID

이후

각 player_ID 에 따라 그 플레이어의 경기정보 (필요한 정보는 characterName + position)

                  
