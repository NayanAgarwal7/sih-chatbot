def get_response(user_msg):
    msg = user_msg.lower()

    # Rule-based answers
    if "october" in msg and "rajasthan" in msg:
        return "For Rajasthan in October, Wheat, Mustard, and Chickpea are recommended."
    elif "fertilizer" in msg:
        return "Urea and DAP are commonly used fertilizers. Use according to soil testing."
    elif "hello" in msg or "hi" in msg:
        return "Hello 👋! I’m your Crop Recommendation Assistant. How can I help?"
    elif "soil" in msg:
        return ("Soil is the top layer of the earth where plants grow, "
                "composed of minerals, organic matter, air, and water.")
    elif "red soil" in msg:
        return ("Red soil is rich in iron, has a reddish color, "
                "and is mostly found in dry regions. Suitable for crops like cotton, wheat, and pulses.")
    elif "black soil" in msg:
        return ("Black soil, also called regur soil, is rich in clay and retains moisture. "
                "Best for cotton, soybean, and sugarcane.")
    elif "weather" in msg:
        return "Weather affects crop growth. Make sure to check your local forecast before planting."
    
    # Simulated AI response for anything else
    return ("[Simulated AI Reply] I can help with crops, soil, fertilizer, and general agriculture guidance. "
            "Please ask a specific question about farming or crops.")
