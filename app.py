from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)




@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method =='POST':
        date_dep = request.form['Dep_Time']
        day_of_journey = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        month_of_journey = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        arrival_date = request.form['Arrival_Time']
        Arrival_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Arrival_minute = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        duration_hours = abs(Arrival_hour - dep_hour)
        duration_minutes = abs(Arrival_minute - dep_minute)

        Total_Stops = int(request.form['stops'])
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Airline_Jet_Airways = 1
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Indigo'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Multi_carriers'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Airline_SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Airline_Vistara'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Airline_GoAir'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Airline_Multiple_carriers_Premium_economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Airline_Jet_Airways_Business'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        elif (airline=='Airline_Vistara_Premium_economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 1
            Airline_Trujet = 0
        elif (airline=='Airline_Trujet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 1
        else:
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        source = request.form['Source']
        if (source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
        elif (source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0
        elif (source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0
        elif (source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1
        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'New_Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0

        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1

        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        model = pickle.load(open("flight_model.pkl", "rb"))

        prediction = model.predict([[Total_Stops,
                                     day_of_journey,
                                     month_of_journey,
                                     dep_hour,
                                     dep_minute,
                                     Arrival_hour,
                                     Arrival_minute,
                                     duration_hours,
                                     duration_minutes,
                                     Airline_Air_India,
                                     Airline_GoAir,
                                     Airline_IndiGo,
                                     Airline_Jet_Airways,
                                     Airline_Jet_Airways_Business,
                                     Airline_Multiple_carriers,
                                     Airline_Multiple_carriers_Premium_economy,
                                     Airline_SpiceJet,
                                     Airline_Trujet,
                                     Airline_Vistara,
                                     Airline_Vistara_Premium_economy,
                                     Source_Chennai,
                                     Source_Delhi,
                                     Source_Kolkata,
                                     Source_Mumbai,
                                     Destination_Cochin,
                                     Destination_Delhi,
                                     Destination_Hyderabad,
                                     Destination_Kolkata,
                                     Destination_New_Delhi
                                     ]])


        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)
