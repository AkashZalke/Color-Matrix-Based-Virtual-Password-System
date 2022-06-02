import re
import os.path
from flask import Flask,url_for,request
from flask.templating import render_template
from color_mapper import refresh,hex_color
from color_mapper_2 import alphabets
from class_user import user
from user_db_class import *
from authentication import *




if os.path.isfile('userbase.db') is False:
    db=Database('userbase.db')
    db.create_tables()
else:
    db=Database('userbase.db')

app = Flask(__name__)

m=refresh()
temp=m

def virtual_converter(s:str,alphabets:dict)->str:
    final=""
    for i in s:
        final=final+hex_color[alphabets[i]]
    
    return final.upper()

@app.route('/',methods=['POST','GET'])
def index():
    global temp
    if request.method=='POST':
        if request.form['submit_button'] == 'Login':
            username_content=request.form['username_login']
            pswd_content=request.form['vpswd_login'].upper()
            v_password_original_username = virtual_converter(db.display_search_book(username_content)[0][0],temp)
            if pswd_content==v_password_original_username:
                return render_template('success.html')
            else:
                return render_template('fail.html')
            

        if request.form['submit_button'] == 'Refresh':
            temp=refresh()
            return render_template('index.html',coloru=temp)
    else:
        temp=refresh()
        return render_template('index.html',coloru=temp)
        
        
@app.route('/signin',methods=['POST','GET'])
def login():
    if request.method=='POST':
        try:
            user_name=request.form['email']
            real_password=request.form['password']
            temp_user=user(user_name.upper(),real_password.upper())
            db.add_user(temp_user)
            return render_template('success_1.html')
        except:
            return render_template('success_2.html')
            
    else:
        return render_template('sign_in.html')
    
    

if __name__ == "__main__":
    
    app.run(debug=True,host='0.0.0.0')