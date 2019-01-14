from flask import Flask
from flask import jsonify
from flask import request



app = Flask(__name__)

"""
Provides a REST API for the underlying LOLC 
algorithms. 
Used for generating,
1) Profile Score
2) Loan Eligibility Score

To run the server, use: 
FLASK_APP=lolc_flask.py flask run
"""

@app.route("/get_profile_score/<instance_id>")
def get_profile_score(instance_id):
   
    profile_score = 7

    return jsonify(profile_score=profile_score)


@app.route("/get_loan_eligibility_score/<instance_id>")
def get_loan_eligibility_score(instance_id):
    """
    Method used to generate loan eligibility score for a consumer
    based on their existing profile information.

    Reuest Parameters
    ----------
    instance_id: Unique identifier for consumer, string 
    """
    
    
    loan_eligibility_score = 0.8

    return jsonify(loan_eligibility_score=loan_eligibility_score)


if __name__ == '__main__':
    app.run()
