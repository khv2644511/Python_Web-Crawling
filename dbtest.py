import pymysql

# 전역 변수 선언부
conn = None
cur = None

try:
    # MariaDB 연결 설정
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='khv032900!',
        db='pythonDB',
        charset='utf8'
    )
    cur = conn.cursor()

    # 테이블 생성 SQL
    sql = """
    CREATE TABLE IF NOT EXISTS freightTable (
        id CHAR(4) PRIMARY KEY,
        freight_charge CHAR(20),
        currency CHAR(3),
        container_type CHAR(2),
        cargo_type CHAR(10),
        rate_20 DECIMAL(10, 2),
        rate_40 DECIMAL(10, 2),
        rate_hc DECIMAL(10, 2)
    )
    """
    cur.execute(sql)
    conn.commit()
    print("freightTable 테이블이 성공적으로 생성되었습니다.")

except pymysql.MySQLError as e:
    print(f"오류가 발생했습니다: {e}")

finally:
    # 연결 종료
    if cur:
        cur.close()
    if conn:
        conn.close()
