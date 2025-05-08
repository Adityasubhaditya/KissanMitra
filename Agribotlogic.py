import random

# Session data to track the conversation state
session_data = {}

def chatbot_greeting():
    session_data["current_step"] = "start"  # Reset to start
    return {
        'topic': 'Greeting',
        'response': (
            'Hello! 👋 Welcome, Kissan Mitra 🌱<br><br>'
            'I can assist you with the following:<br>'
            'A. <b>Crop Management</b><br>'
            'B. <b>Market Intelligence</b><br>'
            'C. <b>Financial Advisory</b><br>'
            'D. <b>Buying</b><br>'
            'E. <b>Selling</b><br>'
            'F. <b>Emergency</b><br><br>'
            'Please choose an option by replying with A, B, C, D, E, or F.'
        )
    }

# Handle Crop Management
def handle_crop_management(state, user_input=None):
    if state == 'start_crop_management':
        session_data['current_step'] = 'crop_management_menu'
        return {
            'topic': 'Crop Management',
            'response': (
                'Choose an option:<br>'
                '1. <b>Disease Identification and Management</b><br>'
                '2. <b>Crop Recommendations</b><br><br>'
                'Please reply with the option number (1 or 2).'
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
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Remove affected leaves and ensure proper spacing between plants to improve airflow.<br>'
                    '2. <b>Wilting and Yellowing</b>:<br>'
                    '&nbsp;&nbsp;- Diseases: Fusarium Wilt, Verticillium Wilt<br>'
                    '&nbsp;&nbsp;- Solution:<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Use resistant crop varieties.<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Ensure proper drainage and avoid overwatering.<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Rotate crops to prevent soil-borne pathogens.<br>'
                    '3. <b>Pest Infestation</b>:<br>'
                    '&nbsp;&nbsp;- Diseases: Aphid Infestation, Spider Mite Damage<br>'
                    '&nbsp;&nbsp;- Solution:<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Use neem oil or insecticidal soaps to control pests.<br>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;- Introduce beneficial insects like ladybugs or lacewings.'
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
                    'Provide these details separated by commas.'
                )
            }
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Invalid choice. Please reply with 1 or 2.'
            }

# The rest of the functions would be updated in a similar fashion,
# replacing \n with <br> for better formatting.


# Handle Market Intelligence
def handle_market_intelligence(state, user_input=None):
    if state == "start_market_intelligence":
        session_data["current_step"] = "market_intelligence_menu"
        return {
            "topic": "Market Intelligence",
            "response": (
                "Choose an option:\n"
                "1. **Seed Procurement Guidance**\n"
                "2. **Yield Estimation**\n"
                "3. **Current Market Prices**\n"
                "\nPlease reply with the option number (1, 2, or 3)."
            )
        }
    elif state == "market_intelligence_menu":
        if user_input in ["1", "2", "3"]:
            session_data["current_step"] = "intelligence"  # Set next step
            if user_input == "1":
                return {
                    "topic": "Seed Procurement Guidance",
                    "response": "When procuring seeds, farmers should prioritize quality and reliability to ensure the best possible crop yields."
                    "It's essential to buy certified seeds from reputable suppliers, as these seeds are tested for purity, germination rates, and resistance to pests and diseases."
                    "Selecting varieties that are specifically adapted to the local climate, soil type, and agricultural conditions will lead to better growth and productivity."
                    "Before purchasing, farmers should check the seed packaging for the production and expiration dates, as using fresh seeds ensures higher germination rates."
                    "In addition to quantity, farmers should focus on proper storage—seeds should be kept in cool, dry, and dark places to maintain their quality." 
                    "Exploring government programs, agricultural cooperatives, or farmer groups for seed distribution or discounts can also help reduce costs."
                    " Farmers should also consider diversifying their seed sources to avoid reliance on a single supplier and mitigate potential risks from seed shortages or price fluctuations."
                    " Seeking advice from agricultural extension services or local agronomists can provide valuable insights into the best seed choices for specific needs."
                    "Building relationships with trusted seed producers or cooperatives can lead to better deals and early access to high-quality seeds."
                    "By making informed decisions, farmers can maximize their investments in seed procurement and enhance the overall success of their farming practices."
                }
            elif user_input == "2":
                return {
                    "topic": "Yield Estimation",
                    "response": "Yield estimation can be done using the formula: **Yield = (Number of plants per unit area) × (Average weight of produce per plant)**."
                                "Another method is the **Plant Population Method**, which involves multiplying plant density, average weight per plant, and area under cultivation."
                                "The **Harvest Index (HI)**, the ratio of edible crop portions to total biomass, is also used."
                                "For more accuracy, **Crop Growth Models** consider factors like climate, growth stages, and environmental conditions."
                                "Proper management of soil, irrigation, and pests is essential for improving yield predictions."
                }
            elif user_input == "3":
                return {
                    "topic": "Current Market Prices",
                    "response": "Rice: ₹35.31 per kg, with prices varying across states."
                    "Wheat: ₹28.5 per kg, with prices varying across states."
                    "Sugarcane: Typically sold by the tonne; prices vary by region."
                    "Cotton: ₹100 per kg, with prices varying across states."
                    "Maize: ₹25 per kg, with prices varying across states."
                    "Pulses: ₹80 per kg (for pigeon peas), with prices varying widely depending on the type."
                }
        else:
            return {
                "topic": "Invalid Option",
                "response": "Invalid choice. Please reply with 1, 2, or 3."
            }

# Handle Financial Advisory
def handle_financial_advisory(state, user_input=None):
    if state == "start_financial_advisory":
        session_data["current_step"] = "financial_advisory_menu"
        return {
            "topic": "Financial Advisory",
            "response": (
                "Choose an option:\n"
                "1. **Crop Profitability Calculator**\n"
                "2. **Loan Information**\n"
                "3. **Subsidy Information**\n"
                "4. **Investment Management**\n"
                "\nPlease reply with the option number (1, 2, 3, or 4)."
            )
        }
    elif state == "financial_advisory_menu":
        if user_input in ["1", "2", "3", "4"]:
            session_data["current_step"] = "financial"  # Set next step
            if user_input == "1":
                return {
                    "topic": "Crop Profitability Calculator",
                    "response": "Rice: Average profit of ₹20,000 per acre, with variations based on irrigation, input costs, and yield."
                                "Wheat: Average profit of ₹18,000 per acre, influenced by climate conditions and market prices."
                                "Sugarcane: Average profit of ₹35,000 per acre, but varies with weather and sugar prices."
                                "Cotton: Average profit of ₹25,000 per acre, influenced by global cotton prices and pest management."
                                "Maize: Average profit of ₹15,000 per acre, with profitability depending on yield and input costs."
                                "Pulses: Average profit of ₹10,000 to ₹20,000 per acre, depending on market demand and weather conditions."
                }
            elif user_input == "2":
                return {
                    "topic": "Loan Information",
                    "response": "Kisan Credit Card (KCC): Loans ranging from ₹10,000 to ₹3 lakh, with low interest rates (4-7 %) for short-term crop cultivation."
                                "Term Loans: Loans for purchasing farm equipment, seeds, and inputs; typically ₹50,000 to ₹10 lakh with interest rates of 9% to 12%."
                                "Government Schemes: Various schemes like PM-Kisan, NABARD loans provide financial assistance with subsidies, varying from ₹10,000 to ₹1 lakh."
                                "Input Loans: Loans for fertilizers, pesticides, and seeds; repayment period of 6-12 months, with interest rates of around 7-9 %."
                                "Crop Loans: Short-term loans for seasonal crops; loan amounts from ₹50,000 to ₹5 lakh with interest rates ranging from 7% to 12%."
                                "Loan Waivers: Some states offer loan waivers depending on government schemes, often aimed at reducing the burden on distressed farmers."
                }
            elif user_input == "3":
                return {
                    "topic": "Subsidy Information",
                    "response": "PM-KISAN Scheme: Provides ₹6,000 per year in three equal installments for small and marginal farmers, aimed at supporting crop production."
                                "Subsidy for Agricultural Equipment: Government subsidies of 25-50 percent for purchasing machinery like tractors, harvesters, and drip irrigation systems."
                                "National Mission on Agriculture Extension & Technology (NMAET): Provides subsidies for training, technology adoption, and infrastructure development in farming."
                                "Pradhan Mantri Fasal Bima Yojana (PMFBY): Subsidized crop insurance premiums with farmers paying only 2-5 percent of the premium, depending on the crop."
                                "Subsidy on Fertilizers: Government provides subsidies on fertilizers like urea, DAP, and potash to keep costs affordable for farmers."
                                "State-Specific Subsidies: Various states offer their own subsidy programs, including input cost subsidies, irrigation development, and crop-specific assistance."
                }
            elif user_input == "4":
                return {
                    "topic": "Investment Management",
                    "response":"Diversification: Farmers can invest in multiple crops and livestock to reduce risks from crop failure or market fluctuations."
                               "Agri-Business Investments: Investment in agribusinesses like food processing, packaging, and storage facilities can offer stable returns."
                               "Government Schemes: Various government-backed schemes like the Pradhan Mantri Krishi Sinchayee Yojana (PMKSY) help farmers invest in irrigation infrastructure."
                               "Cooperative Farming: Investment in farmer cooperatives can provide access to shared resources, bulk purchasing, and better market prices."
                               "Microfinance: Small loans or savings groups, supported by microfinance institutions, help farmers invest in inputs or improve their business operations."
                               "Long-Term Investment: Investing in agricultural land or agroforestry can provide long-term capital appreciation and sustained income."
                }
        else:
            return {
                "topic": "Invalid Option",
                "response": "Invalid choice. Please reply with 1, 2, 3, or 4."
            }

# Handle Buying
def handle_buying(state, user_input=None):
    if state == "start_buying":
        session_data["current_step"] = "buying_menu"
        return {
            "topic": "Buying",
            "response": (
                "Choose an option:\n"
                "1. **Equipment**\n"
                "2. **Seeds**\n"
                "3. **Fertilizers**\n"
                "\nPlease reply with the option number (1, 2, or 3)."
            )
        }
    elif state == "buying_menu":
        if user_input in ["1", "2", "3"]:
            session_data["current_step"] = "buying"  # Set next step
            if user_input == "1":
                return {
                    "topic": "Equipment",
                    "response":"Tractors: Prices typically range from ₹3 lakh to ₹10 lakh, depending on the brand and horsepower (HP). Popular brands include Mahindra, John Deere, and New Holland."
                                "Harvesters: Combine harvesters can cost between ₹10 lakh and ₹25 lakh, while smaller rice or wheat harvesters may cost ₹5 lakh to ₹8 lakh."
                                "Sprayers: Manual sprayers start at around ₹1,000, while motorized sprayers can range from ₹10,000 to ₹50,000 depending on capacity and features."
                                "Ploughs: A basic tractor-mounted plough can cost around ₹20,000 to ₹50,000, with advanced versions priced higher depending on the design and brand."
                                "Drip Irrigation System: Costs for installing a drip irrigation system vary, but small-scale systems can start from ₹30,000, with larger systems going up to ₹2 lakh or more for bigger farms."
                                "Power Tillers: Prices for power tillers range from ₹1.5 lakh to ₹4 lakh, depending on brand and specifications."
                }
            elif user_input == "2":
                return {
                    "topic": "Seeds",
                    "response":  "Rice Seeds: Prices typically range from ₹50 to ₹150 per kg, depending on the variety (e.g., Basmati, Non-Basmati)."
                                 "Wheat Seeds: Prices generally range from ₹30 to ₹50 per kg, with hybrid varieties costing a bit more."
                                 "Sugarcane Seeds (Setts): Prices vary, typically ranging from ₹1,000 to ₹3,000 per tonne, depending on the variety and quality."
                                 "Cotton Seeds: The price for hybrid cotton seeds is around ₹700 to ₹1,500 per kg, depending on the quality and variety."
                                 "Maize Seeds: Prices generally range from ₹60 to ₹120 per kg, depending on the hybrid variety."
                                 "Pulses Seeds: Prices vary by type, but for common pulses like chickpeas (toor) and lentils, they range from ₹80 to ₹200 per kg."
                }
            elif user_input == "3":
                return {
                    "topic": "Fertilizers",
                    "response": "Urea: Prices typically range from ₹250 to ₹350 per 50 kg bag, depending on the state and market conditions."
                                "Diammonium Phosphate (DAP): Prices generally range from ₹1,200 to ₹1,500 per 50 kg bag, with slight variations based on region."
                                "Potash (MOP): Prices generally range from ₹800 to ₹1,200 per 50 kg bag."
                                "Neem Cake: Prices typically range from ₹15 to ₹25 per kg, depending on the quality and supplier."
                                "Compost: Prices for organic compost range from ₹500 to ₹1,500 per tonne, depending on the composition and source."
                                "Micronutrients: Prices for micronutrient mixtures (like zinc, boron) can vary from ₹100 to ₹300 per kg, depending on the formulation."
                }
        else:
            return {
                "topic": "Invalid Option",
                "response": "Invalid choice. Please reply with 1, 2, or 3."
            }

# Handle Selling
def handle_selling(state, user_input=None):
    if state == "start_selling":
        session_data["current_step"] = "selling_menu"
        return {
            "topic": "Selling",
            "response": (
                "Choose an option:\n"
                "1. **To Government**\n"
                "2. **To Local Vendors**\n"
                "\nPlease reply with the option number (1 or 2)."
            )
        }
    elif state == "selling_menu":
        if user_input in ["1", "2"]:
            session_data["current_step"] = "selling"  # Set next step
            if user_input == "1":
                return {
                    "topic": "To Government",
                    "response":"Step 1: Registration: Farmers need to register with government platforms like the Minimum Support Price (MSP) or through state-specific Agricultural Marketing Boards or cooperatives."
                                "Step 2: Documentation: Ensure you have required documents, including Aadhar card, bank account details, land ownership papers, and crop details."
                                "Step 3: Identify Government Schemes: Find the right government procurement schemes like PM-AASHA, MSP, or procurement through state agencies (e.g., FCI, NAFED)."
                                "Step 4: Submit Crop Details: Provide accurate details of the crops being sold, such as quantity, quality, and harvesting date, to the respective agencies or platforms."
                                "Step 5: Crop Grading and Weighing: Government agencies or associated bodies will inspect and grade the produce before purchasing. They may also offer transportation assistance."
                                "Step 6: Receive Payment: After the sale, payments are typically made directly to the farmer’s bank account under MSP or through the respective procurement system."
                                "Step 7: Keep Track: Ensure that all payment receipts and records are kept for reference and to track any future transactions."
                }
            elif user_input == "2":
                return {
                    "topic": "To Local Vendors",
                    "response": "Reach out to local vendors or use online platforms like AgriMarket for selling."
                }
        else:
            return {
                "topic": "Invalid Option",
                "response": "Invalid choice. Please reply with 1 or 2."
            }

# Handle Emergency
def handle_emergency(state, user_input=None):
    if state == "start_emergency":
        session_data["current_step"] = "emergency"  # Set next step
        return {
            "topic": "Emergency",
            "response": (
                "Emergency Contacts:\n"
                "- Police: 100\n"
                "- Ambulance: 108\n"
                "- Pest Control: 1800-123-4567\n"
                "\nLet me know if you need further help."
            )
        }

# Analyze Query
def analyze_query(query):
    query = query.lower()
    current_step = session_data.get("current_step", "start")

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
                'response': 'Please choose an option by replying with A, B, C, D, E, or F.'
            }
    elif current_step == "crop_management_menu":
        if query == "1":
            return handle_crop_management("crop_management_menu", "1")
        elif query == "2":
            return handle_crop_management("crop_management_menu", "2")
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1 or 2.'
            }
    elif current_step == "disease_management":
        if query == "2":
            return handle_crop_management("crop_management_menu", "2")
    elif current_step == "crop_recommendation":
        if query == "menu-1":
            return handle_crop_management("start_crop_management")
    elif current_step == "market_intelligence_menu":
        if query == "1":
            return handle_market_intelligence("market_intelligence_menu", "1")
        elif query == "2":
            return handle_market_intelligence("market_intelligence_menu", "2")
        elif query == "3":
            return handle_market_intelligence("market_intelligence_menu", "3")
    elif current_step == "intelligence":
        if query == "menu-2":
            return handle_market_intelligence("start_market_intelligence")
    elif current_step == "financial_advisory_menu":
        if query == "1":
            return handle_financial_advisory("financial_advisory_menu", "1")
        elif query == "2":
            return handle_financial_advisory("financial_advisory_menu", "2")
        elif query == "3":
            return handle_financial_advisory("financial_advisory_menu", "3")
        elif query == "4":
            return handle_financial_advisory("financial_advisory_menu", "4")
    elif current_step == "financial":
        if query == "menu-3":
            return handle_financial_advisory("start_financial_advisory")
    elif current_step == "buying_menu":
        if query == "1":
            return handle_buying("buying_menu", "1")
        elif query == "2":
            return handle_buying("buying_menu", "2")
        elif query == "3":
            return handle_buying("buying_menu", "3")
    elif current_step == "buying":
        if query == "menu-4":
            return handle_buying("start_buying")
    elif current_step == "selling_menu":
        if query == "1":
            return handle_selling("selling_menu", "1")
        elif query == "2":
            return handle_selling("selling_menu", "2")
    elif current_step == "selling":
        if query == "menu-5":
            return handle_selling("start_selling")
    elif current_step == "start_emergency":
        if query == "1":
            return handle_emergency("start_emergency")
        elif query == "2":
            return handle_emergency("start_emergency")
        else:
            return {
                'topic': 'Invalid Option',
                'response': 'Please reply with 1 or 2.'
            }

    return {
        'topic': 'General Assistance',
        'response': "Sorry, I didn't understand that. Could you clarify?"
    }
