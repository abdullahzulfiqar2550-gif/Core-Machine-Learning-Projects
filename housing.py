import uvicorn
from fastapi import FastAPI
import pickle
app = FastAPI()
pickle_in = open("C:\\Users\\Abdul\\OneDrive\\Documents\\Ultimate AI Mastery BootCamp\\Machine Learning\\Session 23&24\\ML_projects\\regressor.pkl","rb")
model=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to UET Lahore'}

@app.post('/predict')
def predict(MedInc:int,HouseAge:int,AveRooms:int,AveBedrms:int,Population:int,AveOccup:int,Latitude:int,Longitude:int):


    prediction = model.predict([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)