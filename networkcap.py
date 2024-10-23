from seleniumwire import webdriver  # seleniumwire를 사용함을 확인
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import selenium
print(selenium.__version__)

class TestRunner:
    def __init__(self):
        self.driver = None  # driver 초기화

    def setup_driver(self):
        chrome_options = self.get_chrome_options()
        chrome_driver_path = ChromeDriverManager().install()
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)  # Chrome driver 설정
        # self.driver.scopes = ['*']  # 모든 HTTP 요청을 캡처

    def get_chrome_options(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')  # 안전하지 않은 작업을 방지
        chrome_options.add_argument('--window-size=1280,920')  # 창 크기 설정
        chrome_options.add_argument('--disable-dev-shm-usage')  # 공유 메모리 사용 제한
        return chrome_options
    
    def test_run(self):
        # if not self.driver:
            # self.setup_driver()
        self.setup_driver()
        
        self.driver.get("https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PNC&dlyCtrCd=HK&dlyPlcCd=HKG&polNm=BUSAN+NEW+PORT,+KOREA&podNm=HONG+KONG&etd=20241112&frtAppNo=&vslCd=KMZ&vslNm=KMTC+SHIMIZU&voyNo=2411S&rteCd=KIS1&eiCatCd=O&frtResult=&reqRno=000000473452&bkgClose=N&raTsParam=&promotionChk=N&scenarioCd=&promoNo=&kmtcSpotYn=Y&kmtcPremiumNegoYn=Y&etaBookingMsg=&hongkongTsYn=&hongkongTsMsg=&detailResp2=%7B%22tsDegree%22:%220%22,%22vslNm1%22:%22KMTC+SHIMIZU%22,%22voyNo%22:%222411S%22,%22rteCd%22:%22KIS1%22,%22polNm%22:%22BUSAN+NEW+PORT,+KOREA%22,%22podNm%22:%22HONG+KONG%22,%22pod1Nm%22:%22HONG+KONG%22,%22transitTime%22:%222%EC%9D%BC+19%EC%8B%9C%EA%B0%84+%22,%22transitTime1%22:%222%EC%9D%BC+19%EC%8B%9C%EA%B0%84+%22,%22polEtbDT%22:%222024.11.11+07:00%22,%22etdDT%22:%222024.11.12+02:00%22,%22polTml%22:%22BCT24+(BUSAN+CONTAINER+TERMINAL)%22,%22polTmlCd%22:%22BCT24%22,%22etaDT%22:%222024.11.14+21:00%22,%22podTml%22:%22HIT+(Hongkong+International+Terminal)%22,%22vslNm2%22:%22%22,%22voyNo2%22:%22%22,%22rteCd2%22:%22%22,%22pod2Nm%22:%22%22,%22transitTime2%22:%22%22,%22polEtbDT2%22:%22%22,%22polTml2%22:%22%22,%22etaDT2%22:%22%22,%22podTml2%22:%22%22,%22vslNm3%22:%22%22,%22voyNo3%22:%22%22,%22rteCd3%22:%22%22,%22pod3Nm%22:%22%22,%22transitTime3%22:%22%22,%22polEtbDT3%22:%22%22,%22polTml3%22:%22%22,%22etaDT3%22:%22%22,%22podTml3%22:%22%22,%22vslNm4%22:%22%22,%22voyNo4%22:%22%22,%22rteCd4%22:%22%22,%22pod4Nm%22:%22%22,%22transitTime4%22:%22%22,%22polEtbDT4%22:%22%22,%22polTml4%22:%22%22,%22etaDT4%22:%22%22,%22podTml4%22:%22%22,%22bkgDocCls%22:%222024.11.08+14:00%22,%22bkgCgoCls%22:%222024.11.10+13:00%22,%22bkgMfCls%22:%222024.11.08+14:00%22,%22cfsCls%22:%222024.11.08+12:00%22,%22mrnNo%22:%22%22,%22apoTcnt%22:%220%22,%22callSign%22:%22D5YE8%22,%22ts%22:%22N%22,%22vslCd%22:%22KMZ%22,%22pol%22:%22PNC%22,%22pod%22:%22HKG%22,%22bkgClose%22:%22N%22,%22dtBkgYn%22:%22N%22,%22bkgVslCd%22:%22KMZ%22,%22bkgVoyNo%22:%222411S%22,%22kmtcSpotLineYn%22:%22Y%22,%22kmtcSpotUserYn%22:%22Y%22,%22kmtcSpotClosYn%22:%22N%22,%22etd%22:%2220241112%22,%22etdTm%22:%220200%22,%22eta%22:%2220241114%22,%22etaTm%22:%222100%22,%22vslNm%22:%22KMTC+SHIMIZU%22,%22polEta%22:%22202411110700%22,%22polEtd%22:%22202411120200%22,%22podTmlCd%22:%22HIT%22,%22polCtrCd%22:%22KR%22,%22podCtrCd%22:%22HK%22,%22vgmDocCls%22:%222024.11.08+14:00%22,%22frtResult%22:%22A%22,%22frtAppNo%22:%22%22,%22reqRno%22:%22000000473452%22%7D&urlOrNot=false&cntrTypCd=GP")
        time.sleep(2)

        for request in self.driver.requests:
            if request.response:
                print(f'{request.url}, 응답코드 {request.response.status_code}, 컨텐츠 유형: {request.response.headers["Content-Type"]}')
                # 응답받은 각 요청의 URL, 상태 코드, 컨텐츠 타입을 출력
    
def main():
    test_runner = TestRunner()
    test_runner.test_run()

if __name__ == '__main__':
    main()
