import yaml
import bot.base.log as logger

log = logger.get_logger(__name__)


class Config(dict):
    def __getattr__(self, key):
        value = self.get(key, None)
        if isinstance(value, dict):
            value = Config(value)
        return value


def load() -> Config:
    config_file = open("config.yaml", 'r', encoding='utf-8')
    config = config_file.read()
    return Config(yaml.load(config, yaml.FullLoader))


CONFIG = load()
