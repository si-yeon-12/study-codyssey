# area_map.csv, area_struct.csv, area_category.csv 파일을 불러와 내용 출력 및 분석

import pandas as pd # pandas 라이브러리를 pd라는 이름으로 불러옴
import os

def load_analyze_csv():
    area_category = pd.read_csv("team_project\area_category.csv")

    area_struct = pd.read_csv("team_project\area_struct.csv")
    
    area_map = pd.read_csv("team_project\area_map.csv")

    area_struct_category = pd.merge(area_struct, area_category, 
                                    on='category', how='left')

    area_combined = pd.merge(area_struct_category, area_map, 
                             on=['x', 'y'], how='left')

    area_combined = area_combined[['area', 'x', 'y', 
                                   'category', ' struct', 'ConstructionSite']]
    print(area_combined.head(10), "\n\n\n\n\n")

    area_combined = area_combined.sort_values(by=['area', 'x', 'y'], ascending=True)
    print(area_combined.head(10))

    area_combined_one = area_combined[area_combined['area']==1]
    print(area_combined_one.head(10))

    area_combined_one.to_csv('team_project\area_combined_one.csv', index=None)

if __name__ == "__main__":
    load_analyze_csv()
    