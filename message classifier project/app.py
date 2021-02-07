# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 02:13:00 2021

@author: Saish Mendke
"""

import numpy as np
from flask import Flask, flash, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
import sys
from sklearn.ensemble import GradientBoostingClassifier
from logging import FileHandler, WARNING
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
import re
from werkzeug.utils import secure_filename
import os
#from werkzeug import secure_filename
#import dateparser
from collections import Counter
import matplotlib.pyplot as plt
plt.style.use('ggplot') 
#from sklearn.linear_model import LogisticRegression

app = Flask(__name__) #Initialize the flask App
model1 = pickle.load(open('model1.pkl', 'rb'))

#regressor = LogisticRegression()
#Fitting model with trainig data
#regressor.fit(x, y)
file_handler = FileHandler('error.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

data = pd.read_csv('Messages - Sheet1.csv')
data = data.dropna()
print('in', file=sys.stderr)
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(model1.score(count_vect.transform(X_test), y_test))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        #print('here', file=sys.stderr)
        file = request.files['myfile']
        #
        if file.filename == '':
            flash('No selected file')
        #print(file)
        #f.save(secure_filename(f.filename))
        UPLOAD_FOLDER = '/media'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        file.save(secure_filename(file.filename))
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('working fine') 
        #f.save(f.filename)
        x = open(file.filename,'r', encoding = 'utf-8') #Opens the text file into variable x but the variable cannot be explored yet
        y = x.read() #By now it becomes a huge chunk of string that we need to separate line by line
        content = y.splitlines()
        chat = content
       # print(y)

        join = [line for line in chat if  "joined using this" in line] 
        
        chat = [line.strip() for line in chat]
        
        
        
        #Clean out the join notification lines
        clean_chat = [line for line in chat if not "joined using this" in line]
        
        #Further cleaning
        #Remove empty lines
        clean_chat = [line for line in clean_chat if len(line) > 1]
        
        
        
        left = [line for line in clean_chat if line.endswith("left")]
        
        
        clean_chat = [line for line in clean_chat if not line.endswith("left")]
        
        
        msgs = [] #message container
        pos = 0 #counter for position of msgs in the container
        #print(clean_chat)
        """
        Flow:
        For every line, see if it matches the expression which is starting with the format "number(s)+slash" eg "12/"
        If it does, it is a new line of conversion as they begin with dates, add it to msgs container
        Else, it is a continuation of the previous line, add it to the previous line and append to msgs, then pop previous line.
        """
        for line in clean_chat:
            if re.findall("\A\d+[/]", line):
                msgs.append(line)
                pos += 1
            else:
                take = msgs[pos-1] + ". " + line
                msgs.append(take)
                msgs.pop(pos-1)
        
        #for i in range(len(msgs)): 
         #   print(msgs[i])
         
        
        time = [msgs[i].split(',')[1].split('-')[0] for i in range(len(msgs))]
        time = [s.strip(' ') for s in time] # Remove spacing
        
        
        date = [msgs[i].split(',')[0] for i in range(len(msgs))]
        
        name = [msgs[i].split('-')[1].split(':')[0] for i in range(len(msgs))]
         
        
        content = []
        for i in range(len(msgs)):
          try:
            content.append(msgs[i].split(':')[2])
          except IndexError:
            content.append('Missing Text')
        
        
        df = pd.DataFrame(list(zip(date, time, name, content)), columns = ['Date', 'Time', 'Name', 'Content'])
        
        
        df = df[df["Content"]!='Missing Text']
        df.reset_index(inplace=True, drop=True)
        
        print('in')
        print(df['Content'])
        #text = request.form['text']
        labels = []
        #print([text])
        #print(model.score(X_train_tfidf, y_train))
        for i in df['Content']:
            prediction = model1.predict(count_vect.transform([i]))
            labels.append(int(prediction[0]))
        #print(model1.predict(count_vect.transform([text])))
        #print(prediction[0])
        #print(labels) 
        #if(int(prediction[0]) == 1):
            #print('Important', file=sys.stderr) 
         #   prediction_text = 'Important'
        #elif(int(prediction[0]) == 2):
            #print('Spam', file=sys.stderr) 
         #   prediction_text = 'Spam'
        #else:
         #   prediction_text = 'Discussion'   
            
    except:
        return render_template('apology.html')
    
    #return render_template('index.html', prediction_text='The prediction of COVID-19 is {}'.format(prediction))
    return render_template('classified-messages.html', labels=labels, df=df, n=len(labels),elem=0)

if __name__ == "__main__":
    app.run(debug=True)