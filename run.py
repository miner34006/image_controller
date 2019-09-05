import os
from app import app

# Get port from env vars, default = 5000
PORT = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=PORT)
 