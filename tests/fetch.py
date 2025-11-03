from flask import Flask, render_template, jsonify, url_for
import requests
import os

app = Flask(__name__, template_folder="templates")

# Remote API (ngrok) - change as needed or set REMOTE_API env var
REMOTE_API = os.environ.get("REMOTE_API", "https://36ca8cba74f2.ngrok-free.app/api/dustbin/")

@app.route("/")
def index():
    # provide the proxy route to the template so JS uses the local proxy (avoids CORS)
    return render_template("index.html", proxy_url=url_for("proxy"))

@app.route("/proxy")
def proxy():
    """Fetch remote API and return JSON to the browser (acts as a CORS-free proxy)."""
    try:
        resp = requests.get(REMOTE_API, headers={"Accept": "application/json"}, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "fetch_failed", "message": str(e)}), 502

    content_type = resp.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        text = resp.text
        return jsonify({
            "error": "non_json_response",
            "message": "Remote returned non-JSON content",
            "preview": text[:800]
        }), 502

    try:
        return jsonify(resp.json())
    except ValueError:
        return jsonify({"error": "invalid_json", "message": "Could not parse JSON from remote"}), 502

if __name__ == "__main__":
    # development server
    app.run(host="127.0.0.1", port=5000, debug=True)
