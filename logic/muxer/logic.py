from dataclasses import dataclass
from typing import Dict
from request.request import Request
import logic.components.filters
import logic.components.reactors

@dataclass
class LogicConfig:
    filters: Dict[str,Dict]
    reactors: Dict[str,Dict]
    builder: str

class Logic:
    def __init__(self, name, filters, reactors, builder):
        self.name = name
        self.filters = filters
        self.reactors = reactors
        self.builder = builder

    def filter(self, request: Request):
        fail_reasons = []

        for filter in self.filters:
            fail_reason = filter.filter(request)
            if fail_reason:
                fail_reasons.append(fail_reason)

        return fail_reasons

    def react(self, request: Request):
        fail_reasons = []

        for reactor in self.reactors:
            fail_reason = reactor.react(request)
            if fail_reason:
                fail_reasons.append(fail_reason)

        return fail_reasons

    def build(self, request: Request) -> str:
        return "legit built response"

    def handle(self, request: Request):
        filter_fail_reasons = self.filter(request)
        if filter_fail_reasons:
            return None, filter_fail_reasons

        response = self.build(request)
        react_fail_reasons = self.react(request)

        return response, react_fail_reasons

def create_logic_from_config(name: str, config: LogicConfig):
    config = LogicConfig(**config)

    filters = logic.components.filters.create_filters(config.filters)
    reactors = logic.components.reactors.create_reactors(config.reactors)
    builder = config.builder

    return Logic(name=name, filters=filters,reactors=reactors,builder=builder)

def create_logics_from_config(config: Dict[str,LogicConfig]):
    logics = []
    for name, logic_config in config.items():
        logics.append(create_logic_from_config(name,logic_config))

    return logics