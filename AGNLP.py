import random
import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Session data to track the conversation state
session_data = {}

def chatbot_greeting():
    session_data["current_step"] = "start"  # Reset to start
    return {
        'topic': 'Greeting',
        'response': (
            'Hello! 👋 Welcome to Kissan-Mitra 🌱<br><br>'
            'I can assist you with the following agricultural topics:<br>'
            'A. <b>Crop Management</b><br>'
            'B. <b>Market Intelligence</b><br>'
            'C. <b>Financial Advisory</b><br>'
            'D. <b>Buying Agricultural Inputs</b><br>'
            'E. <b>Selling Agricultural Produce</b><br>'
            'F. <b>Emergency Assistance</b><br><br>'
            'Please choose an option by replying with A, B, C, D, E, or F.<br>'
            'Reply with "menu" anytime to go back to the main menu.'
        )
    }

def extract_intent_and_entities(query):
    """
    Extract intent and entities from the user query using spaCy.
    """
    doc = nlp(query)
    
    # Define possible intents
    intents = {
        "crop_management": ["crop", "disease", "soil", "irrigation", "fertilizer", "pest"],
        "market_intelligence": ["market", "price", "yield", "seed", "procurement"],
        "financial_advisory": ["loan", "subsidy", "profit", "investment", "finance"],
        "buying": ["buy", "equipment", "seeds", "fertilizer", "purchase"],
        "selling": ["sell", "produce", "government", "vendor", "market"],
        "emergency": ["emergency", "help", "pest", "contact", "assistance"]
    }
    
    # Extract intent
    intent = None
    for key, keywords in intents.items():
        if any(keyword in query.lower() for keyword in keywords):
            intent = key
            break
    
    # Extract entities (e.g., crop type, disease name, etc.)
    entities = {ent.text: ent.label_ for ent in doc.ents}
    
    return intent, entities

def handle_crop_management(state, user_input=None):
    if state == 'start_crop_management':
        session_data['current_step'] = 'crop_management_menu'
        return {
            'topic': 'Crop Management',
            'response': (
                'Crop Management Help 🌾<br>'
                '1. <b>Disease Identification and Management</b><br>'
                '2. <b>Crop Recommendations</b><br>'
                '3. <b>Soil Health and Fertilization</b><br>'
                '4. <b>Irrigation Techniques</b><br>'
                'Please reply with the topic number (1, 2, 3, or 4) to learn more!<br>'
                'Reply with "back" to return to the main menu.'
            )
        }
    elif state == 'crop_management_menu':
        if user_input == '1':
            session_data['current_step'] = 'disease_management'
            return {
                'topic': 'Disease Identification',
                'response': (
                    'Common crop diseases and their management:<br>'
                    '1. <b>Leaf Spots</b>:<br>'
                    '&nbsp;&nbsp;- Diseases: Leaf Blight, Leaf Spot Disease<br>'
                    '&nbsp;&nbsp;- Solution:<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Apply fungicides like Mancozeb or Chlorothalonil.<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Remove affected leaves and ensure proper spacing between plants.<br>'
                    '2. <b>Wilting and Yellowing</b>:<br>'
                    '&nbsp;&nbsp;- Diseases: Fusarium Wilt, Verticillium Wilt<br>'
                    '&nbsp;&nbsp;- Solution:<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Use resistant crop varieties.<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Ensure proper drainage and avoid overwatering.<br>'
                    '3. <b>Pest Infestation</b>:<br>'
                    '&nbsp;&nbsp;- Diseases: Aphid Infestation, Spider Mite Damage<br>'
                    '&nbsp;&nbsp;- Solution:<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Use neem oil or insecticidal soaps to control pests.<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Introduce beneficial insects like ladybugs or lacewings.<br><br>'
                    'Reply with "back" to return to the Crop Management menu.'
                )
            }
        elif user_input == '2':
            session_data['current_step'] = 'crop_recommendation'
            return {
                'topic': 'Crop Recommendations',
                'response': (
                    'To recommend a crop, please provide:<br>'
                    '- <b>Soil Type</b> (e.g., sandy, clayey, loamy)<br>'
                    '- <b>Temperature Range</b> (e.g., 20°C-30°C)<br>'
                    '- <b>Rainfall Level</b> (light, moderate, heavy)<br><br>'
                    'Provide these details separated by commas.<br><br>'
                    'Reply with "back" to return to the Crop Management menu.'
                )
            }
        elif user_input == '3':
            session_data['current_step'] = 'soil_health'
            return {
                'topic': 'Soil Health and Fertilization',
                'response': (
                    'Soil Health Tips:<br>'
                    '- Test soil pH and nutrient levels regularly.<br>'
                    '- Use organic compost to improve soil fertility.<br>'
                    '- Rotate crops to prevent soil depletion.<br>'
                    '- Apply fertilizers based on soil test results.<br>'
                    'Example: For nitrogen-deficient soil, apply urea or ammonium nitrate.<br><br>'
                    'Reply with "back" to return to the Crop Management menu.'
                )
            }
        elif user_input == '4':
            session_data['current_step'] = 'irrigation_techniques'
            return {
                'topic': 'Irrigation Techniques',
                'response': (
                    'Common Irrigation Methods:<br>'
                    '- <b>Drip Irrigation</b>: Efficient water usage, ideal for water-scarce regions.<br>'
                    '- <b>Sprinkler Irrigation</b>: Suitable for large fields and uneven terrain.<br>'
                    '- <b>Flood Irrigation</b>: Traditional method, best for rice and similar crops.<br>'
                    '- <b>Subsurface Irrigation</b>: Reduces water evaporation and weed growth.<br><br>'
                    'Reply with "back" to return to the Crop Management menu.'
                )
            }
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Invalid choice. Please reply with 1, 2, 3, or 4.<br><br>'
                            'Reply with "back" to return to the main menu.'
            }
    elif state in ['disease_management', 'crop_recommendation', 'soil_health', 'irrigation_techniques']:
        if user_input == 'back':
            session_data['current_step'] = 'crop_management_menu'
            return handle_crop_management('start_crop_management')
    else:
        return {
            'topic': 'Invalid State',
            'response': 'Invalid state. Please start over.'
        }

def handle_market_intelligence(state, user_input=None):
    if state == 'start_market_intelligence':
        session_data['current_step'] = 'market_intelligence_menu'
        return {
            'topic': 'Market Intelligence',
            'response': (
                'Market Intelligence Help 📊<br>'
                '1. <b>Seed Procurement Guidance</b><br>'
                '2. <b>Yield Estimation</b><br>'
                '3. <b>Current Market Prices</b><br>'
                'Please reply with the topic number (1, 2, or 3) to learn more!<br>'
                'Reply with "back" to return to the main menu.'
            )
        }
    elif state == 'market_intelligence_menu':
        if user_input == '1':
            session_data['current_step'] = 'seed_procurement'
            return {
                'topic': 'Seed Procurement Guidance',
                'response': (
                    'Seed Procurement Tips:<br>'
                    '- Always buy certified seeds from reputable suppliers.<br>'
                    '- Check for germination rates and seed quality.<br>'
                    '- Choose seeds adapted to your local climate and soil.<br>'
                    '- Store seeds in cool, dry conditions to maintain viability.<br><br>'
                    'Reply with "back" to return to the Market Intelligence menu.'
                )
            }
        elif user_input == '2':
            session_data['current_step'] = 'yield_estimation'
            return {
                'topic': 'Yield Estimation',
                'response': (
                    'Yield Estimation Methods:<br>'
                    '- Use the formula: **Yield = (Number of plants per unit area) × (Average weight of produce per plant)**.<br>'
                    '- Consider factors like soil fertility, weather, and pest control.<br>'
                    '- Use crop growth models for more accurate predictions.<br><br>'
                    'Reply with "back" to return to the Market Intelligence menu.'
                )
            }
        elif user_input == '3':
            session_data['current_step'] = 'market_prices'
            return {
                'topic': 'Current Market Prices',
                'response': (
                    'Current Market Prices:<br>'
                    '- Rice: ₹35.31 per kg<br>'
                    '- Wheat: ₹28.5 per kg<br>'
                    '- Sugarcane: ₹1,000-₹3,000 per tonne<br>'
                    '- Cotton: ₹100 per kg<br>'
                    '- Maize: ₹25 per kg<br>'
                    '- Pulses: ₹80-₹200 per kg (depending on type).<br><br>'
                    'Reply with "back" to return to the Market Intelligence menu.'
                )
            }
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Invalid choice. Please reply with 1, 2, or 3.<br><br>'
                            'Reply with "back" to return to the main menu.'
            }
    elif state in ['seed_procurement', 'yield_estimation', 'market_prices']:
        if user_input == 'back':
            session_data['current_step'] = 'market_intelligence_menu'
            return handle_market_intelligence('start_market_intelligence')
    else:
        return {
            'topic': 'Invalid State',
            'response': 'Invalid state. Please start over.'
        }

def handle_financial_advisory(state, user_input=None):
    if state == 'start_financial_advisory':
        session_data['current_step'] = 'financial_advisory_menu'
        return {
            'topic': 'Financial Advisory',
            'response': (
                'Financial Advisory Help 💰<br>'
                '1. <b>Crop Profitability Calculator</b><br>'
                '2. <b>Loan Information</b><br>'
                '3. <b>Subsidy Information</b><br>'
                '4. <b>Investment Management</b><br>'
                'Please reply with the topic number (1, 2, 3, or 4) to learn more!<br>'
                'Reply with "back" to return to the main menu.'
            )
        }
    elif state == 'financial_advisory_menu':
        if user_input == '1':
            session_data['current_step'] = 'crop_profitability'
            return {
                'topic': 'Crop Profitability Calculator',
                'response': (
                    'Crop Profitability Examples:<br>'
                    '- Rice: Average profit of ₹20,000 per acre.<br>'
                    '- Wheat: Average profit of ₹18,000 per acre.<br>'
                    '- Sugarcane: Average profit of ₹35,000 per acre.<br>'
                    '- Cotton: Average profit of ₹25,000 per acre.<br><br>'
                    'Reply with "back" to return to the Financial Advisory menu.'
                )
            }
        elif user_input == '2':
            session_data['current_step'] = 'loan_information'
            return {
                'topic': 'Loan Information',
                'response': (
                    'Loan Options:<br>'
                    '- Kisan Credit Card (KCC): Loans up to ₹3 lakh at 4-7% interest.<br>'
                    '- Term Loans: For equipment and inputs, ₹50,000 to ₹10 lakh at 9-12% interest.<br>'
                    '- Government Schemes: PM-Kisan, NABARD loans with subsidies.<br><br>'
                    'Reply with "back" to return to the Financial Advisory menu.'
                )
            }
        elif user_input == '3':
            session_data['current_step'] = 'subsidy_information'
            return {
                'topic': 'Subsidy Information',
                'response': (
                    'Subsidy Schemes:<br>'
                    '- PM-KISAN: ₹6,000 per year in three installments.<br>'
                    '- Subsidy for Agricultural Equipment: 25-50% off on machinery.<br>'
                    '- Fertilizer Subsidy: Reduced prices for urea, DAP, and potash.<br><br>'
                    'Reply with "back" to return to the Financial Advisory menu.'
                )
            }
        elif user_input == '4':
            session_data['current_step'] = 'investment_management'
            return {
                'topic': 'Investment Management',
                'response': (
                    'Investment Tips:<br>'
                    '- Diversify crops and livestock to reduce risk.<br>'
                    '- Invest in agribusinesses like food processing.<br>'
                    '- Explore government schemes for irrigation and infrastructure.<br><br>'
                    'Reply with "back" to return to the Financial Advisory menu.'
                )
            }
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Invalid choice. Please reply with 1, 2, 3, or 4.<br><br>'
                            'Reply with "back" to return to the main menu.'
            }
    elif state in ['crop_profitability', 'loan_information', 'subsidy_information', 'investment_management']:
        if user_input == 'back':
            session_data['current_step'] = 'financial_advisory_menu'
            return handle_financial_advisory('start_financial_advisory')
    else:
        return {
            'topic': 'Invalid State',
            'response': 'Invalid state. Please start over.'
        }

def handle_buying(state, user_input=None):
    if state == 'start_buying':
        session_data['current_step'] = 'buying_menu'
        return {
            'topic': 'Buying Agricultural Inputs',
            'response': (
                'Buying Help 🛒<br>'
                '1. <b>Equipment</b><br>'
                '2. <b>Seeds</b><br>'
                '3. <b>Fertilizers</b><br>'
                'Please reply with the topic number (1, 2, or 3) to learn more!<br>'
                'Reply with "back" to return to the main menu.'
            )
        }
    elif state == 'buying_menu':
        if user_input == '1':
            session_data['current_step'] = 'equipment'
            return {
                'topic': 'Equipment',
                'response': (
                    'Equipment Prices:<br>'
                    '- Tractors: ₹3 lakh to ₹10 lakh.<br>'
                    '- Harvesters: ₹5 lakh to ₹25 lakh.<br>'
                    '- Sprayers: ₹1,000 to ₹50,000.<br>'
                    '- Drip Irrigation Systems: ₹30,000 to ₹2 lakh.<br><br>'
                    'Reply with "back" to return to the Buying menu.'
                )
            }
        elif user_input == '2':
            session_data['current_step'] = 'seeds'
            return {
                'topic': 'Seeds',
                'response': (
                    'Seed Prices:<br>'
                    '- Rice Seeds: ₹50 to ₹150 per kg.<br>'
                    '- Wheat Seeds: ₹30 to ₹50 per kg.<br>'
                    '- Cotton Seeds: ₹700 to ₹1,500 per kg.<br>'
                    '- Maize Seeds: ₹60 to ₹120 per kg.<br><br>'
                    'Reply with "back" to return to the Buying menu.'
                )
            }
        elif user_input == '3':
            session_data['current_step'] = 'fertilizers'
            return {
                'topic': 'Fertilizers',
                'response': (
                    'Fertilizer Prices:<br>'
                    '- Urea: ₹250 to ₹350 per 50 kg.<br>'
                    '- DAP: ₹1,200 to ₹1,500 per 50 kg.<br>'
                    '- Potash: ₹800 to ₹1,200 per 50 kg.<br>'
                    '- Neem Cake: ₹15 to ₹25 per kg.<br><br>'
                    'Reply with "back" to return to the Buying menu.'
                )
            }
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Invalid choice. Please reply with 1, 2, or 3.<br><br>'
                            'Reply with "back" to return to the main menu.'
            }
    elif state in ['equipment', 'seeds', 'fertilizers']:
        if user_input == 'back':
            session_data['current_step'] = 'buying_menu'
            return handle_buying('start_buying')
    else:
        return {
            'topic': 'Invalid State',
            'response': 'Invalid state. Please start over.'
        }

def handle_selling(state, user_input=None):
    if state == 'start_selling':
        session_data['current_step'] = 'selling_menu'
        return {
            'topic': 'Selling Agricultural Produce',
            'response': (
                'Selling Help 🚜<br>'
                '1. <b>To Government</b><br>'
                '2. <b>To Local Vendors</b><br>'
                'Please reply with the topic number (1 or 2) to learn more!<br>'
                'Reply with "back" to return to the main menu.'
            )
        }
    elif state == 'selling_menu':
        if user_input == '1':
            session_data['current_step'] = 'to_government'
            return {
                'topic': 'To Government',
                'response': (
                    'Selling to Government:<br>'
                    '- Register with MSP or state agencies.<br>'
                    '- Provide crop details and documents.<br>'
                    '- Payments are made directly to your bank account.<br><br>'
                    'Reply with "back" to return to the Selling menu.'
                )
            }
        elif user_input == '2':
            session_data['current_step'] = 'to_local_vendors'
            return {
                'topic': 'To Local Vendors',
                'response': (
                    'Selling to Local Vendors:<br>'
                    '- Reach out to local vendors or use platforms like AgriMarket.<br>'
                    '- Negotiate prices based on market rates.<br><br>'
                    'Reply with "back" to return to the Selling menu.'
                )
            }
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Invalid choice. Please reply with 1 or 2.<br><br>'
                            'Reply with "back" to return to the main menu.'
            }
    elif state in ['to_government', 'to_local_vendors']:
        if user_input == 'back':
            session_data['current_step'] = 'selling_menu'
            return handle_selling('start_selling')
    else:
        return {
            'topic': 'Invalid State',
            'response': 'Invalid state. Please start over.'
        }

def handle_emergency(state, user_input=None):
    if state == 'start_emergency':
        session_data['current_step'] = 'emergency_menu'
        return {
            'topic': 'Emergency Assistance',
            'response': (
                'Emergency Contacts:<br>'
                '- Police: 100<br>'
                '- Ambulance: 108<br>'
                '- Pest Control: 1800-123-4567<br><br>'
                'Reply with "back" to return to the main menu.'
            )
        }
    elif state == 'emergency_menu':
        if user_input == 'back':
            session_data['current_step'] = 'start'
            return chatbot_greeting()
    else:
        return {
            'topic': 'Invalid State',
            'response': 'Invalid state. Please start over.'
        }

def analyze_query(query):
    query = query.lower()
    current_step = session_data.get("current_step", "start")

    # Extract intent and entities using NLP
    intent, entities = extract_intent_and_entities(query)
    
    # If intent is detected, route to the appropriate handler
    if intent:
        if intent == "crop_management":
            return handle_crop_management("start_crop_management")
        elif intent == "market_intelligence":
            return handle_market_intelligence("start_market_intelligence")
        elif intent == "financial_advisory":
            return handle_financial_advisory("start_financial_advisory")
        elif intent == "buying":
            return handle_buying("start_buying")
        elif intent == "selling":
            return handle_selling("start_selling")
        elif intent == "emergency":
            return handle_emergency("start_emergency")
    
    # If no intent is detected, fall back to the existing logic
    if query == "menu":
        return chatbot_greeting()

    if current_step == "start":
        if query == "a":
            return handle_crop_management("start_crop_management")
        elif query == "b":
            return handle_market_intelligence("start_market_intelligence")
        elif query == "c":
            return handle_financial_advisory("start_financial_advisory")
        elif query == "d":
            return handle_buying("start_buying")
        elif query == "e":
            return handle_selling("start_selling")
        elif query == "f":
            return handle_emergency("start_emergency")
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please choose an option by replying with A, B, C, D, E, or F, or type "menu" to return to the main menu.'
            }
    elif current_step == "crop_management_menu":
        if query in ["1", "2", "3", "4"]:
            return handle_crop_management("crop_management_menu", query)
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1, 2, 3, or 4, or type "menu" to return to the main menu.'
            }
    elif current_step == "market_intelligence_menu":
        if query in ["1", "2", "3"]:
            return handle_market_intelligence("market_intelligence_menu", query)
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1, 2, or 3, or type "menu" to return to the main menu.'
            }
    elif current_step == "financial_advisory_menu":
        if query in ["1", "2", "3", "4"]:
            return handle_financial_advisory("financial_advisory_menu", query)
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1, 2, 3, or 4, or type "menu" to return to the main menu.'
            }
    elif current_step == "buying_menu":
        if query in ["1", "2", "3"]:
            return handle_buying("buying_menu", query)
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1, 2, or 3, or type "menu" to return to the main menu.'
            }
    elif current_step == "selling_menu":
        if query in ["1", "2"]:
            return handle_selling("selling_menu", query)
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1 or 2, or type "menu" to return to the main menu.'
            }
    elif current_step == "emergency_menu":
        if query == "back":
            session_data['current_step'] = "start"
            return chatbot_greeting()
    else:
        return {
            'topic': 'General Assistance',
            'response': 'I am here to help! Please choose a topic or ask a question. Reply with "menu" to return to the main menu.'
        }