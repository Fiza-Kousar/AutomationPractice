"""
Add New Student(POST)
Fetch Student Details (GET)
Update Student Details (PUT)
Delete Student (DELETE)
"""






import requests
import json
import jsonpath

def test_add_student_data():
    API_URl="https://thetestingworldapi.com/api/studentsDetails" # https://thetestingworldapi.com (Base URL)
                                                                  # api/studentsDetails (Relative URL)
    f=open('//Users//fiza//Downloads//PycharmProjects//pythonProject//PytestLearning//RequestJSON.json','r')
    json_request = json.loads(f.read()) # typecasting into JSON format
    response = requests.post(API_URl,json_request)
    print(response.text)



def test_Update_Student_Data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7108632"

    f = open('//Users//fiza//Downloads//PycharmProjects//pythonProject//PytestLearning//RequestJSON.json','r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL,json_request)
    print(response.text)




def test_Delete_Student():

    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7108632"
    response = requests.delete(API_URL)
    print(response.text)



def test_getStudentData():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7108632"

    response = requests.get(API_URL)
    json_response = response.json()
   # json_response = json.loads(response.text)
    print(json_response)
    id= jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 7108632
    print(id)
