import logic.components.extractors
import logic.components.translators

def create_recurring_types(config):
    extractors = logic.components.extractors.create_extractors(config.extractors)
    translators = logic.components.translators.create_translators(config.translators)
    return extractors, translators
