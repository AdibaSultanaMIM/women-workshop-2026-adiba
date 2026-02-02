from flask import Flask, request, jsonify
from flask_cors import CORS
from database import save_registration
from email_service import send_confirmation_email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure CORS for GitHub Pages
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://adibasultanamim.github.io",
            "https://we-ict-workshop.github.io",
            "http://localhost:*"
        ]
    }
})

@app.route('/api/register', methods=['POST'])
def register():
    """Handle workshop registration"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['full_name', 'email', 'phone', 'institution', 'topic']
        for field in required_fields:
            if not data.get(field) or not str(data.get(field)).strip():
                return jsonify({'error': f'{field.replace("_", " ").title()} is required'}), 400
        
        # Save to database
        registration_id = save_registration(data)
        
        # Send confirmation email (graceful failure)
        try:
            send_confirmation_email(data['email'], data['full_name'])
        except Exception as e:
            print(f"Email sending failed: {e}")
            # Continue anyway - data is saved
        
        return jsonify({
            'message': 'Registration successful! You will receive a confirmation email shortly.',
            'id': registration_id
        }), 200
        
    except Exception as e:
        print(f"Registration error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'WE-ICT 2026 Registration API'}), 200

if __name__ == '__main__':
    app.run(debug=False)

