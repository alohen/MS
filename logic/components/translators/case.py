from dataclasses import dataclass, field
from request.request import Request, Identifier, Property
from typing import Optional
import re

@dataclass
class CaseConfig:
    case: str
    property: Optional[str]
    identifier: Optional[str]

class Case:
    def __init__(self,config: CaseConfig):
        self.property = config.property
        self.identifier = config.identifier
        self.__set_change_func(config.case)

    def __set_change_func(self, case):
        if case == "upper":
            self.change_func = self.to_upper
        elif case == "lower":
            self.change_func = self.to_lower
        else:
            raise ValueError("case must be lower or upper")

    def translate(self, request: Request) -> Request:
        if self.identifier:
            request.identifiers[self.identifier] = self.change_func(request.identifiers[self.identifier])

        if self.property:
            request.properties[self.property] = self.change_func(request.properties[self.property])

        return request

    @staticmethod
    def to_upper(obj):
        obj.value = obj.value.upper()
        return obj

    @staticmethod
    def to_lower(obj):
        obj.value = obj.value.lower()
        return obj
