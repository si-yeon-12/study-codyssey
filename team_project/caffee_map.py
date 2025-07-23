# area_map.csv, area_struct.csv, area_category.csv 파일을 불러와 내용 출력 및 분석

import pandas as pd # pandas 라이브러리를 pd라는 이름으로 불러옴
import os

def load_analyze_csv():
    
    # area_변수에 각각의 csv파일을 불러온다.
    area_category = pd.read_csv("team_project/area_category.csv")
    area_struct = pd.read_csv("team_project/area_struct.csv")   
    area_map = pd.read_csv("team_project/area_map.csv")

    # area_struct 파일에 category를 기준으로 area_category 파일을 합친다.
    area_struct_category = pd.merge(area_struct, area_category, 
                                    on='category', how='left')

    # 위에서 합쳐진 파일에 area_map 파일도 합친다.
    area_combined = pd.merge(area_struct_category, area_map, 
                             on=['x', 'y'], how='left')

    # 3가지 csv 파일이 모두 합쳐진 파일의 칼럼을 보기 편하게 재정렬한다.
    area_combined = area_combined[['area', 'x', 'y', 
                                   'category', ' struct', 'ConstructionSite']]
    
    # 합쳐진 파일에서 area 와 x, y 칼럼 기준 오름차순으로 값들을 정렬한다.
    area_combined = area_combined.sort_values(by=['area', 'x', 'y'], ascending=True)
    area_combined.to_csv('team_project/area_combined.csv', index=None)

    # 합쳐진 파일에서 area가 1인 값들만 모아 area_combined_one 파일을 만들고 csv 파일로 저장한다.
    area_combined_one = area_combined[area_combined['area']==1]
    area_combined_one.to_csv('team_project/area_combined_one.csv', index=None)

    # 구조물 종류별 개수를 요약해서 출력한다.
    print(area_combined[' struct'].value_counts())

if __name__ == "__main__":
    load_analyze_csv()
    