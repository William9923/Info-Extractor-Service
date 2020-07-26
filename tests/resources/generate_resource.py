import json 
from typing import Dict, Any, Tuple, List
from pprint import pprint
from pathlib import Path

def generate_tokenize_resource() -> List[Dict[str,Any]]:
    filename = Path.cwd() / "tests" / "resources" / "tokenize.json"
    return generate_resource(filename)

def generate_text_resource() -> List[Dict[str, Dict[str,Any]]]:
    filename = Path.cwd() / "tests" / "resources" / "text_preprocessor.json"
    return generate_resource(filename)

def generate_url_resource() -> List[Dict[str, Dict[str,Any]]]:
    filename = Path.cwd() / "tests" / "resources" / "url_preprocessor.json"
    return generate_resource(filename)

def generate_service_resource() -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
    filename = Path.cwd() / "tests" / "resources" / "service_resource.json"
    return generate_resource(filename)

def generate_resource(filename: str) -> Dict[str,Any]:
    with open(filename, 'r') as f:
        datastore = json.load(f)
        return datastore

