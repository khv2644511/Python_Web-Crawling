import pymysql
import json

with open('freight_data2.json', "r") as f:
    data = json.load(f)

# with open('port.json', "r") as f:
#     port_data = json.load(f)

def insert_port_data(json, startPort):
        # 전역 변수 선언부
        conn = None
        cur = None

        # MySQL 연결 설정
        conn = pymysql.connect(host='127.0.0.1', user='root', password='khv032900!', db='pythonDB', charset='utf8')
        cur = conn.cursor()

        # create_port_info_table_sql = """
        # CREATE TABLE IF NOT EXISTS portTable (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     ctrCd VARCHAR(2),
        #     ctrEnm VARCHAR(50),
        #     lowerCtrEnm VARCHAR(50),
        #     plcCd VARCHAR(3),
        #     plcNm VARCHAR(50),
        #     plcEnm VARCHAR(50),
        #     lowerPlcEnm VARCHAR(50),
        #     plcEnmOnly VARCHAR(50),
        #     plcCatCd char(2)
        # )
        # """
        # cur.execute(create_port_info_table_sql)

        portTable=""
        # 테이블 생성
        cur.execute("""
        CREATE TABLE IF NOT EXISTS portTable(
            id INT AUTO_INCREMENT PRIMARY KEY,
            ctrCd VARCHAR(2),
            ctrEnm VARCHAR(50),
            lowerCtrEnm VARCHAR(50),
            plcCd VARCHAR(3),
            plcNm VARCHAR(100),
            plcEnm VARCHAR(255), 
            lowerPlcEnm VARCHAR(100),
            plcEnmOnly VARCHAR(100),
            plcCatCd char(2)
        )""")


           # Insert data into the table
        insert_sql = """
        INSERT INTO portTable (ctrCd, ctrEnm, lowerCtrEnm, plcCd, plcNm, plcEnm, lowerPlcEnm, plcEnmOnly, plcCatCd)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        for item in json:
            cur.execute(insert_sql, (
                item['ctrCd'],
                item['ctrEnm'],
                item['lowerCtrEnm'],
                item['plcCd'],
                item['plcNm'],
                item['plcEnm'],
                item['lowerPlcEnm'],
                item['plcEnmOnly'],
                item['plcCatCd'],
            ))
        

        conn.commit()

        # 마지막엔 무조건 close() 메소드로 db연결을 해제해야 한다.
        conn.close()

# 크롤링해서 받아온 운임데이터로부터 테이블 생성해서 데이터 넣기

def insert_data_into_db(json, startPort, destPort):
    try:
        # 전역 변수 선언부
        conn = None
        cur = None

        # MySQL 연결 설정
        conn = pymysql.connect(host='127.0.0.1', user='root', password='khv032900!', db='pythonDB', charset='utf8')
        cur = conn.cursor()

        # freightTable 테이블 생성 (없을 경우에만 생성)
        create_table_sql = f"""
        
        CREATE TABLE IF NOT EXISTS freightTable (
            id INT AUTO_INCREMENT PRIMARY KEY,
            startPort VARCHAR(20),
            destPort VARCHAR(20),
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

                ei_value = "E Charges" if item.get('frtPncCd') == 'P' else "I Charges" if item.get('frtPncCd') == 'C' else None

                # 데이터 삽입 SQL
                insert_sql = f"""
                INSERT INTO freightTable (startPort, destPort, frtCd, EI, frtCdNm, Currency, Type, cargo, rate20, rate40, rateHc)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                
                # 해당 항목이 존재하지 않을 경우 None으로 대체하여 데이터 삽입
                cur.execute(insert_sql, (
                    startPort,
                    destPort,
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
    
# insert_data_into_db(data, 'busan', 'hong')
# insert_port_data(port_data)