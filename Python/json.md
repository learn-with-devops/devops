## Python JSON Modules

JSON (JavaScript Object Notation) is frequently used between a server and a web application.

### Importent

        JSON	         Python
        ----             ------
        object	         dict
        array	         list
        string	         str
        number (int)	 int
        number (real)	 float
        true	         True
        false	         False
        null	         None

### An example of JSON data:

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
        
### Convert the JSON data to Directory

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


### Real Time Scenario ( Read a Json File and do modifications on that and convert again to JSON file.)

    Reference : https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON
    youtube :  https://www.youtube.com/watch?v=9N6a-VLBa2I
    
                import json

                with open('states.json') as f:
                    data = json.load(f)
                    print(type(data))
                    print(data)

                for st in data['states']:
                    # print(st['name'], st['abbreviation'])
                    del st['abbreviation']
                    print(st)

                with open('new_states.json', 'w') as f:
                    json.dump(data, f, indent=2)
    
    
### Example 2

        import json

        with open('wiki.json') as w:
            data = json.load(w)

        #print(type(data))

        # tt = json.loads(data)
        #print(type(json.dumps(data, indent=2)))

        #a = json.dumps(data, indent=2)
        # print(a)

        #print(len(data['dataset']['data']))

        date_n = dict()
        for item in data['dataset']['data']:
            #print(item)
            date = item[0]
            count = item[2]
            date_n[date]= count

        print(date_n['2005-01-03'])


        #    print("Current_date    ", date ," ", count )
        
        Ref: https://www.youtube.com/watch?v=9N6a-VLBa2I
