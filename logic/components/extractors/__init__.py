from logic.components.factory import ComponentFactory
from .header import Header, HeaderConfig

EXTRACTORS = {
    "header": (Header, HeaderConfig)
}

FACTORY = ComponentFactory(EXTRACTORS)
def create_extractor(name: str, config: dict):
    return FACTORY.create_instance(name, config)

def create_extractors(config: dict):
    return FACTORY.create_from_dict(config)

