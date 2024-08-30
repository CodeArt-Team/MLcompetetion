''' 
📌 Description :  

    - 경진대회 데이터 셋 보기위한 함수들 ...
    - Visualization Class :
        0)
    - DataPreprocessing class :
        0) plotSetting
        1) DataInfo
        2) column_hist
        3) column_zero_find
        4) show_corr
    - ModelTest class 
        1) real_pred_compare
        2) linear_regressor_prdict
        3) knn_regressor_predict
        4) xgboost_regressor_predict
        5) randomforest_regressor_predict
📌 Date : 2024.06.02 
📌 Author : Forrest D Park 
📌 Update : 
    2024.08.07 by pdg : DataInfo 함수 생성
    2024.08.23  by pdg : DataInfo -> 시계열 데이터 일때 그래프 시각화 하는 기능 추가 
        - 분석때 배운거 다 플랏할수있도록 함수화 하자. 

'''

def imd(image_address,width =700, height=300):
    print(f'<br><img src = "{image_address}" width="{width}" height="{height}"/><br>')
def colored_text(text, color='default', bold=False):
    '''
    #### 예시 사용법
    print(colored_text('저장 하지 않습니다.', 'red'))
    print(colored_text('저장 합니다.', 'green'))
    default,red,green,yellow,blue, magenta, cyan, white, rest
    '''
    colors = {
        'default': '\033[99m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',  # 보라색
        'cyan': '\033[96m',
        'white': '\033[97m',
        'black': '\033[30m',  # 검은색
        'bright_black': '\033[90m',  # 밝은 검정색 (회색)
        'bright_red': '\033[91m',  # 밝은 빨간색
        'bright_green': '\033[92m',  # 밝은 초록색
        'bright_yellow': '\033[93m',  # 밝은 노란색
        'bright_blue': '\033[94m',  # 밝은 파란색
        'bright_magenta': '\033[95m',  # 밝은 보라색
        'bright_cyan': '\033[96m',  # 밝은 청록색
        'bright_white': '\033[97m',  # 밝은 흰색
        'reset': '\033[0m'
    }

    # 무지개 색 추가 (RGB 값 사용)
    rainbow_colors = [
        '\033[38;2;255;0;0m',  # 빨간색
        '\033[38;2;255;127;0m',  # 주황색
        '\033[38;2;255;255;0m',  # 노란색
        '\033[38;2;0;255;0m',  # 초록색
        '\033[38;2;0;255;127m',  # 청록색
        '\033[38;2;0;0;255m',  # 파란색
        '\033[38;2;127;0;255m',  # 보라색
    ]

    # 무지개 색 추가 (색상 명칭)
    colors.update({
        'rainbow_red': rainbow_colors[0],
        'rainbow_orange': rainbow_colors[1],
        'rainbow_yellow': rainbow_colors[2],
        'rainbow_green': rainbow_colors[3],
        'rainbow_cyan': rainbow_colors[4],
        'rainbow_blue': rainbow_colors[5],
        'rainbow_magenta': rainbow_colors[6],
    })

    color_code = colors.get(color, colors['default'])
    bold_code = '\033[1m' if bold else ''
    reset_code = colors['reset']

    return f"{bold_code}{color_code}{text}{reset_code}"
def blue(str, b=False):return colored_text(str, 'blue', bold=b)
def yellow(str, b=False):return colored_text(str, 'yellow', bold=b)
def red(str, b=False):return colored_text(str, 'red', bold=b)
def green(str, b=False):return colored_text(str, 'green', bold=b)
def magenta(str, b=False):return colored_text(str, 'magenta', bold=b)
# 무지개 색 함수 추가
def rainbow_red(str, b=False):return colored_text(str, 'rainbow_red', bold=b)
def rainbow_orange(str, b=False):return colored_text(str, 'rainbow_orange', bold=b)
def rainbow_yellow(str, b=False):return colored_text(str, 'rainbow_yellow', bold=b)
def rainbow_green(str, b=False):return colored_text(str, 'rainbow_green', bold=b)
def rainbow_cyan(str, b=False):return colored_text(str, 'rainbow_cyan', bold=b)
def rainbow_blue(str, b=False):return colored_text(str, 'rainbow_blue', bold=b)
def rainbow_magenta(str, b=False):return colored_text(str, 'rainbow_magenta', bold=b)
# 검은색 함수 추가
def black(str, b=False):return colored_text(str, 'black', bold=b)
def rainbow_text(text,bold =False):
    """텍스트를 무지개색으로 한 글자씩 출력합니다."""
    rainbow_colors = [
        '\033[38;2;255;0;0m',  # 빨간색
        '\033[38;2;255;127;0m',  # 주황색
        '\033[38;2;255;255;0m',  # 노란색
        '\033[38;2;0;255;0m',  # 초록색
        '\033[38;2;0;255;127m',  # 청록색
        '\033[38;2;0;0;255m',  # 파란색
        '\033[38;2;127;0;255m',  # 보라색
    ]
    colored_text = ''
    for i, char in enumerate(text):
        colored_text += rainbow_colors[i % len(rainbow_colors)] + char
    colored_text += '\033[0m'  # 색상 초기화
    bold_code = '\033[1m' if bold else ''
    return f"{bold_code}{colored_text}"


## google api 사용하여 주소 찾기 
def find_location(test,save_ok = False, save_file_path=""):
    import googlemaps
    import pandas as pd
    my_key="AIzaSyB8IQ9_T6w74by5ctA2lHirC-_jHR0OmKI" ## google 
    maps = googlemaps.Client(key=my_key)
    
    # 지도 그리기
    import folium
    import numpy as np
    from folium.features import CustomIcon
    total_map = folium.Map(
        location=[37.55, 126.98],
        zoom_start=12,
    )
    idolbom_icoon_address = "/Users/forrestdpark/Desktop/PDG/Python_/BerryMLcompetetion/공모전/서울GovTech/돌봄서비스/idolbomi_02.png"

    icon = CustomIcon(idolbom_icoon_address, icon_size=(40, 40))
    df = pd.DataFrame(columns=['센터명', '위도', '경도', '주소'])
    for i, center in enumerate(test['센터명']):
        if i != 100000:
            try:
                
                geo_location = maps.geocode(center, language='ko')[0].get('geometry')  # 한글 주소 설정
                lat = geo_location['location']['lat']
                lng = geo_location['location']['lng']
                address_kor = maps.geocode(center, language='ko')[0].get('formatted_address')
                
                # print(f"{center} 마커 추가 {maps.geocode(center, language='ko')[0].get('formatted_address')}")  # 한글 주소 출력
                
                # DataFrame에 데이터 추가 (concat 사용)
                new_row = pd.DataFrame({'센터명': [center], '위도': [lat], '경도': [lng], '주소': [address_kor]})
                df = pd.concat([df, new_row], ignore_index=True)
                marker = folium.Marker(
                    [lat, lng],  # 각 센터의 좌표 사용
                    radius=20,
                    # icon=icon,
                    color='brown',
                    fill=True,
                    fill_color='red',
                    fill_opacity=0.8,
                    popup=f"<pre>{center} <pre>",
                    tooltip=f"{center}<br>{address_kor}"
                )
                total_map.add_child(marker)  # 마커를 지도에 추가
            except IndexError:
                print(f"{center}의 위치를 찾을 수 없습니다.")
                new_row = pd.DataFrame({'센터명': [center], '위도': [np.nan], '경도': [np.nan], '주소': [np.nan]})
                df = pd.concat([df, new_row], ignore_index=True)
            # DataFrame을 CSV 파일로 저장
    if save_ok:
        print(yellow("파일을 저장합니다."))
        df.to_csv(save_file_path, index=False, encoding='utf-8')
    return total_map

def Analysis_title(Title):
    random_imoticon = ["🙀","👻","😜","🤗","🙄","🤑","🤖"]
    import numpy as np
    import random
    imo = random_imoticon[random.randrange(1,len(random_imoticon))]
    print(rainbow_green(f"✻✻✻✻______{imo*1} {Title} {imo*1}______✻✻✻✻",True))

def df_display_centered(df):
    from IPython.display import display, HTML
    import pandas as pd 
    if type(df) != type(pd.DataFrame()):
        df=pd.DataFrame(df)
    display(HTML('<div style="text-align: center; margin-left: 50px;">{}</div>'.format(df.to_html().replace('<table>', '<table style="margin: 0 auto;">'))))

def data_watch_one(start_, dataInfo=False,data_folder_path="./데이터파일"):
    ## Data Fetching range
    start_data  =start_
    end_data =start_data+1
    
    Analysis_title(f"{start_data}-{end_data} 번 파일 데이터 보고 분석 by Forrest.D.Park")
    data_dict=DataPreprocessing.data_fetch(data_folder_path,start_data,end_data)
    
    ## data watching
    for i in range(len(data_dict.keys())):
        data_num= sorted(data_dict.keys())[i]
        print(yellow(f"\n\n{data_num} 파일의 데이터 프레임.tail() "))
        # 화면 가운데 정렬하여 출력
        df_display_centered(DataPreprocessing.key_selector(data_dict, i).tail())
        if dataInfo:
            DataPreprocessing.plotSetting()
            DataPreprocessing.dataInfo2(DataPreprocessing.key_selector(data_dict,i))
    return data_dict

def data_watch_range(start_,end_, dataInfo = False,data_folder_path="./데이터파일"):
    ## Data Fetching
    data_folder_path=data_folder_path
    start_data  =start_
    end_data =end_
    Analysis_title(f"{start_data}-{end_data} 번 파일 데이터 보고 분석 by Forrest.D.Park")
    data_dict=DataPreprocessing.data_fetch(data_folder_path,start_data,end_data)
    for i in range(len(data_dict.keys())):
        data_num= sorted(data_dict.keys())[i]
        print(yellow(f"\n\n{data_num} 파일의 데이터 프레임.tail() "))
        # 화면 가운데 정렬하여 출력
        df_display_centered(DataPreprocessing.key_selector(data_dict, i).tail())
        if dataInfo:
            DataPreprocessing.plotSetting(pltStyle='default')
            DataPreprocessing.dataInfo2(DataPreprocessing.key_selector(data_dict,i))
    return data_dict

def drawing_graph_01():
    # 여가부 그래프 따라 그리기 
    import pandas as pd
    import matplotlib.pyplot as plt

    columns = ['년도', '시간제', '종일제', '기타', '이용가구계', '가구별월평균이용시간']

    # 데이터 추가
    
    data = [
        {'년도': 2019, '시간제': 66783, '종일제': 3702, '기타': 0, '이용가구계': 70485, '가구별월평균이용시간': 71.8},
        {'년도': 2020, '시간제': 56525, '종일제': 3138, '기타': 0, '이용가구계': 59663, '가구별월평균이용시간': 87.4},
        {'년도': 2021, '시간제': 57454, '종일제': 2617, '기타': 11718, '이용가구계': 71789, '가구별월평균이용시간': 87.9},
        {'년도': 2022, '시간제': 61138, '종일제': 2760, '기타': 14314, '이용가구계': 78212, '가구별월평균이용시간': 83.1},
        {'년도': 2023, '시간제': 66515, '종일제': 1890, '기타': 17695, '이용가구계': 86100, '가구별월평균이용시간': 85.6},
    ]

    df_test = pd.DataFrame(data, columns=columns)

    # 시각화
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # bar plot for 시간제, 종일제 (옆으로 나란히)
    width = 0.2  # 막대 너비 조절
    bars_시간제 =ax1.bar(df_test['년도'] - width/2, df_test['시간제'], width, label='시간제', color='skyblue')

    # 바 플롯 위에 데이터 값 표시 (텍스트로 붙이기)
    for i, bar in enumerate(bars_시간제):
        height = bar.get_height()
        x_pos = bar.get_x()
        bar_width = bar.get_width()
        ax1.text(x_pos + bar_width / 2, height, f'{height:.0f}', ha='center', va='bottom', fontsize=8,color='blue')
        
        
        
    bars_종일제 =ax1.bar(df_test['년도'] + width/2, df_test['종일제'], width, label='종일제', color='lightcoral')
    # 바 플롯 위에 데이터 값 표시 (텍스트로 붙이기)
    for i, bar in enumerate(bars_종일제):
        height = bar.get_height()
        x_pos = bar.get_x()
        bar_width = bar.get_width()
        ax1.text(x_pos + bar_width / 2, height, f'{height:.0f}', ha='center', va='bottom', fontsize=8)

    bars_기타 =ax1.bar(df_test['년도'] + width/2*3, df_test['기타'], width, label='기타', color='lightgreen')

    # 바 플롯 위에 데이터 값 표시 (텍스트로 붙이기)
    for i, bar in enumerate(bars_기타):
        height = bar.get_height()
        x_pos = bar.get_x()
        bar_width = bar.get_width()
        ax1.text(x_pos + bar_width / 2, height, f'{height:.0f}', ha='center', va='bottom', fontsize=8)

        
    ax1.plot(df_test['년도'], df_test['이용가구계']*1.05, label='이용가구계', marker='o', linestyle='-')
    # 선 그래프 점에 데이터 값 표시 (텍스트로 붙이기)


    for i, txt in enumerate(df_test['이용가구계']):
        ax1.text(df_test['년도'][i], txt + 5500, f'{txt:.0f}', ha='center', va='bottom', fontsize=8,color='black')
    ax1.set_xlabel('년도')
    ax1.set_ylabel('이용 가구 수')
    ax1.set_title('시간제, 종일제 이용 가구 수 변화 (2019-2023)')
    ax1.legend(loc='upper left')
    ax1.set_ylim([0,110000])
    # twin axes for line plot
    ax2 = ax1.twinx()
    ax2.plot(df_test['년도'], df_test['가구별월평균이용시간'], label='가구별 월평균 이용 시간', marker='o', linestyle='-', color='darkgreen')
    for i, txt in enumerate(df_test['가구별월평균이용시간']):
        ax2.text(df_test['년도'][i], txt + 1.5, f'{txt:.0f}', ha='center', va='bottom', fontsize=9, color='darkgreen')
    ax2.set_ylabel('가구별 월평균 이용 시간 (분)')  # y축 라벨 추가
    ax2.spines['right'].set_position(('outward', 0))  # 오른쪽 축 위치 조정
    ax2.tick_params(axis='y', labelcolor='darkgreen')  # y축 라벨 색상 변경
    ax2.legend(loc='upper right')
    ax2.set_ylim([60,150])
    plt.grid(True)
    plt.show()

def 시계열그래프_칼럼안에서특정데이터에해당하는_다른열들(df,group_col="",selected_row="",target_col = [''],기준연월_str = "기준연월"):
    import matplotlib.pyplot as plt, pandas as pd
    import platform
    from matplotlib import font_manager, rc
    # unicode 설정
    기준연월_str = "기준연월"
    target = df[df[group_col]==selected_row]
    print(yellow(f"Taget data : {selected_row}"))
    
    numeric_columns=target.select_dtypes(include=['number']).columns.tolist()
    print(yellow(f"numeric colums of taget data : {numeric_columns}"))
    
    target[기준연월_str] = pd.to_datetime(target[기준연월_str], format='%Y%m')

    df_display_centered(target.head(1))
    def visualize_01(target,numeric_columns,target_col):
        ### 특정 칼럼 시각화 ####
        plt.figure(figsize=(15,8))
        for column in numeric_columns:
            if column== 기준연월_str:
                continue
            # print(column)
            if column in target_col:
                plt.plot(target[기준연월_str],target[column],label=column, marker = 'o')
        # plt.plot(target['기준연월'],target[target_col],label=target_col, marker = 'o') 
        plt.title(f'{selected_row} - 시간에 따른 {target_col} 변화')
        plt.xlabel('기준연월')
        plt.ylabel(target_col)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)

        # x축 날짜 포맷 설정
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m'))
        plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator(interval=3))
        plt.tight_layout()
        plt.show()
    visualize_01(target,numeric_columns,target_col)
    visualize_01(target,numeric_columns,['신규회원수','신규아동수','대기정회원수','웹회원수'])


def data_column_info(data_column_info_str = ""):
    if data_column_info_str:
        data_column_info = data_column_info_str
    else : 
        data_column_info=\
    '''
    - Molecule ChEMBL ID: ChEMBL 데이터베이스에서 분자의 고유 식별자     
    - Standard Type: 측정된 활성의 유형 (여기서는 IC50)        
    - Standard Relation: 활성 값의 관계 (여기서는 '=', 정확한 값을 의미)       
    - Standard Value: 표준화된 활성 값         
    - Standard Units: 활성 값의 단위 (여기서는 nM, 나노몰)       
    - pChEMBL Value: -log10(몰 단위의 활성 값). 활성의 크기를 나타내는 표준화된 값           
    - Assay ChEMBL ID: 활성을 측정한 실험의 고유 식별자         
    - Target ChEMBL ID: 목표 단백질의 고유 식별자        
    - Target Name: 목표 단백질의 이름           
    - Target Organism: 목표 단백질이 속한 생물종            
    - Target Type: 목표의 유형 (여기서는 단일 단백질)          
    - Document ChEMBL ID: 이 데이터의 출처 문서의 고유 식별자        
    - IC50_nM: IC50 값 (나노몰 단위)       
    - pIC50: -log10(IC50). IC50의 음의 로그 값으로, 활성의 크기를 나타냄          
    - Smiles: 화합물의 구조를 나타내는 SMILES 문자열 '''        
    lines = data_column_info.strip().split('\n')
    for line in lines:
        parts = line.split(':', 1)  # 콜론 기준으로 분리
        if len(parts) == 2:
            left_part = parts[0].strip()
            right_part = parts[1].strip()
            print(rainbow_orange(f"{left_part}:",True), rainbow_cyan(f"{right_part}"))
        else:
            print(line) 


def drop_single_data_col(df):
    to_drop_columns = []

    for order,i in enumerate(df.columns):
        if len(df[i].unique())==1:
            print(yellow(f"   -{order}.{i}칼럼의 데이터는 하나뿐입니다."),rainbow_cyan(" 값:"),rainbow_orange(f"{df[i].unique()[0]}"))
            to_drop_columns.append(i)
    df = df.drop(columns = to_drop_columns)
    print(blue("--- 데이터가 하나뿐인 칼럼을 삭제한 데이터프레임"))
    return df

class DataPreprocessing:
    def __init__(self) -> None:
        pass
    
    def key_selector(data_dict,num=0):
        for order,i in enumerate(sorted(data_dict.keys())):
            print(rainbow_magenta(f"\t{order} 번째 : {i}"))
        data_name= sorted(data_dict.keys())[num]
        print(rainbow_yellow(f"{num}번째 데이터를 {data_name}호출합니다. "))
        return data_dict[data_name]
    
    def data_fetch(data_folder_path,start,end):
        import os,pandas as pd
        from tqdm import tqdm  # 진행 상황 표시 라이브러리
        data_dict ={}
        count = 1
        with tqdm(total=100, desc="Data File 불러오는 중..", bar_format="{desc}:{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [elapsed: {elapsed} remaining: {remaining}]", colour='green') as pbar:
            for filename in os.listdir(data_folder_path):
                file_number = int(filename.split(".")[0])
                if file_number in range(start, end):
                    file_path = os.path.join(data_folder_path, filename)
                    if filename.endswith(".csv"):
                        data_dict[filename] = pd.read_csv(file_path)
                    elif filename.endswith((".xls", ".xlsx")):
                        data_dict[filename] = pd.read_excel(file_path)
                    else:
                        print(f"Unsupported file type: {filename}")
                    
                    pbar.update(count)
                    count += 3

        return data_dict
    
    def plotSetting(pltStyle="seaborn-v0_8"):
        '''
        # Fucntion Description : Plot 한글화 Setting
        # Date : 2024.06.05
        # Author : Forrest D Park 
        # update : 
        '''

        
        import warnings ;warnings.filterwarnings('ignore')
        import sys ;sys.path.append("../../../")
        import os 
        print(blue(f"◎ 현재 경로의 폴더 목록 --",True))
        for i,file in enumerate(os.listdir(os.getcwd())):
            if os.path.isdir(os.path.join(os.getcwd(),file)):
                print(yellow(f"  {i}. {str(os.path.join(os.getcwd(),file))}"))
        sys.path.append("../")
        sys.path.append("../../")
        
        print(blue(f"◎ 주피터 가상환경 체크 : {os.environ['CONDA_DEFAULT_ENV']}",True))
        print(blue(f"◎ Python 설치 경로:{sys.executable}",True))
        print(blue(f"◎ Graph 한글화 Setting",True))
        
  
        # graph style seaborn
        import matplotlib.pyplot as plt # visiulization
        import platform
        from matplotlib import font_manager, rc # rc : 폰트 변경 모듈font_manager : 폰트 관리 모듈
        plt.style.use(pltStyle)
        plt.rcParams['axes.unicode_minus'] = False# unicode 설정
        if platform.system() == 'Darwin': rc('font', family='AppleGothic') # os가 macos
        elif platform.system() == 'Windows': # os가 windows
            path = 'c:/Windows/Fonts/malgun.ttf' 
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            print("Unknown System")
        print(colored_text("◎ OS platform 한글 세팅완료",'blue',bold=True))
        # print(rainbow_green(f"✻✻✻✻______{imo*1} {Title} {imo*1}______✻✻✻✻",True))

    
    
    def dataInfo2(df, replace_Nan=False, PrintOutColnumber = 0,nanFillValue=0, graphPlot=True):
        ### Description  : 새운 데이터 정보 까기 함수
        import pandas as pd
        column_count = len(df.columns)
        row_count = len(df.index)
        nul_count  = df.isnull().sum().sum()
        value_kind_limit =10
        under_limit_columns =[]
        if PrintOutColnumber ==0 :
            PrintOutColnumber = column_count
        print(yellow(f" ◎ Column  : {column_count} 개 "))
        for num,i in enumerate(df.columns.tolist()):
            if num%5 != 0: 
                print(rainbow_orange(f"   {i}"), end=", ")
            else:
                print(rainbow_orange(f"\n   {i}"), end=", ")
        else:print("")
        print(yellow(f" ◎ Row size    : {row_count} 개"))
        print(yellow(f" ◎ Null count   : {nul_count} 개"))
        
        
        for idx, col in enumerate(df.columns):
            if df[f"{col}"].isnull().sum():
                print(f"   => {idx}번째.[{col}]컬럼 : ",f"null {df[f'{col}'].isnull().sum()} 개,\t not null {df[f'{col}'].notnull().sum()} 개")
                ## Null data fill
                if replace_Nan : ## nan 을 0 으로 대체 
                    df[col].fillna(value=nanFillValue, inplace=True)  
        print(yellow(" ◎ 칼럼별 데이터 중복체크"))

        for idx, col in enumerate(df.dtypes.keys()):
            value_counts = df[col].value_counts()
            under_limit_columns.append(col)
            print(yellow(f"   □ {idx+1}번째 칼럼 \" {col}\"  타입 {df.dtypes[col]})"),\
                            red(f"\n    {len(df[col].unique())}"),\
                            green(f"\t/{len(df[col])} ")+ "\t[uniq/raw]",\
            )
            
            ### Value count 값 분포 확인
            check_df = pd.DataFrame(
                    {
                        f'\"{col}\" 칼럼의 중복값': value_counts.index.tolist(),
                        '개수분포': value_counts.values.tolist()
                    },
                    index=range(1, len(value_counts) + 1)
    )

            df_display_centered(check_df.head(10))
            
            # 그래프 생성
            import matplotlib.pyplot as plt
            import seaborn as sns
            
            if len(check_df.index) <10 :
                plt.figure(figsize=(8, 6))  # 그래프 크기 설정
                labels = value_counts.index.tolist()
                for i, label in enumerate(labels):
                    # label을 문자열로 변환
                    label = str(label)
                    if len(label) > 10:
                        labels[i] = label[:10] + "..."
                colors = sns.color_palette("pastel", len(value_counts.values)) 
                # 퍼센트와 실제 수치 함께 표시
                def make_autopct(values):
                    def my_autopct(pct):
                        total = sum(values)
                        val = int(round(pct * total / 100.0))
                        return f'{pct:.1f}% ({val:d})'
                    return my_autopct

                plt.pie(value_counts.values, labels=labels, autopct=make_autopct(value_counts.values), startangle=90, colors=colors)
                plt.title(f"{col} 컬럼 값 분포 (파이 차트)", fontsize=13)
                plt.axis('equal')  # 파이 차트를 원형으로 유지
                plt.show()  # 그래프 출력
                if graphPlot :DataPreprocessing.column_hist(df,col)
            else:
                plt.figure(figsize=(14, 4))  # 그래프 크기 설정
                sns.barplot(x=value_counts.index, y=value_counts.values, palette="viridis") 
                plt.title(f"{col} 컬럼 값 분포",fontsize=13)  # 그래프 제목 설정
                # x축 레이블 길이가 10 글자 이상이면 ...으로 표현
                for label in plt.gca().get_xticklabels():
                    label = str(label)
                    if len(label) > 10:
                        label = label[:10] + "..."  # 변경
                        # label.set_text(label[:10] + "...")
                plt.ylabel("개수")  # y축 레이블 설정
                plt.xticks(rotation=45)  # x축 레이블 회전
                plt.tight_layout()  # 레이블 간 간격 조정
                plt.show()  # 그래프 출력
                if graphPlot :DataPreprocessing.column_hist(df,col)

        else: 
            print(red("\t[RESULT]"),"🙀🙀🙀"*10)
            print(yellow(f"\t🟦{value_kind_limit}개이하의 값 종류를 가지는 칼럼 "))
            # print(red(str(under_limit_columns)))
            for col in under_limit_columns:
                print("\t\t-",yellow(f"{col}:{len(df[col].unique())}: {df[col].unique().tolist()}"))
            else:
                
                print("\t",red(f"총 {len(under_limit_columns)}개"))
                print(rainbow_cyan(" ---- data frame 의 정보 조사 완료 -----}",True))
                return under_limit_columns
                

    
    
    
    def column_hist(df,col):
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        import numpy as np
        num_cols = df.select_dtypes(include=np.number).columns  # 숫자형 칼럼만 선택

        if col in num_cols:
            plt.figure(figsize=(5, 4))
            # 히스토그램과 KDE 동시에 그리기
            sns.histplot(df[col], kde=True, bins=30)
            plt.title(f"{col} -Histogram", fontsize=15)
            plt.xlabel(col, fontsize=12)
            plt.ylabel("Density", fontsize=12)
             # 기술 통계치 계산
            mean_val = df[col].mean()
            median_val = df[col].median()
            std_val = df[col].std()
            min_val = df[col].min()
            max_val = df[col].max()

            # 그래프에 기술 통계치 추가
            stats_text = (
            
            f"""평균값 : {mean_val:<10.1f}
            중앙값 : {median_val:<10.1f}
            표준편차: {std_val:<10.1f}
            최소값 : {min_val:<10.1f}
            최대값 : {max_val:<10.1f}"""
            )
            
            # 텍스트 위치 조정 (좌하단)
            plt.text(x=0.95, y=0.95, s=stats_text, fontsize=8, 
                    ha='right', va='top', transform=plt.gca().transAxes, 
                    bbox=dict(facecolor='white', alpha=0.7))
            plt.show()
        else: 
            print(colored_text("숫자형데이터가 아닙니다",'red',bold=True))
            # sns.histplot(df[col], kde=True, bins=len(df[col].unique()))
            # plt.xticks(rotation=45)  # x축 라벨을 45도 기울입니다
            # plt.show()

    # 각 컬럼별 0 값 비율,갯수보기
    def column_zero_find(data):
        import matplotlib.pyplot as plt
        dataCount = data.columns.shape[0]
        for i in range(dataCount):

            data.columns[i]
            count_zero = (data[data.columns[i]] == 0).sum()
            count_non_zero = (data[data.columns[i]] != 0).sum()
            sizes = [count_zero, count_non_zero]
            labels = [f'{count_zero}개\n0인 데이터', f'{count_non_zero}개\n0이 아닌 데이터']
            colors = ['#ff9999','#66b3ff']
            
            #파이차트 생성
            plt.figure(figsize=(3, 3))
            plt.title(f"{data.columns[i]}컬럼 0비율")
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.show()

    # 각 컬럼별 상관도 높은순으로 뽑기
    def show_corr(data,count):
        import numpy as np
        data2 = data.select_dtypes(include=np.number).columns
        filtered_corr = data2.corr()
        for i in range(len(filtered_corr.columns)):
            abs_values = filtered_corr[filtered_corr.columns[i]].abs()

            top_values = abs_values.nlargest(count)
            print(f"{filtered_corr.columns[i]} 컬럼의 상관계수 탑 5\n\n",top_values[0:count],"\n")
    
    
        ## 농가별로 데이터 나누기 
    def seperate_col_data(df,colname):
        # df  =out
        # colname ='시설아이디'
        uniq_of_col_data = df[colname].unique().tolist()
        print(yellow(f" {colname}에는 {len(uniq_of_col_data)} 종류의 데이터 가있습니다. "))
        seperated_data = {}
        for i in uniq_of_col_data:
            seperated_data[i] = df[df[colname]==i] 
        data_shapes=[seperated_data[i].shape for i in uniq_of_col_data]
        
        print(yellow(f" 기존의 data 를 "))
        for (i,j) in zip(list(seperated_data.keys()),data_shapes):
            print(yellow(f"  {i} : {j}"))
        else:print(yellow(f" 로 쪼갭니다"))
        
        # print(yellow(f"{}"))
        # return seperated_data
    ## 농사기간 계산
    def calc_duration(df, datetime_col):
        from datetime import datetime
        if datetime_col in df.columns :
            if df[datetime_col].dtype=='O':
                test_dt_start= df[datetime_col].sort_values(ignore_index=True,ascending=True).tolist()[0]
                test_dt_end= df[datetime_col].sort_values(ignore_index=True,ascending=True).tolist()[-1]
                
                # datetime.fromtimestamp(test_dt)
                date_start = datetime.strptime(test_dt_start, '%Y-%m-%d %H:%M').date()
                date_end = datetime.strptime(test_dt_end, '%Y-%m-%d %H:%M').date()
                return (date_end- date_start).days
            elif df[datetime_col].dtype=='int64':
                test_dt_start= df[datetime_col].sort_values(ignore_index=True,ascending=True).tolist()[0]
                test_dt_end= df[datetime_col].sort_values(ignore_index=True,ascending=True).tolist()[-1]
                date_start = datetime.strptime(str(test_dt_start), '%Y%m%d')
                date_end = datetime.strptime(str(test_dt_end), '%Y%m%d')
                return (date_end- date_start).days
    ## 주차 계산 함수
    def calculate_week(date, base_date, base_week):
            base_date_timestamp = pd.Timestamp(base_date)

            # 날짜 차이 계산
            delta_days = (date - base_date_timestamp).dt.days

            # 기준 주차에서 날짜 차이를 주 단위로 변환
            week = base_week + delta_days // 7
            return week
    
class DataAcquisition():
    def selenium_APIdata_get(endpoint_base,encode_key,pageNum=1,Rows=1):
        from urllib.parse import urlencode,unquote
        decode_key ="w1N+WdpiUt4yMy2JifOenamzNXc6HCceZ596C21rNM+LICP2KiUHN0E0F3Zf4Yu13zM8Myc/ZtIzgFBcywyxXQ=="
        queryString ="?"+urlencode(
            {
                "serviceKey":unquote(f"{encode_key}"),
                "pageNo":1,
                "numOfRows":1,
                "resultType":"json",
                
            }
        )
        query_URL = endpoint_base+queryString
        # !pip install selenium
        # !pip install webdriver-manager
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.common.by import By
        import json
        from pprint import pprint
        # Chrome browser  와 Chrome Driver Version 확인하기 
        chrome_options = webdriver.ChromeOptions()

        hrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 헤드리스 모드 활성화
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(query_URL)
        data =driver.find_element(By.XPATH,'/html/body/pre').text
        data_json = json.loads(data)

        pprint(data_json["response"])
    
    def request_APIData_get():
        ## Author : 지환 팍
        import requests
        import logging
        import ssl
        import pandas as pd
        from requests.adapters import HTTPAdapter
        from requests.packages.urllib3.util.ssl_ import create_urllib3_context

        # 로깅 설정
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # SSL 컨텍스트 생성
        ctx = create_urllib3_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')

        # 커스텀 어댑터 클래스 정의
        class CustomAdapter(HTTPAdapter):
            def init_poolmanager(self, *args, **kwargs):
                kwargs['ssl_context'] = ctx
                return super(CustomAdapter, self).init_poolmanager(*args, **kwargs)

        # 세션 생성 및 어댑터 설정
        session = requests.Session()
        session.mount('https://', CustomAdapter())

        # API 엔드포인트 URL
        url = "https://apis.data.go.kr/B190001/cardFranchisesV3/cardV3"

        # 인증키
        api_key = "1gpaK4ticgtOqnE5t7cIOQtKz7kP4Lu3HbyACKUWni5Ag/yj9cl9uueNXK20lnGIEqPnYSMiSOmR61YL9xS40g=="

        # 요청 파라미터
        params = {
            "serviceKey": api_key,
            "page": "1",
            "perPage": "3000"
        }

        # 요청 헤더
        headers = {
            "accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }

        try:
            # GET 요청 보내기
            response = session.get(url, params=params, headers=headers, timeout=30)
            
            # 응답 상태 확인
            response.raise_for_status()
            
            # JSON 형식으로 데이터 파싱
            data = response.json()
            
            # 데이터 추출 및 DataFrame 생성
            items = data.get('data', [])
            if items:
                df = pd.DataFrame(items)
                logging.info("DataFrame 생성 완료")
                logging.info(f"DataFrame shape: {df.shape}")
                logging.info("\nDataFrame 첫 5행:")
                logging.info(df.head().to_string())
            else:
                logging.warning("추출된 데이터 항목이 없습니다.")
                logging.info("응답 데이터:")
                logging.info(json.dumps(data, indent=2, ensure_ascii=False))

        except requests.exceptions.RequestException as e:
            logging.error(f"요청 중 오류 발생: {e}")
            if hasattr(e, 'response') and e.response is not None:
                logging.error(f"응답 상태 코드: {e.response.status_code}")
                logging.error(f"응답 내용: {e.response.text}")
            else:
                logging.error("응답 객체가 없습니다.")
        except ValueError as e:
            logging.error(f"JSON 디코딩 오류: {e}")
            logging.error(f"응답 내용: {response.text}")
        except Exception as e:
            logging.error(f"예상치 못한 오류 발생: {e}")

class Visualization():
    
    def plot_boxplots(datasets, titles, figsize=(10, 20)):
        
        import seaborn as sns
        import matplotlib.pyplot as plt
        import platform,os
        from matplotlib import font_manager, rc
        

        # 시각화 설정
        plt.style.use("seaborn-v0_8")
        plt.rcParams['axes.unicode_minus'] = False
        
        # 시스템에 따른 폰트 설정
        if platform.system() == 'Darwin': 
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows': 
            path = 'c:/Windows/Fonts/malgun.ttf' 
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            print("Unknown System")

        # 그래프 그리기
        fig, axes = plt.subplots(len(datasets), 1, figsize=figsize)  # 데이터셋 개수에 따라 서브플롯 생성

        for i, data in enumerate(datasets):
            sns.boxplot(data=data, ax=axes[i])
            axes[i].set_title(titles[i])

        # 그래프 간격 조절
        plt.tight_layout()

        # 그래프 출력
        plt.show()
        # 함수 사용 예시
        # datasets = [out, B, C, D, E]
        # titles = ['사전테스트 생육데이터', '환경 데이터 B', '환경 데이터 C', '환경 데이터 D', '환경 데이터 E']
        # plot_boxplots(datasets, titles)

class ModelTest():
    # 예시 데이터 (training_table과 target_table이 이미 존재한다고 가정)
    # training_table = pd.DataFrame(...)
    # target_table = pd.DataFrame(...)

    # 데이터 분할
    def real_pred_compare(predictions,test_target,test_input):
        print(yellow("🔸🔸🔸🔸🔸🔸[[실제 예측값 확인]]🔸🔸🔸🔸🔸🔸"))
        for idx,(pred_result,real,test_in) in enumerate(zip(predictions,test_target.values,test_input.values)):
            if idx < 4:
                str_real = "\t"
                str_pred = "\t"
                str_input = "\t"
                for i in list(real):
                    str_real = "\t".join("{:>8d}".format(int(val)) for val in real)
                for j in list(map(int,(pred_result))):
                    str_pred = "\t".join("{:>8d}".format(int(val)) for val in pred_result)
                for k in list(test_in):
                    str_input += str(k) + "\t"

                
                print(f"***** {idx} 번째 test 결과 ***** ")
                print("인풋 정보"+"---"*200)
                print(f"인풋칼럼","\t".join((list(test_input.columns))),sep = "\t\t")
                print(f"***인풋\t  {str_input}", sep='\t')
                print("아웃풋 정보"+"---"*200)
                print(f"  ","\t".join((list(test_target.columns))),sep = "\t\t")
                formatted_columns = "\t".join("{:>8s}".format(col) for col in list(test_target.columns))
                print(f"    \t{formatted_columns}")
                print(f"실제\t  {str_real}", sep='\t')
                print(f"예측\t  {str_pred}", sep='\t')

    def linear_regressor_prdict(train_input, train_target, test_input, test_target):
        from statistics import LinearRegression
        import numpy as np
        from sklearn.multioutput import MultiOutputRegressor
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn.model_selection import cross_val_score
        import joblib

        ## Linear Regression model 비교
        lin_regressor = LinearRegression()
        multi_output_regressor_lin = MultiOutputRegressor(lin_regressor)
        multi_output_regressor_lin.fit(train_input, train_target)
        y_pred_lin = multi_output_regressor_lin.predict(test_input)
        mse = mean_squared_error(test_target, y_pred_lin)
        rmse = np.sqrt(mse)
        r2 = r2_score(test_target, y_pred_lin) 
        
        #### 교차검증 
        scores_cv = cross_val_score(multi_output_regressor_lin,train_input,train_target,scoring='neg_mean_squared_error',cv=10)
        rmse_cv = np.sqrt(-scores_cv)
        print(f"Linear regression model RMSE: {rmse:.2f}")
        print(f"Linear regression model R2 score: {r2:.2f}")
        print("\t ",f"LR cv score : {rmse_cv}")
        print("\t ",f"LR cv RMSE  average : {rmse_cv.mean():.2f}")
                # 모델 저장
        joblib.dump(multi_output_regressor_lin, "Linear_model")
        print(f'모델이 {"Linear_model"} 이름으로 저장됨')
        predictions = multi_output_regressor_lin.predict(test_input)
        ModelTest.real_pred_compare(predictions,test_target,test_input)

    def knn_regressor_predict(train_input, train_target, test_input, test_target, multi_out=True):
        ### Description: multiioutput 일때와 single output 일 때 구분해서 학습하도록 함. 
        ### Date : 2024.08.29 
        
        import numpy as np
        from sklearn.multioutput import MultiOutputRegressor
        from sklearn.neighbors import KNeighborsRegressor
        from sklearn.metrics import mean_squared_error
        from xgboost import XGBRegressor
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn.model_selection import cross_val_score
        import joblib

        ## KNN regression model
        knn_regressor = KNeighborsRegressor(n_neighbors=3)

        if multi_out:
            ## Multi Output Setting
            multi_output_regressor_knn = MultiOutputRegressor(knn_regressor)
            multi_output_regressor_knn.fit(train_input, train_target)
            score = multi_output_regressor_knn.score(test_input, test_target)
            y_pred_knn = multi_output_regressor_knn.predict(test_input)
            mse = mean_squared_error(test_target, y_pred_knn)
            rmse = np.sqrt(mse)
            # R2 스코어 계산
            r2 = r2_score(test_target, y_pred_knn)
            print(yellow(f'KNN(k=3) regression model score: {score}'))
            print(yellow(f'KNN(k=3) regression model RMSE: {rmse:.2f}'))
            print(yellow(f'KNN regression R2 score: {r2:.2f}'))
            #### 교차검증 
            scores_cv = cross_val_score(multi_output_regressor_knn, train_input, train_target, scoring='neg_mean_squared_error', cv=10)
            rmse_cv = np.sqrt(-scores_cv)
            print(rainbow_orange(f" ◉ KNN Cross Validation score : {rmse_cv}"))
            print(rainbow_orange(f" ◉ KNN Cross Validation RMSE average : {rmse_cv.mean():.2f}"))
            # 모델 저장
            joblib.dump(multi_output_regressor_knn, "KNN_model")
            print(f'모델이 {"KNN_model"} 이름으로 저장됨')
            predictions = multi_output_regressor_knn.predict(test_input)

        else:  # multi_out이 False일 경우
            knn_regressor.fit(train_input, train_target)  # KNeighborsRegressor를 학습
            score = knn_regressor.score(test_input, test_target)
            y_pred_knn = knn_regressor.predict(test_input)
            mse = mean_squared_error(test_target, y_pred_knn)
            rmse = np.sqrt(mse)
            # R2 스코어 계산
            r2 = r2_score(test_target, y_pred_knn)
            print(yellow(f' ◉ KNN(k=3) regression model score: {score:.2f}'))
            print(yellow(f' ◉ KNN(k=3) regression model RMSE: {rmse:.2f}'))
            print(yellow(f' ◉ KNN regression R2 score: {r2:.2f}'))
            #### 교차검증 
            scores_cv = cross_val_score(knn_regressor, train_input, train_target, scoring='neg_mean_squared_error', cv=10)
            rmse_cv = np.sqrt(-scores_cv)
            print(rainbow_orange(f" ◉ KNN Cross Validation RMSE : "))
            for order,i in enumerate(rmse_cv):
                if order ==0:
                    print("    : ",end="")
                print(f" {i:.3f} ",end=", ")
            else: print()
            print(rainbow_orange(f" ◉ KNN Cross Validation RMSE average : {rmse_cv.mean():.2f}"))
            # 모델 저장
            joblib.dump(knn_regressor, "KNN_model")
            print(f'모델이 {"KNN_model"} 이름으로 저장됨')
            predictions = knn_regressor.predict(test_input)

    def xgboost_regressor_predict(train_input, train_target, test_input, test_target, multi_out=True):
        """
        XGBoost 회귀 모델을 학습하고 예측합니다. 

        Args:
            train_input (pd.DataFrame): 학습 데이터의 입력 특성
            train_target (pd.Series): 학습 데이터의 목표 값
            test_input (pd.DataFrame): 테스트 데이터의 입력 특성
            test_target (pd.Series): 테스트 데이터의 목표 값
            multi_out (bool, optional): 여러 출력 값을 예측할지 여부. 기본값은 True입니다.

        Returns:
            None: 결과를 출력하고 모델을 저장합니다.
        """

        import numpy as np
        from sklearn.multioutput import MultiOutputRegressor
        from sklearn.metrics import mean_squared_error
        from xgboost import XGBRegressor
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn.model_selection import cross_val_score
        import joblib

        # xg_reg = XGBRegressor(enable_categorical=True)
        xg_reg = XGBRegressor(enable_categorical=True, feature_names=train_input.columns[:-1]) # feature_names 설정
        # 데이터 타입 변환 (필요에 따라)
        for col in train_input.columns:
            if col == 'Smiles':  # SMILES 컬럼은 제외
                continue
            train_input[col] = train_input[col].astype(int)  # 모든 열을 int 타입으로 변환 (필요에 따라 다른 타입으로 변환)
            test_input[col] = test_input[col].astype(int)  # test_input도 마찬가지로 변환

        if multi_out:
            # 여러 출력 값 예측 설정
            multi_output_regressor_xg = MultiOutputRegressor(xg_reg)
            multi_output_regressor_xg.fit(train_input, train_target)

            score = multi_output_regressor_xg.score(test_input, test_target)
            y_pred_xg = multi_output_regressor_xg.predict(test_input)
            mse = mean_squared_error(test_target, y_pred_xg)
            rmse = np.sqrt(mse)
            # R2 스코어 계산
            r2 = r2_score(test_target, y_pred_xg)   
            print(yellow(f' ◉ XGB regression model score: {score:.2f}'))
            print(yellow(f' ◉ XGBoost(3) regression model RMSE: {rmse:.2f}'))
            print(yellow(f' ◉ XGBoost regression model R2 score: {r2:.2f}'))
            ### 교차검증
            scores_cv = cross_val_score(multi_output_regressor_xg, train_input, train_target, scoring='neg_mean_squared_error', cv=10)
            rmse_cv = np.sqrt(-scores_cv)
            # 모델 저장
            joblib.dump(multi_output_regressor_xg, "XG_model")
            print(f'모델이 {"XG_model"} 이름으로 저장됨')
            print(rainbow_orange(f" ◉ XGB Cross Validation RMSE : "))
            for order, i in enumerate(rmse_cv):
                if order == 0:
                    print("    : ", end="")
                print(f" {i:.3f} ", end=", ")
            else:
                print()
            print(rainbow_orange(f" ◉ XGB Cross Validation RMSE average : {rmse_cv.mean():.2f}"))
            predictions = multi_output_regressor_xg.predict(test_input)

        else:
            # 단일 출력 값 예측
            xg_reg.fit(train_input, train_target)

            score = xg_reg.score(test_input, test_target)
            y_pred_xg = xg_reg.predict(test_input)
            mse = mean_squared_error(test_target, y_pred_xg)
            rmse = np.sqrt(mse)
            # R2 스코어 계산
            r2 = r2_score(test_target, y_pred_xg)
            print(yellow(f' ◉ XGB regression model score: {score:.2f}'))
            print(yellow(f' ◉ XGBoost(3) regression model RMSE: {rmse:.2f}'))
            print(yellow(f' ◉ XGBoost regression model R2 score: {r2:.2f}'))
            ### 교차검증
            scores_cv = cross_val_score(xg_reg, train_input, train_target, scoring='neg_mean_squared_error', cv=10)
            rmse_cv = np.sqrt(-scores_cv)
            # 모델 저장
            joblib.dump(xg_reg, "XG_model")
            print(f'모델이 {"XG_model"} 이름으로 저장됨')
            print(rainbow_orange(f" ◉ XGB Cross Validation RMSE : "))
            for order, i in enumerate(rmse_cv):
                if order == 0:
                    print("    : ", end="")
                print(f" {i:.3f} ", end=", ")
            else:
                print()
            print(rainbow_orange(f" ◉ XGB Cross Validation RMSE average : {rmse_cv.mean():.2f}"))
            predictions = xg_reg.predict(test_input)

        # ModelTest.real_pred_compare(predictions, test_target, test_input)

    def randomforest_regressor_predict(train_input, train_target, test_input, test_target):
        import numpy as np
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.multioutput import MultiOutputRegressor
        from sklearn.metrics import mean_squared_error
        from xgboost import XGBRegressor
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn.model_selection import cross_val_score
        import joblib
        import os

        rf_reg = RandomForestRegressor(n_estimators=1, random_state=42)
        multi_output_regressor_rf = MultiOutputRegressor(rf_reg)
        multi_output_regressor_rf.fit(train_input, train_target)

        y_pred_rf = multi_output_regressor_rf.predict(test_input)
        mse = mean_squared_error(test_target, y_pred_rf)
        rmse = np.sqrt(mse)
        r2 = r2_score(test_target, y_pred_rf)

        print(yellow(f'RandomForest regression model RMSE: {rmse:.2f}'))
        print(f'RandomForest regression model R2 score: {r2:.2f}')

        # 교차 검증
        scores_cv = cross_val_score(multi_output_regressor_rf, train_input, train_target, 
                                    scoring='neg_mean_squared_error', cv=10)
        rmse_cv = np.sqrt(-scores_cv)
        print("\t ", red(f"RF cv RMSE scores: {rmse_cv}"))
        print("\t ", green(f"RF cv RMSE average: {rmse_cv.mean():.2f}"))

        # R2 교차 검증
        r2_scores_cv = cross_val_score(multi_output_regressor_rf, train_input, train_target, 
                                    scoring='r2', cv=10)
        print("\t ", red(f"RF cv R2 scores: {r2_scores_cv}"))
        print("\t ", green(f"RF cv R2 average: {r2_scores_cv.mean():.2f}"))

        # 모델 저장
        joblib.dump(multi_output_regressor_rf, "RF_model")
        print(f'모델이 {"RF_model"} 이름으로 저장됨')

        predictions = multi_output_regressor_rf.predict(test_input)
        ModelTest.real_pred_compare(predictions, test_target, test_input)


    
if __name__ == "__main__":
    import pandas as pd ,sys
    input_data = pd.read_csv('/Users/forrestdpark/Desktop/PDG/Python_/BerryMLcompetetion/BerryMachineLearning/예선연습_2023_tomato/Data/2023_smartFarm_AI_hackathon_dataset.csv')
    while True : 
        yellow("프로그램 시작")
        # DataPreprocessing.plotSetting()
        DataPreprocessing.dataInfo(input_data)
        print(green("다시 실행하시겠습니니까?(yes =1, no=0): "))
        restart_query = int(sys.stdin.readline())
        if restart_query == 0:
            break     
    
