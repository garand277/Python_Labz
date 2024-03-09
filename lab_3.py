import requests, ast

def get_response():
    response = 0
    def get_body():
        nonlocal response
        response = requests.get('https://dogapi.dog/api/v2/facts')
        dictionary = ast.literal_eval(response.text)
        body = dictionary['data'][0]['attributes']['body']
        print(body)
    return get_body

dog_facts = get_response()
dog_facts()
dog_facts()
dog_facts()
dog_facts()
dog_facts()
