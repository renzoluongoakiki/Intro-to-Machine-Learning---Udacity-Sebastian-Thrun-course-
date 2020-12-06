#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print "personas en el dataset:",len(enron_data)
print "#atributos para cada persona:",len(enron_data["SKILLING JEFFREY K"])

# Cuantas personas cumplen una condicion
keys=[]
for key in enron_data:
    if enron_data[key]["poi"]==True:
        keys.append(key)
print "#personas de interes en enron_data:",len(keys)
print "personas de interes:",keys

#Un dato de 1 persona
print "STOCK OPTIONS EXERCISED SKILLING",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#Un dato de varias personas
for capo in ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]:
	print capo,"Total Payments (se robo):",enron_data[capo]["total_payments"]

#Toda la info de 1 persona
print enron_data["SKILLING JEFFREY K"]

personas_con_salary = []
personas_con_email = []
for key in enron_data:
	if enron_data[key]["salary"]!="NaN":
		personas_con_salary.append(key)
	if enron_data[key]["email_address"]!="NaN":
		personas_con_email.append(key)
print "#personas con salary:",len(personas_con_salary)
print "#personas con email:",len(personas_con_email)

# contar nulos en la columna total_payments
total_payments_nan = []
for person in enron_data:
	if enron_data[person]["total_payments"]=="NaN":
		total_payments_nan.append(person)
print "#personas con total_payments='NaN':",len(total_payments_nan)


