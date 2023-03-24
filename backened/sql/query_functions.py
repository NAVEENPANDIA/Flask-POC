
from backened.sql.query import CONST_INSERT, CONST_SELECT_ALL_QUERY, CONST_LOGIN, CONST_PROFILE
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
    
def connection():

    engine = create_engine('mysql://root:admin@172.17.0.2:3306/flask', poolclass = NullPool)
    conn = engine.connect()
    return conn

def run_select_all():
     # results = select_all()
    sql = text(CONST_SELECT_ALL_QUERY)
    conn = connection()
    
    #print(sql)
    result = conn.execute(sql).fetchall()
    conn.close()
    return result

def run_insert(data):
    conn = connection()
    sql = text(CONST_INSERT) 
    print(sql)
    conn.execute(sql, data)
    conn.close()
    return {'status': 'success'}


def run_select_where(data):
    
    conn = connection()
    sql = text(CONST_LOGIN)  
    results = conn.execute(sql, data)
    result_dict = [dict(u) for u in results.fetchall()] 
    conn.close()
    return result_dict[0]

def run_select_where_uid(data):
    conn = connection()
    sql = text(CONST_PROFILE)
    results = conn.execute(sql, data).first()  
    print("111", results)
    conn.close()
    return dict(results)  