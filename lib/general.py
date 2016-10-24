import yaml
from settings import CONF_FILEPATH


def get_websites_confs():
    with open(CONF_FILEPATH, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            return None

