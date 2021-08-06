import pathlib
import random
import json



class Database():
    db = "db"

    def model_return(self):
        pass

    def store(self, data):
        file_data = pathlib.Path("registration.txt")
        data["userid"] = 1234

        with open('registration.txt', 'w') as outfile:
            json.dump(data, outfile)

        return {
            "code": 200,
            "userid": data.get("userid"),
            "message": "registered"
        }

    def assessment_data(self, data):
        file_data = pathlib.Path("file.txt")
        if not file_data:
            file_data.write("file.txt", "w+")
            pass
        
        with open('file.txt', 'w') as outfile:
            json.dump(data, outfile)

        return {
            "code": 200,
            "message": "stored success"
        }
 

        
            
 



