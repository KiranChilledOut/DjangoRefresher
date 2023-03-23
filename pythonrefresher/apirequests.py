import json
import requests

person = {
    'firstname' : 'kiran raj',
    'lastname' : 'Rajendran'
}

print(person)

jsonresult = json.dumps(person)
print(jsonresult)

stringresult=json.loads(jsonresult)
print(stringresult)

url = "https://jsonplaceholder.typicode.com/todos"
apioutput = requests.get(url)
apijson = apioutput.json()
for item in apijson:
    print(item["title"])