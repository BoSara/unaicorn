def rfc_heart_model(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    import pickle
    x = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    randomforest = pickle.load(open('heart_disease.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction == 1:
    	return "He May have Heart Disease !!!"
    else:
    	return "He is Fine !!!"
    return prediction