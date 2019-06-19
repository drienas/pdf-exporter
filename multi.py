import pandas as pd
from flask import Flask, request, make_response
from flask_cors import CORS

def format_data(data):
  df = pd.DataFrame(data["rows"])
  df = df[data['keep']]
  df.rename(columns=data['cols'], inplace=True)
  return df

app = Flask(__name__)
CORS(app)

@app.route('/csv', methods=['POST'])
def post(): 
  data = format_data(request.json)
  resp = make_response(data.to_csv(encoding='utf-8-sig', index=False))
  resp.headers["Content-Type"] = "text/csv; charset=utf-8-sig"
  return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0',
          port=3103)