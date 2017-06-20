#String util
#-*- coding:UTF-8 -*-

class String:
    'String 工具类'
    def isBlank(self, source):
        return not source.strip()
    def __init__(self):
        return



StringUtil = String()

ss = ""
if StringUtil.isBlank(ss):
    print "ss is null"
else :
    print "ss not null"
