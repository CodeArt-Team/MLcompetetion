"""
    🔸 Team : 가나다라마바사 팀
    🔸 Date : 2024.07.30 
    🔸 Requirement : 
        Requirement : 
        Scikit-Learn 1.2.2
        XGBoost 2.0.3
    🔸 Description: 사전테스트 제출 파일 
    🔸 구동방식 
        1. 환경데이터가 있는 폴더의 절대 경로를 command 에 작성합니다. 
        2. 생육데이터가 있는 폴더의 절대 경로를 command 에 작성합니다. 
    
"""
## 머신러닝을 위한 라이브러리  패키지 설치 
def MLLibraryInstalls():
    import subprocess
    import sys
    import warnings
    warnings.filterwarnings('ignore')
    def install(package):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")
    # pandas 없으면 pandas 설치
    try:
        import pandas
    except ImportError:
        print("Installing pandas")
        install('pandas')
    finally:
        try:
            import pandas as pd
        except ImportError:
            print("Failed to import pandas after installation")
    # numpy 없으면 numpy 설치
    try:
        import numpy
    except ImportError:
        print("Installing numpy")
        install('numpy')
    finally:
        try:
            import numpy as np
        except ImportError:
            print("Failed to import numpy after installation")
    # sklearn 없으면 sklearn 설치
    try:
        import sklearn
    except ImportError:
        print("Installing sklearn")
        install('scikit-learn')
    finally:
        try:
            from sklearn.tree import DecisionTreeRegressor
            from sklearn.metrics import mean_squared_error, r2_score
        except ImportError:
            print("Failed to import sklearn modules after installation")
    # matplotlib 없으면 matplotlib 설치
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Installing sklearn")
        install('matplotlib')
    finally:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("Failed to import matplotlib modules after installation")
            
    # Seaborn 없으면 Seaborn 설치
    try:
        import seaborn
    except ImportError:
        print("Installing sklearn")
        install('seaborn')
    finally:
        try:
            import seaborn
        except ImportError:
            print("Failed to import matplotlib modules after installation")
### 필요한 library package install 
# MLLibraryInstalls()
try:
    import pandas as pd,numpy as np ## pandas, numpy 
    import matplotlib.pyplot as plt,seaborn as sns  # 시각화
    import warnings; warnings.filterwarnings('ignore')  # 경고 무시
    import sys,os # file directory access
    from pprint import pprint 
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_squared_error, r2_score

    print("필요한 라이브러리 설치 및 임포트 완료")
    import platform; print(platform.platform())
    import sys; print("Python",sys.version)
    import sklearn; print("Scikit-Learn", sklearn.__version__)
    import xgboost; print("XGBoost", xgboost.__version__)
except ImportError as e:
    print(f"필요한 라이브러리 임포트에 실패했습니다: {e}")
# 기본 세팅
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
def yellow(str):return colored_text(str,'yellow')
def red(str):return colored_text(str,'red')
def green(str):return colored_text(str,'green')



class ReadInputOutput:
    @staticmethod
    def make_DayToWeek(dataB, dataC, dataD, dataE):
        from datetime import datetime, timedelta
        ## datetime date, time 분리
        datalist = [dataB, dataC, dataD, dataE]
        ## datetime을 date로 변경 
        for data in datalist:
            data['datetime'] = pd.to_datetime(data['datetime'])
            data['date'] = data['datetime'].dt.date
            data['time'] = data['datetime'].dt.hour
        
        base_dateB = datetime(2023, 10, 6)
        base_dateC = datetime(2023, 9, 22)  
        base_dateD = datetime(2023, 10, 18)  
        base_dateE = datetime(2023, 9, 22)  
        
        base_weekB = 4
        base_weekC = 1
        base_weekD = 4
        base_weekE = 1
        # 주차 계산 함수
        def calculate_week(date, base_date, base_week):
            base_date_timestamp = pd.Timestamp(base_date)
            # 날짜 차이 계산
            delta_days = (date - base_date_timestamp).dt.days

            # 기준 주차에서 날짜 차이를 주 단위로 변환
            week = base_week + delta_days // 7
            return week


        datesB = pd.to_datetime(dataB['date']) 
        datesC = pd.to_datetime(dataC['date']) 
        datesD = pd.to_datetime(dataD['date']) 
        datesE = pd.to_datetime(dataE['date']) 

        weeksB = calculate_week(datesB, base_dateB, base_weekB)
        weeksC = calculate_week(datesC, base_dateC, base_weekC)
        weeksD = calculate_week(datesD, base_dateD, base_weekD)
        weeksE = calculate_week(datesE, base_dateE, base_weekE)

        dataB['weeks'] = weeksB
        dataC['weeks'] = weeksC
        dataD['weeks'] = weeksD
        dataE['weeks'] = weeksE
    
    @staticmethod
    def main():
        print("\n")
        print(green("1.환경데이터가 존재하는 폴더의 경로를 입력해주세요 :\n"))
        input_env_data_folder_path  = str(sys.stdin.readline().rstrip())
        print(" input env data folder path : ",input_env_data_folder_path)
        if os.path.isdir(input_env_data_folder_path):
            for file in os.listdir(input_env_data_folder_path):
                # print(file)
                if file == "environmentsB.csv":
                    input_b=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input b 입력 완료")
                if file == "environmentsC.csv":
                    input_c=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input c 입력 완료")
                if file == "environmentsD.csv":
                    input_d=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input d 입력 완료")
                if file == "environmentsE.csv":
                    input_e=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input e 입력 완료")  
            else: print(" 모든 데이터를 받았습니다")
        else : print("경로를 다시 입력하세요 ")
        print(green("2.생육데이터가 존재하는 폴더의 경로를 입력해주세요 :\n"))
        output_growth_data_folder_path  = str(sys.stdin.readline().rstrip())
        if os.path.isdir(output_growth_data_folder_path):
            for file in os.listdir(output_growth_data_folder_path):
                if file =="사전테스트-생육데이터.xlsx":
                    output=pd.read_excel(output_growth_data_folder_path,file)
                    print("생육데이터를 받았습니다")
        ### output data Fetching 
        print(yellow("🔹 Data preprocessing Start--->"))
        ReadInputOutput.make_DayToWeek(input_b, input_c, input_d, input_e)
        print(" ---a")


#/Users/forrestdpark/Desktop/PDG/Python_/BerryMLcompetetion/BerryMachineLearning/Data/사전테스트-환경데이터
# /Users/forrestdpark/Desktop/PDG/Python_/BerryMLcompetetion/BerryMachineLearning/Data


if __name__ == "__main__":
    ReadInputOutput.main()