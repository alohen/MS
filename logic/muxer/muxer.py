from dataclasses import dataclass
from typing import List
from request.request import Request
from logic.muxer.common import create_recurring_types
from logic.muxer.domain import create_domains_from_config, DomainHandlerConfig


@dataclass
class MuxerConfig:
    extractors: str
    translators: str
    domains: List[DomainHandlerConfig]


class Muxer:
    def __init__(self):
        self.domains_to_handlers = dict()

    def add_domain(self, name, handler):
        self.domains_to_handlers[name] = handler

    def handle(self, request: Request):
        domain_handler = self.domains_to_handlers.get(request.host, None)
        if not domain_handler:
            print("domain not found")

        return domain_handler.handle(request)

def create_muxer_from_config(config: MuxerConfig):
    extractors, translators = create_recurring_types(config)
    domains = create_domains_from_config(config.domains, config_extractors=extractors,config_translators=translators)

    mux = Muxer()
    for domain in domains:
        mux.add_domain(domain.name, domain)
    return mux


