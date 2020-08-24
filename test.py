# -*- coding: utf-8 -*-
import cx_Oracle as cx      #导入模块
con = cx.connect('positever', '152500', '127.0.0.1:1521/POSITEVER')  #创建连接
cursor = con.cursor()       #创建游标
cursor.execute("select * from FIELD_A")  #执行sql语句
data = cursor.fetchall()        #获取一条数据
print(data)     #打印数据
cursor.close()  #关闭游标
con.close()     #关闭数据库连接