from app import app, mongo
from flask import request
from flask import jsonify



import sys
import json





    # def solutionMet(self,payload):
    #     ecle_error = mongo.db.ecle_error
    #     ecle_solution = mongo.db.ecle_solution

    #     errorid_solution = ecle_error.find_one({'errorName':payload['errorCode']})

    #     print("in solution")
    #     print(errorid_solution)
        
    #     solution_details = ecle_solution.find_one({'errorid':errorid_solution['_id']})

    #     solutionID = solution_details['_id']
    #     solution = solution_details['solution']
    #     creationTime = solution_details['creationTime']

    #     return solutionID,solution,creationTime


@app.route('/')
def hello():
    # ecle_error = mongo.db.students
    # ecle_error.insert_one({'rootId':'aakash'})
    return {"hello": "world"}

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        if request.get_json:

            data = request.get_json()

            ecle_error = mongo.db.students
            inserted = ecle_error.insert_one({'name':data['name'],
                                    'roll': data['roll'],
                                    'college':data['college']})


    return {"message": inserted.inserted_id}

@app.route('/getall',methods=['GET'])
def getall():
    getall = mongo.db.students

    output = []
    for stu in getall.find():
        output.append({'id':stu['_id'],'name':stu['name'],'roll':stu['roll'],'college':stu['college']})
  

    return jsonify(output)

        




        







        


  




        
        
       
        
    
















app.run(host='0.0.0.0',port=5000, debug = True),