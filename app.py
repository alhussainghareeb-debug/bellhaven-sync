import json
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

API_TOKEN = "bh_P2Lz48fRF1VSQgNjk0t00g"
BASE_URL = "https://analyst-assessment-production.up.railway.app/api/v1"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Bellhaven CRM Sync Review Queue</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f9; margin: 0; padding: 20px; color: #333; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        h1 { color: #004080; }
        .card { border: 1px solid #ddd; padding: 20px; margin-bottom: 20px; border-radius: 6px; background: #fafafa; }
        .tag { display: inline-block; padding: 4px 8px; font-size: 12px; font-weight: bold; border-radius: 4px; color: white; background: #e67e22; }
        .btn { padding: 10px 18px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 14px; }
        .btn-approve { background: #27ae60; color: white; margin-right: 10px; }
        .btn-reject { background: #c0392b; color: white; }
        .btn:hover { opacity: 0.9; }
    </style>
</head>
<body>
<div class="container">
    <h1>Bellhaven Sync Review Queue</h1>
    <p>Review proposed updates and CHOW rules before writing back to the CRM API.</p>
    <hr>
    
    <div class="card">
        <h3>Sample Proposal: Amberly Care Center <span class="tag">Needs Review</span></h3>
        <p><strong>Current Parent:</strong> Stonebridge Eldercare</p>
        <p><strong>Proposed Change:</strong> Update parent to Bellhaven Senior Living (CHOW Rule Applied)</p>
        <p><strong>Revenue / AR:</strong> $0 / $0 (Safe for direct re-parenting)</p>
        <br>
        <button class="btn btn-approve" onclick="alert('Proposal Approved & Written to CRM API!')">Approve & Write</button>
        <button class="btn btn-reject" onclick="alert('Proposal Rejected.')">Reject</button>
    </div>
</div>
</body>
</html>
"""


@app.route("/")
def index():
  return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
  print("Starting local review app at http://127.0.0.1:5000 ...")
  app.run(port=5000, debug=True)