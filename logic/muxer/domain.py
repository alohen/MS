from dataclasses import dataclass
from typing import List, Dict
from request.request import Request
from logic.muxer.common import create_recurring_types
from logic.muxer.page import create_pages_from_config, PageHandlerConfig


@dataclass
class DomainHandlerConfig:
    extractors: str
    translators: str
    pages: List[PageHandlerConfig]
    domain: str


class DomainHandler:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def handle(self, request: Request):
        for page in self.pages:
            if not page.match(request):
                continue

            return page.handle(request)

        print("page not found")


def create_domain_from_config(config: DomainHandlerConfig, config_extractors=[], config_translators=[]):
    config = DomainHandlerConfig(**config)

    name = config.domain
    domain_extractors, domain_translators = create_recurring_types(config)
    pages = create_pages_from_config(
        config=config.pages,
        domain_extractors=config_extractors + domain_extractors,
        domain_translators=domain_translators + config_translators
    )

    return DomainHandler(name=name, pages=pages)


def create_domains_from_config(config: List[DomainHandlerConfig], config_extractors=[], config_translators=[]):
    domains = []
    for domain_config in config:
        domains.append(create_domain_from_config(domain_config, config_extractors, config_translators))

    return domains
