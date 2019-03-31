import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent.parent
config_path = BASE_DIR / "db.yaml"
server_path = BASE_DIR / "server.yaml"


def get_config(path):
    with open(path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config


server_config = get_config(server_path)
config = get_config(config_path)
