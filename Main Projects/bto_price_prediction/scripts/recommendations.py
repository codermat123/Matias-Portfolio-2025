# Function to recommend a flat based on user inputs (year range, region, budget)
def recommend_bto_budget(year_range, region, budget):
    print(f"Inputs received - Year Range: {year_range}, Region: {region}, Budget: {budget}")

    # Ensure the budget is in integer format (removing commas if it's a string)
    if isinstance(budget, str):
        budget = int(budget.replace(',', ''))

    # Matching year ranges to predefined options using integer ranges
    year_mapping = {
        "2026-2030": range(2026, 2031),  # years 2026 to 2030
        "2031-2034": range(2031, 2035),  # years 2031 to 2034
        "2035-2038": range(2035, 2039)   # years 2035 to 2038
    }

    # Convert year_range to integer for comparison
    selected_year = int(year_range)

    year_found = False
    for year_range_key, year_values in year_mapping.items():
        if selected_year in year_values:
            year_range = year_range_key
            year_found = True
            print(f"Year {selected_year} matched with range {year_range_key}")
            break

    if not year_found:
        return "Year range not valid."

    # Hardcoded recommendations based on Region and Budget
    if region == "West":
        if year_range == "2026-2030":
            if budget == 400000:
                return {"town": "Choa Chu Kang", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Jurong West", "room_type": "4-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Bukit Batok", "room_type": "4/5-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Choa Chu Kang", "room_type": "5-room", "max_selling_price": 1000000}
        elif year_range == "2031-2034":
            if budget == 400000:
                return {"town": "Jurong West", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Bukit Batok", "room_type": "3/4-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Choa Chu Kang", "room_type": "4-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Choa Chu Kang", "room_type": "5-room", "max_selling_price": 1000000}
        elif year_range == "2035-2038":
            if budget == 400000:
                return {"town": "Choa Chu Kang", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Tengah", "room_type": "3-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Jurong West", "room_type": "4-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Choa Chu Kang", "room_type": "5-room", "max_selling_price": 1000000}

    # North Region recommendations
    elif region == "North":
        if year_range == "2026-2030":
            if budget == 400000:
                return {"town": "Yishun", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Woodlands", "room_type": "4-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Sembawang", "room_type": "4/5-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Yishun", "room_type": "5-room", "max_selling_price": 1000000}
        elif year_range == "2031-2034":
            if budget == 400000:
                return {"town": "Woodlands", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Yishun", "room_type": "3/4-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Sembawang", "room_type": "4-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Yishun", "room_type": "5-room", "max_selling_price": 1000000}
        elif year_range == "2035-2038":
            if budget == 400000:
                return {"town": "Yishun", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Woodlands", "room_type": "3-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Sembawang", "room_type": "4-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Yishun", "room_type": "5-room", "max_selling_price": 1000000}

    # North-East Region recommendations
    elif region == "North-East":
        if year_range == "2026-2030":
            if budget == 400000:
                return {"town": "Punggol", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Sengkang", "room_type": "4-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Sengkang", "room_type": "4/5-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Punggol", "room_type": "5-room", "max_selling_price": 1000000}
        elif year_range == "2031-2034":
            if budget == 400000:
                return {"town": "Sengkang", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Punggol", "room_type": "3/4-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Sengkang", "room_type": "4-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Punggol", "room_type": "5-room", "max_selling_price": 1000000}
        elif year_range == "2035-2038":
            if budget == 400000:
                return {"town": "Punggol", "room_type": "3-room", "max_selling_price": 400000}
            elif budget == 600000:
                return {"town": "Sengkang", "room_type": "3-room", "max_selling_price": 600000}
            elif budget == 800000:
                return {"town": "Sengkang", "room_type": "4-room", "max_selling_price": 800000}
            elif budget == 1000000:
                return {"town": "Punggol", "room_type": "5-room", "max_selling_price": 1000000}

    # Default if no match is found
    return "No flat matches your criteria within your budget."