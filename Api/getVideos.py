#!/usr/bin/env python
#coding:utf-8

from flask import Flask,jsonify,request
import pymysql

#配置信息
config={
    'host':'123.207.110.222',
    'port':3306,
    'user':'bibiziyuan',
    'password':'HpSJY8dXz7rCZX4y',
    'database':'bibiziyuan',
    'charset':'utf8'
}
#打开数据库连接
db= pymysql.connect(**config)
# 使用cursor()方法获取操作游标
cur = db.cursor()
# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
def select(f,l):
    # 数据从第f条起取l条
    sql = "select * from videos limit " + f + "," + l + ";"
    #数据得总条数
    sum = "select COUNT(*) from videos;"
    try:
        results=[]
        cur.execute(sql)  # 执行sql语句
        datas = cur.fetchall()  # 获取查询的所有记录
        cur.execute(sum)
        cont = cur.fetchone()
        print(999999,range(len(datas)))
        for i in range(len(datas)):
            results.append({
                "id":datas[i][0],
                "title":datas[i][1],
                "img_src":datas[i][2],
                "video_addr":datas[i][3],
                "director":datas[i][4],
                "performer":datas[i][5],
                "language":datas[i][6],
                "classify":datas[i][7],
                "area":datas[i][8],
                "status":datas[i][9],
                "up_date":datas[i][10],
                "release_date":datas[i][11],
                "introduce":datas[i][12],
                "is_free":datas[i][13],
                "is_vip":datas[i][14],
                "is_eg":datas[i][15]
            })
        return {'cont':cont[0],'results':results}
        # print("id","title", "img_src", "video_addr", "director","performer","language","classify","area","status","up_date","release_date","introduce","is_free","is_vip","is_eg")
    except Exception as e:
        raise e
    # finally:
        # db.close()  # 关闭连接

app = Flask(__name__)#创建一个服务，赋值给APP
@app.route('/videos',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post
#讲的是封装成一种静态的接口，无任何参数传入
def get_user():#-----这里的函数名称可以任意取
    f = request.args.get('f', '0')
    l = request.args.get('l', '10')
    results = select(f,l)

    return  jsonify(results)#把字典转成json串返回

app.run(host='0.0.0.0',port=5000,debug=False)