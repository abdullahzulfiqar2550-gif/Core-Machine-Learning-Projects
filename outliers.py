import uvicorn
from fastapi import FastAPI
import pickle
app= FastAPI()
pickle_in = open("C:\\Users\\Abdul\\OneDrive\\Documents\\Ultimate AI Mastery BootCamp\\Machine Learning\\Session 23&24\\ML_projects\\outlier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Outlier Detection Model Deployment'}

@app.post('/predict')
def predict(X1:int,X2:int):

    prediction = classifier.predict([[X1,X2]])
    if (prediction[0] == 1):
        prediction="Not an Outlier"
    elif (prediction[0] == -1):
        prediction=" Outlier"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
