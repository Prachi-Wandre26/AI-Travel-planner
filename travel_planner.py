import google.generativeai as genai
import google.api_core.exceptions
import streamlit as st

# Initialize Google GenAI (set up your API key)
genai.configure(api_key="AIzaSyApJBcqf9MfKvaihVzVFTXCS5CGsKGayVc")

def get_travel_options(source, destination):
    # Define the prompt for GenAI
    prompt = f"Suggest travel options from {source} to {destination} with estimated costs."
    
    # List available models
    models = list(genai.list_models())
    
    # Check if we have at least one model available
    if not models:
        st.error("❌ No models found!")
        return []

    # Assuming the first model is the one we want to use (or choose an appropriate model)
    model = models[0]

    try:
        # Generate content using the correct method for this model
        response = model.generate_text(prompt)  # Use generate_text() method to get a response
        
        # Process response
        travel_options = parse_response(response['text'])  # Adjust to access the text field
        return travel_options

    except google.api_core.exceptions.NotFound:
        st.error("❌ Model not found! Please check the model name and try again.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
        return []

def parse_response(response_text):
    """ Convert GenAI response into structured travel options """
    options = []
    for line in response_text.split("\n"):
        parts = line.split("-")
        if len(parts) == 2:
            mode, cost = parts
            options.append({"mode": mode.strip(), "cost": cost.strip()})
    return options
