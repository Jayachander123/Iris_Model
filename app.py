import pickle
from flask import Flask, request, jsonify, render_template
#import numpy as np

app = Flask(__name__)


# @app.route("/", methods =["GET", "POST"])
# def welcome():
#     return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def predict():
    try:

        if request.method == 'GET':
            return render_template('index.html')
        if request.method == "POST":
            # getting input with name = fname in HTML form
            option1 = request.form.get("param1")
            # getting input with name = lname in HTML form
            option2 = request.form.get("sepellen")
            option3 = request.form.get("sepelwidth")
            option4 = request.form.get("petallength")
            option5 = request.form.get("petalwidth")

            if option1 == 'SVM':
                model = pickle.load(open('pickle_files/model_svm.pkl', 'rb'))
            elif option1 == 'LR':
                model = pickle.load(open('pickle_files/model_lgrg.pkl', 'rb'))
            elif option1 == 'RF':
                model = pickle.load(open('pickle_files/model_rf.pkl', 'rb'))
            elif option1 == 'KNN':
                model =pickle.load(open('pickle_files/model_knn.pkl', 'rb'))

            predict_value = model.predict([[option2, option3, option4, option5]])
            predict_value = predict_value[0]
            return jsonify(f"Based on your Selected Model {option1} Sepal Length {option2} Sepal Width {option3} Petal Length {option4} and Petal Width {option5} \
             Species is {predict_value}")
    except Exception as e:
        return str(e)

    #prediction = np.array2string(model.predict(data))


if __name__ == '__main__':
    app.run(debug=True)
