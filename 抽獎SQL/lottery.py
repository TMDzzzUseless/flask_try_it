# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:56:37 2024

@author: a66
"""

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # lang=request.headers.get('accept-language')
    # if lang.startswith('en'):    
    #     return 'hellow world'
    # else:
    #     return '你好'
    
@app.route('/getsum')
def  getsum():
    max_no=request.args.get('max',100)
    min_no=request.args.get('min',1)
    sum_no=int(max_no)+int(min_no)
    return '結果'+str(sum_no)

@app.route('/twosum')
def two_sum():
    sum1=request.args.get("sum1","")
    sum2=request.args.get("sum2","")
    ans=str(int(sum1)+int(sum2))
    return  render_template('ans.html',data=ans)

app.debug=True
app.run()