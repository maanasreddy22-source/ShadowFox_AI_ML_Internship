
import gradio as gr
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("car_price_prediction_model.pkl")

# Prediction function
def predict_price(year, present_price, kms, owner,
                  fuel, seller, transmission):

    car = pd.DataFrame([{
        "Year": year,
        "Present_Price": present_price,
        "Kms_Driven": kms,
        "Owner": owner,
        "Fuel_Type_CNG": int(fuel == "CNG"),
        "Fuel_Type_Diesel": int(fuel == "Diesel"),
        "Fuel_Type_Petrol": int(fuel == "Petrol"),
        "Seller_Type_Dealer": int(seller == "Dealer"),
        "Seller_Type_Individual": int(seller == "Individual"),
        "Transmission_Automatic": int(transmission == "Automatic"),
        "Transmission_Manual": int(transmission == "Manual")
    }])

    car = car[model.feature_names_in_]
    result = model.predict(car)[0]

    return f"Estimated Selling Price: ₹{result:.2f} lakhs"


# Create Gradio interface
app = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Year", value=2018),
        gr.Number(label="Present Price", value=8.5),
        gr.Number(label="Kilometers Driven", value=30000),
        gr.Dropdown([0, 1, 2, 3], value=0, label="Previous Owners"),
        gr.Dropdown(["Petrol", "Diesel", "CNG"], value="Petrol", label="Fuel"),
        gr.Dropdown(["Dealer", "Individual"], value="Individual", label="Seller"),
        gr.Dropdown(["Manual", "Automatic"], value="Manual", label="Transmission")
    ],
    outputs=gr.Textbox(label="Predicted Price"),
    title="Car Selling Price Prediction"
)

app.launch(share=True)
