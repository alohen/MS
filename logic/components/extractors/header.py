from dataclasses import dataclass, field
from request.request import Request, Identifier, Property
from typing import Optional
import re

@dataclass
class HeaderConfig:
    name: str
    regex: str
    property: Optional[str]
    identifier: Optional[str]

class Header:
    def __init__(self,config: HeaderConfig):
        self.name = config.name
        self.property = config.property
        self.identifier = config.identifier
        self.regex = re.compile(config.regex)

    def extract(self, request: Request) -> Request:
        header = request.headers.get(self.name, None)
        if not header:
            return request

        match = self.regex.search(header)
        if not match:
            return request

        extracted = match.group(1)

        if self.identifier:
            request.identifiers[self.identifier] = Identifier(name=self.identifier,value=extracted,included=True)

        if self.property:
            request.properties[self.property] = Property(name=self.property,value=extracted)

        return request