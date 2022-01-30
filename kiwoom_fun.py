from pykiwoom.kiwoom import *
from datetime import datetime


kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
# accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
# user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
# user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
# keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
# firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부

# kospi = kiwoom.GetCodeListByMarket('0')
# kosdaq = kiwoom.GetCodeListByMarket('10')
# etf = kiwoom.GetCodeListByMarket('8')

# state = kiwoom.GetConnectState()

# name = kiwoom.GetMasterCodeName(kospi[0])

# state = kiwoom.GetConnectState()

# if state == 0:
#     print("미연결")
# elif state == 1:
#     print("연결완료")

# stock_cnt = kiwoom.GetMasterListedStockCnt("005930")

# 감리구분 = kiwoom.GetMasterConstruction("005930")

# 상장일 = kiwoom.GetMasterListedStockDate("005930")

# # 조건식을 PC로 다운로드
# kiwoom.GetConditionLoad()

# # 전체 조건식 리스트 얻기
# conditions = kiwoom.GetConditionNameList()

# # 0번 조건식에 해당하는 종목 리스트 출력
# condition_index = conditions[0][0]
# condition_name = conditions[0][1]
# codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

# accounts = kiwoom.GetLoginInfo("ACCNO")
# stock_account = accounts[0]

# # 삼성전자, 10주, 시장가주문 매수
# kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")
