import uvicorn
from fastapi import FastAPI
import pickle
app = FastAPI()
pickle_in = open("m1.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Classifier Model Deployment using FastAPI '}

@app.post('/predict')
def predict( mean_radius:float, mean_texture:float, mean_perimeter:float, mean_area:float,
        mean_smoothness:float, mean_compactness:float, mean_concavity:float,
        mean_concave_points:float, mean_symmetry:float, mean_fractal_dimension:float):
        prediction = classifier.predict([[ mean_radius, mean_texture, mean_perimeter, mean_area,
        mean_smoothness, mean_compactness, mean_concavity,
        mean_concave_points, mean_symmetry, mean_fractal_dimension]])
        if(prediction[0] == 0):
             prediction="Malignant"
        elif(prediction[0] == 1):
              prediction="Benign"
        return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
