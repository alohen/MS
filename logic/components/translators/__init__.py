from logic.components.factory import ComponentFactory
from .case import Case, CaseConfig

TRANSLATORS = {
    "case": (Case, CaseConfig)
}

FACTORY = ComponentFactory(TRANSLATORS)
def create_translator(name: str, config: dict):
    return FACTORY.create_instance(name, config)

def create_translators(config: dict):
    return FACTORY.create_from_dict(config)
