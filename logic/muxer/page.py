from dataclasses import dataclass
from typing import Dict, List
from request.request import Request
from logic.muxer.common import create_recurring_types
from logic.muxer.logic import create_logics_from_config, LogicConfig
import re

@dataclass
class PageHandlerConfig:
    regex: str
    extractors: Dict[str,Dict]
    translators: Dict[str,Dict]
    logics: Dict[str,LogicConfig]


class PageHandler:
    def __init__(self, regex, extractors, translators, logics):
        self.regex = re.compile(regex)
        self.extractors = extractors
        self.translators = translators
        self.logics = logics

    def match(self, request: Request):
        match = self.regex.match(request.path)
        return bool(match)

    def extract(self, request: Request) -> Request:
        for extractor in self.extractors:
            request = extractor.extract(request)

        return request

    def translate(self, request: Request) -> Request:
        for translator in self.translators:
            request = translator.translate(request)

        return request

    def handle(self, request):
        request = self.extract(request)
        request = self.translate(request)

        print(request)

        for logic in self.logics:
            response, fail_reasons = logic.handle(request)
            print(fail_reasons)
            if response:
                return response

        return "empty response"


def create_page_from_config(config: PageHandlerConfig, domain_extractors=[], domain_translators=[]):
    config=PageHandlerConfig(**config)

    regex = config.regex
    page_extractors, page_translators = create_recurring_types(config)
    logics = create_logics_from_config(config.logics)

    return PageHandler(
        regex=regex,
        extractors=domain_extractors + page_extractors,
        translators=domain_translators + page_translators,
        logics=logics
    )

def create_pages_from_config(config: List[PageHandlerConfig], domain_extractors=[], domain_translators=[]):
    pages = []
    for page_config in config:
        pages.append(create_page_from_config(page_config,domain_extractors,domain_translators))

    return pages
