"""
    🔸 Team : 가나다라마바사 팀
    🔸 Date : 2024.07.30 
    🔸 Description: 사전테스트 제출 파일 
    🔸 구동방식 
        1. 환경데이터가 있는 폴더의 절대 경로를 command 에 입력합니다. 
        2. 생육데이터가 있는 폴더의 절대 경로를 command 에 입력합니다.
        3. 모델 파일이 있는 폴더의 경로를 command 에 입력합니다 
        4. output이  predictBerry.csv 파일로 저장됩니다. 
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
MLLibraryInstalls()

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
import math
import time


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

        dataB.head()

    def merge_input_output(saveFilename,input_b, input_c, input_d, input_e,output):
        from sklearn.preprocessing import MinMaxScaler
        dataB, dataC, dataD, dataE = input_b, input_c, input_d, input_e
        #컬럼이름변경
        # dataR.rename(columns={'생육주사': '주차'}, inplace=True)

            # 전체 데이터를 사용하여 피벗 테이블을 생성합니다
        # '시설아이디' 유무에 따른 row 갯수 오류 확인하기
        dataR = output

        pivot = pd.pivot_table(dataR, 
                                values='조사항목값', 
                                index=['시설아이디','생육주사', '조사일자', '표본번호'], 
                                columns='조사항목', 
                                aggfunc='first')
        # print(pivot)
        # 인덱스를 리셋합니다
        pivot = pivot.reset_index()
        
        pivot = pivot.rename(columns={'생육주사': '주차','착과수': '개화수'})

        # pivot = pivot.drop('조사항목', axis=1, errors='ignore')
        print("$$$$$$")
        print(pivot.columns)
        pivot.to_csv("pivot.csv")
        # pd.read_csv()
        # print(pivot)
        pivot = pd.read_csv("pivot.csv")
        
        print(pivot)
        # pivot.head()
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
        

        # 주차와 input 데이터만 데이터셋으로 만듬
        dataCC = dataC.iloc[: ,[2,3,4,5,6,7,10]]
        dataBB = dataB.iloc[: ,[2,3,4,5,6,7,10]]
        dataDD = dataD.iloc[: ,[2,3,4,5,6,7,10]]
        dataEE = dataE.iloc[: ,[2,3,4,5,6,7,10]]

        dataT = pd.concat([dataBB, dataCC, dataDD, dataEE], ignore_index=True)
        print(dataT)
            # 주차와 input 데이터만 데이터셋으로 만듬
        dataC2 = dataC.iloc[: ,[0,2,3,4,5,6,7,10]]
        dataB2 = dataB.iloc[: ,[0,2,3,4,5,6,7,10]]
        dataD2 = dataD.iloc[: ,[0,2,3,4,5,6,7,10]]
        dataE2 = dataE.iloc[: ,[0,2,3,4,5,6,7,10]]

        # CO2 컬럼 정규화
        datalist2 = [dataB2, dataC2, dataD2, dataE2]

        for data in datalist2:

            min_x = data['innerCO2'] - data['innerCO2'].min()
            min_max = data['innerCO2'].max() - data['innerCO2'].min()
            
            normalCO2 = min_x / min_max
            data['CO2'] = normalCO2
            

        dataE2
        dataT = pd.concat([dataB2, dataC2, dataD2, dataE2], ignore_index=True)

        dataT.rename(columns={"생육주차":"주차"}, inplace=True)



        
        dataT.rename(columns={"주차":"weeks"}, inplace=True)
        dataT.rename(columns={"farm":"시설아이디"}, inplace=True)
        pivot.rename(columns={"주차":"weeks"}, inplace=True)     
        # print(dataT)
        # dataT에서 7주차 D농가 데이터 삭제
        dataT = dataT[~((dataT['weeks'] == 7) & (dataT['시설아이디'] == 'D농가'))]

        # pivot에서 7주차 D농가 데이터 삭제
        pivot = pivot[~((pivot['weeks'] == 7) & (pivot['시설아이디'] == 'D농가'))]
        pivot = pivot.iloc[:,1:]   

        dataT[dataT['시설아이디'] == 'B농가'].iloc[:, 1:]

        farms = ['B', 'C', 'D', 'E']
        group_stats = {}

        for farm in farms:
            farm_data = dataT[dataT['시설아이디'] == f'{farm}농가'].iloc[:, 1:]
            group_stats[farm] = farm_data.groupby('weeks').agg(['sum', 'mean', 'min', 'max', 'std','var','median'])
            
            # 열 이름 변경
            group_stats[farm].columns = [f'{col[0]}_{col[1]}' for col in group_stats[farm].columns]
            
            # 인덱스 리셋 및 시설아이디 추가
            group_stats[farm] = group_stats[farm].reset_index()
            group_stats[farm]['시설아이디'] = f'{farm}농가'

        # 모든 농가의 데이터를 하나로 합치기
        result = pd.concat([group_stats[farm] for farm in farms], ignore_index=True)

        # pivot 데이터와 병합 (필요한 경우)
        result = pd.merge(pivot, result, on=['시설아이디', 'weeks'], how='inner')
        # print(result.head())
        # 결과를 CSV 파일로 저장
        result.to_csv(f'{saveFilename}.csv', index=False)
    @staticmethod
    def model_apply():
        
        import joblib

        

        print("ddd")
        print(green("3.모델이 저장된 폴더의 경로를 입력해주세요:\n"))
        model_path  = str(sys.stdin.readline().rstrip())
        model =joblib.load(os.path.join(model_path,"rfRegressor_berry.h5"))

        import h5py
        

        
        model = joblib.load(os.path.join(model_path, "rfRegressor_berry.h5"))

        # # 모델과 입력 컬럼 이름 불러오기
        # h5_filename = 'rfRegressor_berry.h5'
        # with h5py.File(h5_filename, 'r') as h5file:
        #     # 모델 불러오기
        #     rf_data = h5file['model'][()]
        #     loaded_rf = joblib.loads(rf_data.tobytes())
            
        #     # 입력 컬럼 이름 불러오기
        #     input_columns = h5file['input_columns'][()].tolist()

        # # 불러온 모델과 입력 컬럼 이름 확인
        # print("Input Columns:", input_columns)
        # print("Loaded Model:", loaded_rf)


        

        # print("input columns : ",input_columns)
        data = pd.read_csv("ML_final.csv")



        x = data[['weeks', '표본번호', 'supplyEC_sum', 'supplyEC_mean',
       'supplyEC_min', 'supplyEC_max', 'supplyEC_std', 'supplyEC_var',
       'supplyEC_median', 'supplyPH_sum', 'supplyPH_mean', 'supplyPH_min',
       'supplyPH_max', 'supplyPH_std', 'supplyPH_var', 'supplyPH_median',
       'innerCO2_sum', 'innerCO2_mean', 'innerCO2_min', 'innerCO2_max',
       'innerCO2_std', 'innerCO2_var', 'innerCO2_median', 'innerHum_sum',
       'innerHum_mean', 'innerHum_min', 'innerHum_max', 'innerHum_std',
       'innerHum_var', 'innerHum_median', 'innerTemp_sum', 'innerTemp_mean',
       'innerTemp_min', 'innerTemp_max', 'innerTemp_std', 'innerTemp_var',
       'innerTemp_median', 'innerSolar_sum', 'innerSolar_mean',
       'innerSolar_min', 'innerSolar_max', 'innerSolar_std', 'innerSolar_var',
       'innerSolar_median']]
        
        pred = model.predict(x)
        df = pd.DataFrame(pred)
        df.columns = ['관부직경','엽병장','엽수','엽장','엽폭','개화수','초장','화방 꽃수(소화수)']
        df.to_csv("predictBerry.csv",index=None)


        



        





        
    
    
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

        
        output=pd.read_excel(os.path.join(output_growth_data_folder_path,"사전테스트-생육데이터.xlsx"))


        
        ### output data Fetching 
        print(yellow("🔹 Data preprocessing Start--->"))
        ReadInputOutput.merge_input_output("ML_final",input_b, input_c, input_d, input_e,output)
        ReadInputOutput.model_apply()



# print(output.tail())
# print(input_b.tail())

# /Users/ji-hwanpark/Desktop/공모전/git/BerryMLcompetetion/BerryMachineLearning/Data/사전테스트-환경데이터
# /Users/ji-hwanpark/Desktop/공모전/git/BerryMLcompetetion/BerryMachineLearning/Data/생육데이터
# /Users/ji-hwanpark/Desktop/공모전/git/BerryMLcompetetion/BerryMachineLearning/











if __name__ == "__main__":
    ReadInputOutput.main()