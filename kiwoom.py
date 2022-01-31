from pykiwoom.kiwoom import *
import time
from datetime import datetime
import pandas as pd


kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 전종목 종목코드
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
codes = kospi + kosdaq

# 문자열로 오늘 날짜 얻기
now = datetime.now()
today = now.strftime("%Y%m%d")

# ```
# 멀티 데이터 가져오기
# ```
# df_li = []

# df = kiwoom.block_request("opt10081",
#                           종목코드="005930",
#                           기준일자="20200424",
#                           수정주가구분=1,
#                           output="주식일봉차트조회",
#                           next=0)
# df_li.append(df)

# while kiwoom.tr_remained:
#     df = kiwoom.block_request("opt10081",
#                               종목코드="005930",
#                               기준일자="20200424",
#                               수정주가구분=1,
#                               output="주식일봉차트조회",
#                               next=2)
#     df_li.append(df)
#     time.sleep(1)
    
# df = pd.concat(df_li)
# df.to_excel("data/005930.xlsx")


# 전 종목의 일봉 데이터
for i, code in enumerate(codes):
    print(f"{i}/{len(codes[3000:])} {code[3000:]}")
    df = kiwoom.block_request("opt10081",
                              종목코드=code,
                              기준일자=today,
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=0)

    out_name = f"data/{code}.xlsx"
    df.to_excel(out_name)
    time.sleep(3.6)
    
# To do
# 전 종목 존재하는 과거 데이터 전부 수집 
# (현재는 2022.01.31 기준 600일 전까지의 데이터만 존재)
