import re

def getResponses(valid_auth_tokens, requests):
    results = []

    for request in requests:
        request_type, url = request[0], request[1]

        params = re.findall(r'\?(.*?)(?:&|$)', url)
        params_dict = {}
        if params:
            params_list = params[0].split('&')
            for param in params_list:
                key, value = param.split('=')
                params_dict[key] = value

        auth_token = params_dict.get('token', None)
        csrf_token = params_dict.get('csrf_token', None) if request_type == 'POST' else None

        if auth_token and auth_token in valid_auth_tokens:
            if request_type == 'POST' and (csrf_token is None or not re.match("^[a-zA-Z0-9]{8,}$", csrf_token)):
                results.append("INVALID")
            else:
                results.append(f"VALID {', '.join([f'{key}, {value}' for key, value in params_dict.items()])}")
        else:
            results.append("INVALID")

    return results
