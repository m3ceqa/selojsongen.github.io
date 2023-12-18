# To test in server, enter command in root directory terminal
# python -m http.server
# Access Server: http://localhost:8000/

import json
from js import console
    
def my_function(*args, **kwargs):

    body = {
        "execution": [
            {
                "executionType": "SSO_SIMPLE",
                "smoke": [],
                "setup": [],
                "main": [],
                "after": []
            }
        ]
    }

    text = Element('area').element.value

    for line in text.splitlines():
        # option = line.strip()
        # option = text.splitlines()
        # option = line
        add_data = {
            "priorityNumber": 1,
            "testPlanName": f"{line}"+".xml",
        }

    
        body['execution'][0]['smoke'].append(add_data)

    final = json.dumps(body, indent = 4)
    # file.write(final)

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')

    console.log(f'text: {text}')

    Element('test-output').element.innerText = final
    # Element('test-output').element.innerText = JSON.stringify(final, undefined, 2)
    # document.getElementById("test-output").innerHTML = JSON.stringify(final, undefined, 2);
    # return final