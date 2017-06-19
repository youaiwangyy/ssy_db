#database util
#-*- coding:UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



def session(addr, database):
    #校验参数, 失败返回参数异常
    __username = "root"
    __password = "root"
    __host = "localhost"
    __port = 3306
    __database = "wangyy_python"
    if not addr.strip() or not database.strip():
        return getSession(__username, __password, __host, __port, __database)
    elif('dev' == addr):#dev
        __username = "mysqlsiud"
        __password = "mysql!@#456"
        __host = "m1.mysql.lizhi.rili.com"
        __port = 3306
        __database = database
        return getSession(__username, __password, __host, __port, __database)
    elif('test' == addr):#test
        __username = "root_dev"
        __password = "root_dev_password"
        __host = "host_dev"
        __port = "port_dev"
        __database = database
        return getSession(__username, __password, __host, __port, __database)
    elif ('prod' == addr):#prod
        __username = "root_dev"
        __password = "root_dev_password"
        __host = "host_dev"
        __port = "port_dev"
        __database = database
        return getSession(__username, __password, __host, __port, __database)
    else:#default
        return getSession(__username, __password, __host, __port, __database)

def getSession(username, password, host, port, database):
    DB_CONNECT_STRING = 'mysql+mysqldb://%s:%s@%s:%d/%s?charset=utf8' %(username, password, host, port, database)
    engine = create_engine(DB_CONNECT_STRING, echo=True)
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session