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
### Common  library install 
# !pip install numpy
# !pip install matplotlib
# !pip install pandas

def Analysis_title(Title):
    random_imoticon = ["🙀","👻","😜","🤗","🙄","🤑","🤖"]
    import numpy as np
    import random
    imo = random_imoticon[random.randrange(1,len(random_imoticon))]
    print(rainbow_green(f"✻✻✻✻______{imo*1} {Title} {imo*1}______✻✻✻✻",True))

def df_display_centered(df):
    from IPython.display import display, HTML
    display(HTML('<div style="text-align: center; margin-left: 50px;">{}</div>'.format(df.to_html().replace('<table>', '<table style="margin: 0 auto;">'))))
class DataPreprocessing:
    def __init__(self) -> None:
        pass
    
    def key_selector(data_dict,num=0):

        data_num= sorted(data_dict.keys())[num]
        
        return data_dict[data_num]
    
    def data_fetch(data_folder_path,start,end):
        import os,pandas as pd
        from tqdm import tqdm  # 진행 상황 표시 라이브러리
        data_dict ={}
        count = 1
        with tqdm(total=100, desc=green("Data File 불러오는 중..",True), bar_format="{desc}:{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [elapsed: {elapsed} remaining: {remaining}]", colour='green') as pbar:
            for i in (os.listdir(data_folder_path)):
                if int(i.split(".")[0]) in range(start,end):
                    # print(int(i.split(".")[0])s)
                    data_dict[f"{i}"]= pd.read_excel(os.path.join(data_folder_path, i))
                    pbar.update(count) 
                    count +=3

            #else : 
                #for i in sorted(data_dict.keys()):print(yellow(f"  {i}"))
                

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
                    df=df[col].fillna(value=nanFillValue, inplace=True)  
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
                    
                    if len(str(label)) > 10:
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
            else:
                plt.figure(figsize=(14, 4))  # 그래프 크기 설정
                sns.barplot(x=value_counts.index, y=value_counts.values, palette="viridis") 
                plt.title(f"{col} 컬럼 값 분포",fontsize=13)  # 그래프 제목 설정
                # x축 레이블 길이가 10 글자 이상이면 ...으로 표현
                for label in plt.gca().get_xticklabels():
                    if len(label.get_text()) > 10:
                        label.set_text(label.get_text()[:10] + "...")
                plt.ylabel("개수")  # y축 레이블 설정
                plt.xticks(rotation=45)  # x축 레이블 회전
                plt.tight_layout()  # 레이블 간 간격 조정
                plt.show()  # 그래프 출력

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

    def knn_regressor_predict(train_input, train_target, test_input, test_target):
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
        ## Multi Output Setting
        multi_output_regressor_knn = MultiOutputRegressor(knn_regressor)
        multi_output_regressor_knn.fit(train_input, train_target)

        score = multi_output_regressor_knn.score(test_input, test_target)
        y_pred_knn = multi_output_regressor_knn.predict(test_input)
        mse = mean_squared_error(test_target, y_pred_knn)
        rmse = np.sqrt(mse)
        # R2 스코어 계산
        r2 = r2_score(test_target, y_pred_knn)
        print(yellow(f'KNN(3) regression model score: {score}'))
        print(f'KNN(3) regression model RMSE: {rmse:.2f}')
        print(f'KNN regression model R2 score: {r2:.2f}')
        #### 교차검증 
        scores_cv = cross_val_score(multi_output_regressor_knn,train_input,train_target,scoring='neg_mean_squared_error',cv=10)
        rmse_cv = np.sqrt(-scores_cv)
        print("\t ",f"KNN cv score : {rmse_cv}")
        print("\t ",f"KNN cv RMSE average : {rmse_cv.mean():.2f}")
        # 모델 저장
        joblib.dump(multi_output_regressor_knn, "KNN_model")
        print(f'모델이 {"KNN_model"} 이름으로 저장됨')
        predictions = multi_output_regressor_knn.predict(test_input)

        ModelTest.real_pred_compare(predictions,test_target,test_input)

    def xgboost_regressor_predict(train_input, train_target, test_input, test_target):
        import numpy as np
        from sklearn.multioutput import MultiOutputRegressor
        from sklearn.metrics import mean_squared_error
        from xgboost import XGBRegressor
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn.model_selection import cross_val_score
        import joblib

        xg_reg = XGBRegressor()
        multi_output_regressor_xg = MultiOutputRegressor(xg_reg)
        multi_output_regressor_xg.fit(train_input, train_target)

        score = multi_output_regressor_xg.score(test_input, test_target)
        y_pred_xg = multi_output_regressor_xg.predict(test_input)
        mse = mean_squared_error(test_target, y_pred_xg)
        rmse = np.sqrt(mse)
        # R2 스코어 계산
        r2 = r2_score(test_target, y_pred_xg)
        print(yellow(f'XGB regression model score: {score}'))
        print(f'XGBoost(3) regression model RMSE: {rmse:.2f}')
        print(f'XGBoost regression model R2 score: {r2:.2f}')
        ### 교찯검증
        scores_cv = cross_val_score(multi_output_regressor_xg,train_input,train_target,scoring='neg_mean_squared_error',cv=10)
        rmse_cv = np.sqrt(-scores_cv)
        # 모델 저장
        joblib.dump(multi_output_regressor_xg, "XG_model")
        print(f'모델이 {"XG_model"} 이름으로 저장됨')
        print("\t ",f"XGB cv score : {rmse_cv}")
        print("\t ",f"XGB cv RMSE average : {rmse_cv.mean():.2f}")
        predictions = multi_output_regressor_xg.predict(test_input)
        ModelTest.real_pred_compare(predictions,test_target,test_input)

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
    
