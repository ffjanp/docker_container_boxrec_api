#!flask/bin/python
from flask import Flask
from flask import request
import pandas as pd
from sklearn import linear_model
import pickle
import math
from flask import render_template
# creating and saving some model
def drawn_chance(rating_diff):
    sigma= 309.1541334536843
    coefficient = 0.07355460439376074
    chance = coefficient*math.e**(-(rating_diff**2)/(2*sigma**2))
    return chance
def left_chance(rating_diff):
    chance = (1/(1+pow(10,-rating_diff/350)))*(1 - drawn_chance(rating_diff))
    return chance

def right_chance(rating_diff):
    chance = (1/(1+pow(10,rating_diff/350)))*(1 - drawn_chance(rating_diff))
    return chance
name_to_id = pickle.load( open( "boxer_name_id.p", "rb" ) )
features = pickle.load( open( "boxer_features.p", "rb" ) )

app = Flask(__name__)


@app.route('/isAlive')
def index():
    return "true"

@app.route('/prediction/api/v1.0/some_prediction', methods=['GET'])
def get_prediction():
    boxer1 = str(request.args.get('boxer_id_l'))
    boxer1 = boxer1.replace('+',' ')
    print(boxer1)
    boxer2 = str(request.args.get('boxer_id_r'))
    boxer2 = boxer2.replace('+', ' ')
    print(boxer2)
    feature3 = str(request.args.get('f3'))
    if boxer1 in name_to_id:
        id1 = name_to_id[boxer1]['boxer_id']
    else:
        return render_template('index.html',f0=0,f1=1,f2='',f3='',f4='',f5='d')
    if boxer2 in name_to_id:
        id2 = name_to_id[boxer2]['boxer_id']
    else:
        return render_template('index.html',f0=0,
                    f1=0,f2='',f3='',f4='',f5='d')
    rating1 = features[id1]['elo_rating']
    print(rating1)
    rating2 = features[id2]['elo_rating']
    print(rating2)
    difference = rating1 - rating2
    p_drawn = drawn_chance(difference)
    p_right = right_chance(difference)
    print(p_right)
    p_left = left_chance(difference)
    print(p_left)
    return render_template('index.html',f0 =
                           1,f1=boxer1,f2=boxer2,f3=p_drawn,f4=p_left,f5=p_right)
   
if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')        
    # app.run(debug=True)
