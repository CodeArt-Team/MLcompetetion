''' 
📌 Fucntion Description :  Data frame 의 정제를 위한 기본 정보 출력
📌 Date : 2024.06.02 
📌 Author : Forrest D Park 
📌 Update : 
    2024.08.07 by pdg : DataInfo 함수 생성

'''


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
            'magenta': '\033[95m', #보라색
            'cyan': '\033[96m',
            'white': '\033[97m',
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
        color_code = colors.get(color, colors['default'])
        bold_code = '\033[1m' if bold else ''
        reset_code = colors['reset']
        
        return f"{bold_code}{color_code}{text}{reset_code}"
def blue(str):return colored_text(str,'blue')
def yellow(str):return colored_text(str,'yellow',bold=True)
def red(str):return colored_text(str,'red',bold=True)
def green(str):return colored_text(str,'green',bold=True)
def magenta(str):return colored_text(str,'magenta')
def Explaination(title,explain):
    title =str(title).upper()
    print(colored_text(f"___ 🟡 {title}. ",'green',bold=True))
    print(colored_text(f"______ 📌 {explain}",'yellow'))

class DataPreprocessing:
    def __init__(self) -> None:
        pass
    
    def plotSetting(pltStyle="seaborn-v0_8"):
        '''
        # Fucntion Description : Plot 한글화 Setting
        # Date : 2024.06.05
        # Author : Forrest D Park 
        # update : 
        '''
        Explaination("plotSetting","matplotlibn plot 한글화 Setting")
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
        print(colored_text("___## OS platform 한글 세팅완료 ## ___",'magenta'))

    def dataInfo(df, replace_Nan=False, PrintOutColnumber = 0,nanFillValue=0, graphPlot=True):
        column_count = len(df.columns)
        row_count = len(df.index)
        nul_count  = df.isnull().sum().sum()
        value_kind_limit =10
        under_limit_columns =[]
        if PrintOutColnumber ==0 :
            PrintOutColnumber = column_count
        print(yellow(f"- column 수 : {column_count}"))
        print(df.columns)
        print(yellow(f"- row 수    : {row_count}"))
        print(yellow(f"- null 수   : {nul_count}"))
        
        
        for idx, col in enumerate(df.columns):
            if df[f"{col}"].isnull().sum():
                print(f"   => {idx}번째.[{col}]컬럼 : ",f"null {df[f'{col}'].isnull().sum()} 개,\t not null {df[f'{col}'].notnull().sum()} 개")
                ## Null data fill
                if replace_Nan : ## nan 을 0 으로 대체 
                    df=df[col].fillna(value=nanFillValue, inplace=True)  
        print(yellow("- 칼럼별 데이터 중복체크"))
        print( yellow("idx.columName |\t\t\t\t |Colum Info(dtype)|** "))
        print( "",yellow("--"*len("columIdx |\t\t\t\t **|Col(dtype)|** ")))
        for idx, col in enumerate(df.dtypes.keys()):
            if idx < PrintOutColnumber: ### -> 출력할 칼럼수 제한 
                if len(f"\t{idx}.[{col}({df.dtypes[col]})]:")<25 : ### 이쁘게 출력하기 위해 칼럼 이름 글자수 25개 이하 인것은 탭을 두번만 함. 
                    value_counts = df[col].value_counts()
                    if len(df[col].unique())<10: #중복값이 10 이하일경우 value count 출력
                        under_limit_columns.append(col)
                        print(yellow(f"{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                            red(f"{len(df[col].unique())}"),\
                            green(f"\t/{len(df[col])} ")+ "\t[uniq/raw]",\
                            blue(f"---📌값의 종류가 {value_kind_limit}개 미만 입니다. "),\
                             sep=" ")
                        ### Value count 값 분포 확인
                        print("\t\t",magenta("--"*20))
                        for order,(i,v) in enumerate(zip(value_counts.index.tolist(), value_counts.values.tolist())):
                            print(magenta(f"\t\t |-[{order}] {i} : \t{v}"))
                        print("\t\t",magenta("--"*20))
                        if graphPlot :DataPreprocessing.column_hist(df,col)

                    else: 
                        print(yellow(f"{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                        red(f"{len(df[col].unique())}"),f"\t/{len(df[col])} \t[uniq/raw]",\
                             sep=" ")
                        if graphPlot :DataPreprocessing.column_hist(df,col)

                        
                    
                else:### 이쁘게 출력하기 위해 칼럼 이름 글자수 25개 이상 인것은 탭을 두번만 함. 
                    
                    value_counts = df[col].value_counts()
                    if len(df[col].unique())<10: #중복값이 10 이하일경우 value count 출력
                        under_limit_columns.append(col)
                        print(yellow(f"{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                        red(f"{len(df[col].unique())}"),\
                        green(f"\t/{len(df[col])} ")+ "\t[uniq/raw]",\
                            blue(f"---📌값의 종류가 {value_kind_limit}개 미만 입니다. "),\
                             sep=" ")
                        print("\t\t",magenta("--"*20))
                        for order,(i,v) in enumerate(zip(value_counts.index.tolist(), value_counts.values.tolist())):
                            print(magenta(f"\t\t |-[{order}] {i} : \t{v}"))
                        print("\t\t",magenta("--"*20))
                        if graphPlot :DataPreprocessing.column_hist(df,col)


        else: 
            print(f"\t ...etc (추가로 {len(df.dtypes.keys())-PrintOutColnumber}개의 칼럼이 있습니다 )")
            print(red("\t[RESULT]"),"🙀🙀🙀"*10)
            print(yellow(f"\t🟦{value_kind_limit}개이하의 값 종류를 가지는 칼럼 "))
            # print(red(str(under_limit_columns)))
            for col in under_limit_columns:
                print("\t\t-",yellow(f"{col}:{len(df[col].unique())}: {df[col].unique().tolist()}"))
            else:
                
                print("\t",red(f"총 {len(under_limit_columns)}개"))
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
    
class ModelTest():
    print("")
    
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
    
