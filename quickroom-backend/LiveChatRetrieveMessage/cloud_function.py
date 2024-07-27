import json
from google.cloud import firestore

def get_messages(request):
    try:
        # Get user ID and role from query parameters
        user_id = request.args.get('user_id')
        role = request.args.get('role')

        if not user_id:
            return json.dumps({"error": "No user_id provided"}), 400, {'Content-Type': 'application/json'}
        
        if not role:
            return json.dumps({"error": "No role provided"}), 400, {'Content-Type': 'application/json'}

        # Initialize Firestore client
        db = firestore.Client()

        # Reference the user document
        user_ref = db.collection('messages').document(user_id)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            if role == 'user':
                messages = user_data.get('user_messages', [])
            elif role == 'agent':
                messages = user_data.get('agent_messages', [])
            else:
                return json.dumps({"error": "Invalid role provided"}), 400, {'Content-Type': 'application/json'}

            return json.dumps({"messages": messages}), 200, {'Content-Type': 'application/json'}
        else:
            return json.dumps({"error": "User with ID does not exist"}), 404, {'Content-Type': 'application/json'}

    except Exception as e:
        return json.dumps({"error": str(e)}), 500, {'Content-Type': 'application/json'}
