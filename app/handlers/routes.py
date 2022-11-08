import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

# Return true if input is valid, return error message and error code otherwise
def check_input(response):
    if (len(response) < 9):
            return "missing required arguments", 400
        
    if (len(response) > 9):
        return "too many arguments", 400
    
    if (response["reason"] != "course" and
        response["reason"] != "home" and
        response["reason"] != "other" and
        response["reason"] != "reputation"):
        return "invalid reason", 400
    
    if (not isinstance(response["studytime"], int)):
        return "invalid study time", 400
        
    
    if (not(0 < response["studytime"] < 5)):
        return "study time must be integer from 1 to 4", 400
    
    if (response["activities"] != "yes" and response["activities"] != "no"):
        return "invalid activities", 400        
    
    if(not isinstance(response["absences"], int)):
        return "invalid absences", 400
    
    if(response["higher"] != "yes" and response["higher"] != "no"):
        return "invalid higher", 400
    
    if (not(0 < response["traveltime"] < 5)):
        return "travel time must be integer from 1 to 4", 400
    
    if (not(0 < response["failures"] < 5)):
        return "failures must be integer from 1 to 4", 400
    
    if(not isinstance(response["Walc"], int)):
        return "Walc must be integer from 1 to 5", 400
    
    if(not isinstance(response["Dalc"], int)):
        return "Dalc must be integer from 1 to 5", 400
    
    if (not(0 <= response["Dalc"] < 6)):
        return "Dalc must be integer from 1 to 5", 400
    
    if (not(0 <= response["Walc"] < 6)):
        return "Walc must be integer from 1 to 5", 400
    
    return True
    

def configure_routes(app):
    
    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        # Generate Input
        response = request.json
        
        if (check_input(response) != True):
            return check_input(response)
        
        query_df = pd.DataFrame({
            "Dalc": pd.Series(response["Dalc"]),
            "Walc": pd.Series(response["Walc"]),
            "absences":pd.Series(response["absences"]),
            "activities_no": pd.Series(1 if response["activities"] == "no" else 0),
            "activities_yes": pd.Series(1 if response["activities"] == "yes" else 0),
            "failures": pd.Series(response["failures"]),
            "higher_no": pd.Series(1 if response["higher"] == "no" else 0),
            "higher_yes": pd.Series(1 if response["higher"] == "yes" else 0),
            "reason_course": pd.Series(1 if response["reason"] == "course" else 0),
            "reason_home": pd.Series(1 if response["reason"] == "home" else 0),
            "reason_other": pd.Series(1 if response["reason"] == "other" else 0),
            "reason_reputation": pd.Series(1 if response["reason"] == "reputation" else 0),
            "studytime": pd.Series(response["studytime"]),
            "traveltime": pd.Series(response["traveltime"])
        })
        
        prediction = clf.predict_proba(query_df)
        return jsonify((prediction[0][1] * 20))


    @app.route('/get-decision')
    def get_decision():
        response = request.json["score"]
        if (not (isinstance(response, int) or isinstance(response, float))):
            return "invalid score", 400
        
        if (response < 0 or response > 20):
            return "score must be number from 0 to 20", 400
        
        if (response >= 15):
            return jsonify(1)
        
        return jsonify(0)