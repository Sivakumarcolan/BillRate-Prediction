from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
import pickle 
import json
from utils import *

def pickle_reader(path):
    with open(path,'rb') as f:
        encoder = pickle.load(f)
        f.close()
    return encoder

def json_reader(path):
    with open(path,'r') as f:
        Json = json.load(f)
        f.close()
        return Json

model_loader = {1:'Models\Full Data\model_Yearly.pkl',2:'Models\Full Data\model_Quarterly.pkl',3:'Models\Full Data\model_Monthly.pkl',4:'Models\Full Data\model_weekly.pkl',5:'Models/Full Data/model_Daily.pkl'}
encoders_loader = {1:'Models\Full Data\encoders_Yearly.pkl',2:'Models\Full Data\encoders_Quarterly.pkl',3:'Models\Full Data\encoders_Monthly.pkl',4:'Models\Full Data\encoders_weekly.pkl',5:'Models/Full Data/encoders_Daily.pkl'}
metrics_loader = {1:'Models\Full Data\metrics_Yearly.json',2:'Models\Full Data\metrics_Quarterly.json',3:'Models\Full Data\metrics_Monthly.json',4:'Models\Full Data\metrics_weekly.json',5:'Models/Full Data/metrics_Daily.json'}



# def model_prediction_1_1(user_input):
#     encoders = pickle_reader('Models\Iteration 1\encoders.pkl')
#     model = pickle_reader('Models\Iteration 1\model.pkl')
    


def model_prediction_all(user_input,id):
    encoders = pickle_reader(encoders_loader[id])
    model = pickle_reader(model_loader[id])
    json_ = json_reader(metrics_loader[id])
    year, else_ = convert_date_to_year(user_input['date'],id)
    _ , shiftType = convert_time_to_shift(user_input['fromTime'] , user_input['toTime'])
    if else_ is None:
        data = [shiftType,year]
        
    else:
        data = [shiftType,else_,year]
    data += encoders['Organization'].transform([[user_input['Organization']]]).toarray().tolist()[0]
    data += encoders['Location'].transform([[user_input['Location']]]).toarray().tolist()[0]
    data += encoders['Department'].transform([[user_input['Department']]]).toarray().tolist()[0]
    data += encoders['Skill'].transform([[user_input['Skill']]]).toarray().tolist()[0]
    # json_ = json_reader(f'Models\Iteration 1\metrics.json')
    mae = json_['Test']['MAE']
    print(data)
    # print(data)
    return mae, model.predict([data])[0] , json_['Train']['length'] , json_['Test']['length']