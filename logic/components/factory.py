

class ComponentFactory:
    def __init__(self, creation_dict):
       self.creation_dict = creation_dict

    def create_instance(self, name: str, config: dict):
        construction_config = self.creation_dict.get(name, None)
        if not construction_config:
            return None

        parsed_config = construction_config[1](**config)
        instance = construction_config[0](parsed_config)
        return instance

    def create_from_dict(self, config: dict):
        instances = []
        for type_name, instance_configs in config.items():
            for instance_config in instance_configs:
                instance = self.create_instance(type_name, instance_config)
                if not instance:
                    continue

                instances.append(instance)

        return instances
