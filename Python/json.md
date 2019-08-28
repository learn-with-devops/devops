## Python JSON Modules

### Importent

        JSON	Python
        ----    ------
        object	dict
        array	list
        string	str
        number (int)	int
        number (real)	float
        true	True
        false	False
        null	None

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

### Convert JSON to Python Object (Dict)
    
    To convert JSON to a Python dict use this:

        import json

        json_data = '{"name": "Brian", "city": "Seattle"}'
        python_obj = json.loads(json_data)
        print python_obj["name"]
        print python_obj["city"]


### My Example

        import json

        people_string = '''
        {
            "people": [
                {
                    "name": "Anand",
                    "phone": "989898",
                    "mail": ["anand@hcl.com","anandr@hpe.com"],
                    "Address": "Bangalore"
                },
                {
                    "name": "Balu",
                    "phone": "99009",
                    "mail": null,
                    "Addess": "hyd"
                }
            ]
        }
        '''

        data = json.loads(people_string)    // Convert the JSON data to Directory
        print(type(data))
        print(data)
        print("-------------------------")

        print(type(data['people']))

        print("-------------------------")

        for peop in data['people']:
            print(peop['name'])

        for p in data['people']:
            del p['phone']       // Delete a specific string 

        new = json.dumps(data, indent=2, sort_keys=True)  // String/list to JSON Data
        print(new)
