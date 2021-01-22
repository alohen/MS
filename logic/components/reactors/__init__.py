from logic.components.factory import ComponentFactory

REACTORS = {
}

FACTORY = ComponentFactory(REACTORS)
def create_reactor(name: str, config: dict):
    return FACTORY.create_instance(name, config)

def create_reactors(config: dict):
    return FACTORY.create_from_dict(config)
