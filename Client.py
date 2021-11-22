import requests
import random, string 

def get_token():
    tokenEndPoint = f'{baseURL}/api/token/'
    response = requests.post(tokenEndPoint, data={'username': 'admin', 'password': 'app123'})
    token = response.json()['access']
    return token

#get data
def get_data():
    getEndPoint = f'{baseURL}/api/member/'
    header = {'Authorization': f'Bearer {get_token()}'}
    response = requests.get(getEndPoint, headers = header)
    emp_data = response.json()
    for e in emp_data:
        print(e)

#post(add) data
def post_data(random_mrn, random_name, random_dob):
    postEndPoint = f'{baseURL}/api/member/'
    header = {'Authorization': f'Bearer {get_token()}'}
    data = {
        'mrn': f'{random_mrn}', 'name': f'{random_name}', 'dob': 68 + seq
    }
    response = requests.post(postEndPoint, data = data, headers = header)
    print(response.text, response.status_code)

#edit data
def edit_data(mrn, name, ranking, dob):
    editEndPoint = f'{baseURL}/api/member/{mrn}/'
    header = {'Authorization': f'Bearer {get_token()}'}
    data = {
        'name': f'{name}', 'dob': {dob}
    }
    response = requests.put(editEndPoint, data = data, headers = header)
    print(response.text, response.status_code)

#delete data
def delete_data(mrn):
    deleteEndPoint = f'{baseURL}/api/member/{mrn}/'
    header = {'Authorization': f'Bearer {get_token()}'}
    response = requests.delete(deleteEndPoint, headers = header)
    print(response.text, response.status_code)

def get_random_name(name_len):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(name_len)).capitalize()

def get_random_dob():
    pass

if __name__ == "__main__":
    baseURL = 'http://127.0.0.1:8000'
    # print(get_token())
    random_mrn = random.randint(1000, 10000)
    random_name = f'{get_random_name(3)} {get_random_name(6)}'
    random_dob = ''
    post_data(random_mrn, random_name, random_dob)
    get_data()

