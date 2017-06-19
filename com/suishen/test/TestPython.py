#test python
#-*- coding:UTF-8 -*-

from com.suishen.util.DBUtil import session
from sqlalchemy import Integer, String, BIGINT
from com.suishen.util.StringUtil import String
def isStr(str):
    if not str.strip():
        print "addr is null"
    else:
        print "addr not null"


# if isinstance(addr, int):
#     print "true"
# else:
#     print "false"

if __name__ == '__main__':
    # sql = "SELECT t.uid FROM (SELECT temp.uid FROM (SELECT uid FROM wish WHERE uid!=0 AND status=1 GROUP BY uid HAVING COUNT(uid)>1) AS temp WHERE EXISTS (SELECT p.uid FROM stats_personal_center p WHERE p.post_count>2 AND p.uid = temp.uid)) AS t"
    # session = session("dev", "zhwnl_community")
    # uids = session.execute(sql)
    # print uids
    # for uid in uids:
    #     print uid
    # session.commit()
    # session.close()

    print "123"
