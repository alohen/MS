from dataclasses import dataclass, field
from request.request import Request, Identifier, Property
from typing import Optional, List
import re

@dataclass
class RegexConfig:
    white_list: List[str]
    black_list: List[str]
    allow_missing: bool
    property: Optional[str]
    identifier: Optional[str]

class Regex:
    def __init__(self,config: RegexConfig):
        self.property = config.property
        self.identifier = config.identifier
        self.allow_missing = config.allow_missing

        self.white_list = self.complile_regex_list(config.white_list)
        self.black_list = self.complile_regex_list(config.black_list)

    def complile_regex_list(self, regexes):
        compiled_regexes = []
        for regex in regexes:
            compiled_regexes.append(re.compile(regex))
        return compiled_regexes


    def filter(self, request: Request):
        if self.identifier:
            return self.filter_identifier(request)

        return self.filter_property(request)

    def filter_property(self, request: Request):
        property = request.properties.get(self.property, None)
        if not property and not self. allow_missing:
            return f"missing property {self.property}"

        if self.white_list and not self.is_in_white_list(property):
                return f"property {self.property} not in whitelist"

        if self.black_list and self.is_in_black_list(property):
            return f"property {self.property} in blacklist"

    def filter_identifier(self, request: Request):
        identifier = request.identifiers.get(self.identifier, None)
        if not identifier and not self. allow_missing:
            return f"missing identifier {self.identifier}"

        if self.white_list and not self.is_in_white_list(identifier):
            return f"identifier {self.identifier} not in whitelist"

        if self.black_list and self.is_in_black_list(identifier):
            return f"identifier {self.identifier} in blacklist"

    def is_in_white_list(self, data):
        for regex in self.white_list:
            if regex.match(data.value):
                return True
        return False

    def is_in_black_list(self, data):
        for regex in self.black_list:
            if regex.match(data.value):
                return True
        return False
