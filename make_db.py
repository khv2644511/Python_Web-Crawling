import pymysql
import json

with open('freight_data2.json', "r") as f:
    data = json.load(f)

def insert_data_into_db(json):
    try:
        # 전역 변수 선언부
        conn = None
        cur = None

        # MySQL 연결 설정
        conn = pymysql.connect(host='127.0.0.1', user='root', password='khv032900!', db='pythonDB', charset='utf8')
        cur = conn.cursor()

        # freightTable 테이블 생성 (없을 경우에만 생성)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS freightTable (
            id INT AUTO_INCREMENT PRIMARY KEY,
            EI VARCHAR(10),
            frtCd VARCHAR(10),
            frtCdNm VARCHAR(50),
            Currency VARCHAR(3),
            Type VARCHAR(2),
            cargo VARCHAR(2),
            rate20 DECIMAL(10, 2),
            rate40 DECIMAL(10, 2),
            rateHc DECIMAL(10, 2)
        )
        """
        cur.execute(create_table_sql)

        # JSON 데이터에서 'cntrTypCd'가 "GP"인 항목만 DB에 삽입
        for item in json['surChargeList']:
            if item.get('cntrTypCd') == "GP":
            # if item.get('cntrTypCd') == "GP" and item.get('frtCd') == "O/F":

                ei_value = "Export" if item.get('frtPncCd') == 'P' else "Import" if item.get('frtPncCd') == 'C' else None

                # 데이터 삽입 SQL
                insert_sql = """
                INSERT INTO freightTable (frtCd, EI, frtCdNm, Currency, Type, cargo, rate20, rate40, rateHc)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                
                # 해당 항목이 존재하지 않을 경우 None으로 대체하여 데이터 삽입
                cur.execute(insert_sql, (
                    item.get('frtCd'),
                    ei_value,
                    item.get('frtCdNm'),
                    item.get('curCd'),
                    item.get('cntrTypCd'),
                    item.get('cgoTypNm', None),
                    item.get('rate20', None),
                    item.get('rate40', None),
                    item.get('rateHc', None)
                ))

        # 커밋 및 연결 종료
        conn.commit()
        conn.close()

        print("데이터가 성공적으로 DB에 삽입되었습니다.")
    except Exception as e:
        print(f"cannot insert into db: {str(e)}")
    
insert_data_into_db(data)