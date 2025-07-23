# step2

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
from matplotlib.lines import Line2D

def main():
    
    # 1단계 최종 파일 불러오고, 칼럼 이름 공백 없게 수정한다.
    df = pd.read_csv('team_project/area_combined.csv')
    df.columns = df.columns.str.strip()

    # 기본적인 플롯, 그리드를 생성한다.
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_title('area_combined.csv data visualize.', fontsize=16)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # 좌표축 범위를 설정한다. - 데이터 최소/최대 값에 1만큼 여백을 추가한다.
    ax.set_xlim(df['x'].min() -1, df['x'].max() +1)
    ax.set_ylim(df['y'].max() +1, df['y'].min() -1)
    ax.set_aspect('equal', adjustable='box') # X, Y axis 비율을 동일하게 설정한다.

    for index, row in df.iterrows():
        x, y = row['x'], row['y']
        category = row['category']
        is_construction = row['ConstructionSite'] == 1

        # 우선순위에 따라 건설현장부터 체크한다.
        if is_construction:
            size = 1.1
            bottom_left = (x - size/2, y - size/2)
            rect = patches.Rectangle(bottom_left, size, size, facecolor='gray', zorder=4)
            ax.add_patch(rect)
            continue

        # 아파트,빌딩,집,커피점 설정한다.
        if category in [1,2]:
            circle = patches.Circle((x, y), radius=0.4, facecolor='brown', zorder=3)
            ax.add_patch(circle)

        elif category == 3:
            ax.plot(x, y, marker='^', color='green', markersize=20, zorder=3)

        elif category == 4:
            size = 0.8
            bottom_left = (x-size/2, y-size/2)
            rect = patches.Rectangle(bottom_left, size, size, facecolor='green', zorder=3)
            ax.add_patch(rect)

    # 범례 생성한다.
    legend_elements = [
        patches.Patch(facecolor='gray', label='ConstructionSite'),
        patches.Patch(facecolor='brown', label='apartment/buildings'),
        Line2D([0], [0], marker='^', label='MyHome', markerfacecolor='green', markersize=15),
        patches.Patch(facecolor='green', label='coffee shop')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=12)

    # 이미지 파일로 저장한다.
    plt.savefig('map.png', dpi=300, bbox_inches='tight')
    print("map saved successfully")

    plt.show()

if __name__ == "__main__":
    main()