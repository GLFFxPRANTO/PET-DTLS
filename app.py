from flask import Flask, request
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    # Extracting 'uid' parameter from the query string
    uid = request.args.get('uid')
    if not uid:
        return "Error: UID not provided", 400, {'Content-Type': 'text/plain; charset=utf-8'}
    
    url = f"https://freefire-virusteam.vercel.app/glfflike?uid={uid}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "status" in data and data["status"] == "Success":
            # Extracting Pet-related information
            pet_info = data.get("Equipped Pet Information", {})
            pet_level = pet_info.get("Pet Level", "Not available")
            pet_id = pet_info.get("Pet ID", "Not available")
            pet_name = pet_info.get("Pet Name", "Not available")
            pet_skin_id = pet_info.get("Pet Skin ID", "Not available")
            pet_xp = pet_info.get("Pet XP", "Not available")
            selected = pet_info.get("Selected?", "Not available")
            
            return f"""PET LEVEL : {pet_level}
PET ID : {pet_id}
PET NAME : {pet_name}
PET SKIN ID : {pet_skin_id}
PET XP : {pet_xp}

SELECTED : {selected}""", 200, {'Content-Type': 'text/plain; charset=utf-8'}
        
        else:
            return "Error: Status is not Success or Data not found!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment
