from flask import Flask, request, Response
import json
import dbhandler as dbh
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


@app.get('/heros')
def get_heros():
    hero_list = []
    heros_json = None
    try:
        hero_list = dbh.get_heros()
        heros_json = json.dumps(hero_list, default=str)
    except:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)
    if(hero_list):
        return Response(heros_json, mimetype="application/json", status=200)
    else:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)


@app.get('/villians')
def get_villians():
    villian_list = []
    villian_json = None
    try:
        villian_list = dbh.get_villians()
        villian_json = json.dumps(villian_list, default=str)
    except:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)
    if(villian_list):
        return Response(villian_json, mimetype="application/json", status=200)
    else:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)


app.run(debug=True)
