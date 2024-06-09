import numpy as np
import pickle
import streamlit as st



# loading the saved model
loaded_model=pickle.load(open("C:/bin/coding/ML Project Fraud Detection/Trained_Model.sav","rb"))

def prediction(input_data):
    # changing input data into numpy array
    input_data_as_numpy_array=np.array(input_data)
    #Reshape the array as we are predicting for one instance
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    if (prediction[0]==0):
        return("Not Fraud")
    else :
        return("Fraud")


def main():
    # giving title
    st.title("PAYMENTS FRAUD DETECTOR")
    # Getting input from user
    step = st.text_input("Enter the Duration in Steps(1 Step = 1 Hour)")
    type = st.text_input("Enter the Type of Payment")
    amount = st.text_input("Enter the the Amount of the Transaction")
    oldbalanceOrg = st.text_input("Enter the Balance before the Transaction")
    newbalanceOrig = st.text_input("Enter the Balance after the Transaction")
    oldbalanceDest = st.text_input("Enter the Initial Balance of Recipient before the Transaction")
    newbalanceDest = st.text_input("Enter the New Balance of Recipient after the Transaction")

    # code for diagnosis
    diagnosis=" "
    
    #creating a button for prediction
    if st.button("Pedictor"):
        diagnosis = prediction([step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest])
    st.success(diagnosis)

if __name__=="__main__":
    main()