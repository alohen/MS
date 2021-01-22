from logic.components.factory import ComponentFactory
from .regex import Regex, RegexConfig

FILTERS = {
    "regex": (Regex, RegexConfig)
}

FACTORY = ComponentFactory(FILTERS)
def create_filter(name: str, config: dict):
    return FACTORY.create_instance(name, config)

def create_filters(config: dict):
    return FACTORY.create_from_dict(config)
