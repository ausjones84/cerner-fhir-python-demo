# 🏥 Cerner FHIR Python Demo

This project is a simple Python demo that connects to the **Cerner FHIR API** using OAuth 2.0 credentials stored in a `.env` file.  
It shows how to authenticate, retrieve data, and interact with FHIR endpoints securely.

---

## 🚀 Features
- Connects to Cerner’s FHIR API using OAuth 2.0  
- Loads credentials securely with `python-dotenv`  
- Uses `requests` for RESTful API calls  
- Modular design for easy integration with other apps  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ausjones84/cerner-fhir-python-demo.git
cd cerner-fhir-python-demo

Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Create a .env File

Add your environment variables inside a new .env file:

CERNER_TOKEN_URL=<your_token_url>
CERNER_FHIR_BASE=<your_fhir_base_url>
CERNER_CLIENT_ID=<your_client_id>
CERNER_CLIENT_SECRET=<your_client_secret>
CERNER_SCOPE=<your_scope>

5️⃣ Run the Script
python main.py

🧠 Example Output

When successfully connected, you’ll see:

✅ Successfully connected! Token: <token_here>
--- Demo Completed ---


If credentials or the URL are invalid:

⚠️ Error connecting: Invalid URL or credentials.

📦 Dependencies

The project uses:

requests

python-dotenv

pathlib

You can find them listed in requirements.txt.

👨‍💻 Author

Austin Jones
