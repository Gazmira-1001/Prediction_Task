## Fish Market

Dataset link: https://www.kaggle.com/aungpyaeap/fish-market

## Content
This dataset is a record of 7 common different fish species in fish market sales. With this dataset, I have applied Logistic Regression to classify a fish specie. 


## Installation
Use the package manager pip to install requirements.txt.

pip install -r requirements.txt

## Running
python main.py 

## Deployment
This project is deployed in Heroku

## Files 
- templates-> index.html contains the main html file where the user enters the data
- templates->result.html contains the file that would be called when the user click submit
- Procfile -is needed for deployement in Heroku
- Fish.ipynb- contains the file where I have created the model and saved .pkl file
- data.csv - fish species data
- main.py  -the file that contains flask app code
- model.pkl - is the file generated after running the algorithm on fish data
