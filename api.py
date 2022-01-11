from flask import Flask, json

companies = [{"id": 1, "name": "Jad Cloud Tech"}, {"id": 2, "name": "JAD"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080) 
