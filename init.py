from flask import Flask, render_template
import json
from pymongo import MongoClient
app = Flask(__name__,template_folder='./')
client = MongoClient()
db = client.localhack
@app.route('/')
def home():
    return render_template('main_page.html')
@app.route('/result_create',methods=['post'])
def create():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    city1=request.form['prefer_city1']
    city2=request.form['prefer_city2']
    city3=request.form['prefer_city3']
    education=request.form['inst']
    marks=request.form['marks']
    intern=request.form['intern']
    int_tech=request.form['tech']
    int_c_name = request.form['c_name']
    int_period = request.form['period']
    int_desc=request.form['desc']
    project=request.form['project']
    p_tech=request.form['p_tech']
    p_period = request.form['p_period']
    p_desc=request.form['p_desc']
    skills=request.form['skill']
    expertlevel=request.form['expertlevel']
    add_details=request.form['add_details']
    prefer_com=request.form['prefer_com']
    prefer_pos=request.form['prefer_pos']
    available=request.form['avl']

    collection1 = db.Student
    p_id = collection1.insert_one({'name': name,'email':email,'phone':phone,'city1': city1,'city2': city2,'city3': city3,'education': education,'marks': marks,'intern': intern,'int_tech': int_tech,'int_c_name': int_c_name,'int_period': int_period,'int_desc': int_desc,'project': project,'p_tech': p_tech,'p_period': p_period,'int_tech': int_tech,'p_desc': p_desc,'skills': skills,'expertlevel': expertlevel,'add_details': add_details,'prefer_com': prefer_com,'prefer_pos': prefer_pos,'available': available,}).inserted_id


@app.route('/result_com',methods=['post'])
def com():
    com_name=request.form['com_name']
    website=request.form['website']
    year=request.form['year']
    com_desc=request.form['com_desc']
    pos_avl=request.form['pos_avl']
    pos_desc=request.form['pos_desc']
    pos_time=request.form['pos_time']
    pos_place=request.form['pos_place']
    skill_required=request.form['skill']

    collection2 = db.company
    pid = collection2.insert_one({'com_name': com_name , 'website': website, 'year':year , 'com_desc':com_desc , 'pos_avl':pos_avl , 'pos_desc': pos_desc, 'pos_time': pos_time, 'pos_place':pos_place , 'skill_required':  skill_required}).inserted_id
