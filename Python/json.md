# Python JSON Modules


JSON (JavaScript Object Notation) is frequently used between a server and a web application. An example of JSON data:

        {
            "persons": [
                {
                    "city": "Seattle", 
                    "name": "Brian"
                }, 
                {
                    "city": "Amsterdam", 
                    "name": "David"
                }
            ]
        }
        
The json module enables you to convert between JSON and Python Objects.

Convert JSON to Python Object (Dict)
To convert JSON to a Python dict use this:

        import json

        json_data = '{"name": "Brian", "city": "Seattle"}'
        python_obj = json.loads(json_data)
        print python_obj["name"]
        print python_obj["city"]
