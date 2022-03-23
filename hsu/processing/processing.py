import json
import time
import threading
from flask import Flask, request, abort, make_response
from repository import workflows
from repository.models import Models
from repository.workflows import Workflows
from repository.workflow_steps import WorkflowSteps
from repository.workflow_rules import WorkflowRules
import os
import configparser
from repository import CONFIG_PATH
import pickle
import pandas as pd
import jsonpickle

class DataProcessing():
    model_repository = {}
    app = Flask(__name__)
    app.config["DEBUG"] = True
 
    def __init__(self, number):
        self.number = number
        threading.Thread.__init__(self)

    def run(self):

        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        models = Models.list_active_models()

        for model in models:
            model_path = config.get('MODELS','PATH')
            with open(model_path + model.name, 'rb') as file:
                pickle_model = pickle.load(file)
                self.model_repository[model.location_id] = pickle_model

        print("AI Listener is Running!")
        self.app.run(host='127.0.0.1', port=8000,debug=False)

    @app.route("/predict",methods=['POST'])
    def predict():
        data = request.get_json()     

        workflows = Workflows.list_active_workflows(collector_id=1)
        for work in workflows:        
            predicted = ''
            result_to_predict = pd.DataFrame(data['data'], columns=data['columns'])
            
            result_to_predict.drop(["src_ip"], axis=1, inplace=True)
            result_to_predict.drop(["dst_ip"], axis=1, inplace=True)
            result_to_predict.drop(["timestamp"], axis=1, inplace=True)

            steps = WorkflowSteps.list_steps_workflow(work.id)

            for step in steps:
                if(step.type == 1):
                    df_to_predict = DataProcessing.model_repository[step.location_id].transform(df_to_predict)
                else:
                    predicted = DataProcessing.model_repository[step.location_id].predict(df_to_predict)[0]
                
                if(predicted != ''):
                    predicted_temp[step.model_id] = predicted
                    predicted = ''

            rules = WorkflowRules.list_workflow_rules(work.id)
            predicted_decision = ''
            for rule in rules:
                if(eval(rule.condition)):
                    predicted_decision = eval(rule.model_id_value)    
                    if(rule.stop_conditions == 1):
                        break 

        return make_response(jsonpickle.encode(str(predicted_decision), unpicklable=False), 200)

    @app.route("/predictcsv",methods=['POST'])
    def predictcsv():

        results = {
            'workflow'  : [],
            'start_time': [],
            'end_time'  : [],
            'dif_time'  : [],
            'prediction' : []
        }

        data = request.get_json()   
        
        df = pd.DataFrame(data['data'], columns=data['columns'])
         
        df.drop(["src_ip"], axis=1, inplace=True)
        df.drop(["dst_ip"], axis=1, inplace=True)
        df.drop(["timestamp"], axis=1, inplace=True)

        workflows = Workflows.list_active_workflows(collector_id=1)
        
        for work in workflows:
            predicted_temp = {}
            predicted = ''
            start_time = time.time()
            results['start_time'].append(start_time)
            results['workflow'].append(work.id)
            
            df_to_predict = df

            steps = WorkflowSteps.list_steps_workflow(work.id)

            for step in steps:
                if(step.type == 1):
                    df_to_predict = DataProcessing.model_repository[step.location_id].transform(df_to_predict)
                else:
                    predicted = DataProcessing.model_repository[step.location_id].predict(df_to_predict)[0]
                
                if(predicted != ''):
                    predicted_temp[step.model_id] = predicted
                    predicted = ''

            rules = WorkflowRules.list_workflow_rules(work.id)
            predicted_decision = ''
            for rule in rules:
                if(eval(rule.condition)):
                    predicted_decision = eval(rule.model_id_value)    
                    if(rule.stop_conditions == 1):
                        break 

            end_time = time.time()
            dif_time = end_time - start_time
            results['end_time'].append(end_time)
            results['dif_time'].append(dif_time)
            results['prediction'].append(str(predicted_decision))      

        return make_response(jsonpickle.encode(results, unpicklable=False), 200)