import requests
import json
import logging
import os

def setup_api_session(api_key=None):
    """Setup and return a requests session for API calls, with authorization headers included if an API key is provided."""
    session = requests.Session()
    if api_key:
        session.headers.update({'Authorization': f'Bearer {api_key}'})
    return session

def make_api_request(session, url, method='GET', data=None):
    """Make an API request using the provided session, URL, and method. Handles GET and POST requests."""
    try:
        if method.upper() == 'POST':
            response = session.post(url, json=data)
        else:
            response = session.get(url)
        
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        logging.error(f'API request failed: {e}')
        return None

def load_configuration(file_path):
    """Load configuration from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f'Configuration file not found: {file_path}')
    except json.JSONDecodeError:
        logging.error('Error decoding JSON from the configuration file.')
    return {}

def save_configuration(config, file_path):
    """Save a configuration dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
        logging.info(f'Successfully saved configuration to {file_path}')
    except IOError as e:
        logging.error(f'Failed to write to file {file_path}: {e}')

def get_env_variable(var_name, default=None):
    """Retrieve an environment variable or return a default if it's not found."""
    return os.getenv(var_name, default)

# Example usage of the utilities
if __name__ == '__main__':
    # Example for API session setup and request
    session = setup_api_session(get_env_variable('API_KEY'))
    api_response = make_api_request(session, 'https://api.example.com/data')
    print(api_response)

    # Load and save configuration example
    config = load_configuration('config.json')
    config['new_setting'] = 'new_value'
    save_configuration(config, 'config_updated.json')
