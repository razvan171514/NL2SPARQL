import requests

def send_post_request(file_path):
    url = "http://attempto.ifi.uzh.ch/service/owl_verbalizer/owl_to_ace"
    
    with open(file_path, 'r') as file:
        file_contents = file.read()
    
    data = {
        'xml': file_contents,
        'format': 'ace'
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        response_lines = response.text.split('\n')
        return [line for line in response_lines if line.strip() and not line.strip().startswith('/*')]
    return []

for l in send_post_request('../famylia_OWL_verb.owx'):
    print(l)
