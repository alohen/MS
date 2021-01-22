from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class Request:
    '''Object for tracking physical books in a collection.'''
    status_code: int
    id: str
    path: str
    host: str
    headers: Dict
    query_parameters: Dict
    body: str
    identifiers: Optional[Dict] = None
    properties: Optional[Dict] = None

@dataclass
class Identifier:
    name: str
    value: str
    included: bool

@dataclass
class Property:
    name: str
    value: str
