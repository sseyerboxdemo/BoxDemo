# app.py
from flask import Flask, request
import hmac
import hashlib

app = Flask(__name__)
SHARED_SECRET = "YOUR_BOX_WEBHOOK_SECRET"

@app.route("/webhook", methods=["POST"])
def webhook():
    # OPTIONAL: Verify the Box signature
    signature = request.headers.get("Box-Signature", "")
    expected = hmac.new(
        SHARED_SECRET.encode(), request.data, hashlib.sha1
    ).hexdigest()
    if not hmac.compare_digest(signature, expected):
        return "Invalid signature", 403

    data = request.get_json()
    print("📦 Box Webhook Received:", data)
    return "OK", 200

if __name__ == "__main__":
    app.run()
