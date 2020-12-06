#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = (net_worths-predictions)**2 # calcula Squared Errors
    cleaned_data = zip(ages,net_worths,errors) # arma lista de tuplas
    # reorderno cleaned_data segun la 3era columna (errors) con orden descendente
    cleaned_data = sorted(cleaned_data,key=lambda x:x[2], reverse=True)
    # defino el limite 10% para luego quitarlo
    limit = int(len(net_worths)*0.1)
    
    # Devuelvo todo menos el primer 10% de los datos
    return cleaned_data[limit:]

