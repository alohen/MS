import os
from request.testing import sample_request
from logic.muxer.muxer import create_muxer_from_config, MuxerConfig

import json

CONFIG_PATH = b"config/main.json"


def main():
    config = load_config()
    muxer = create_muxer_from_config(MuxerConfig(**config))
    response = muxer.handle(sample_request)
    print(response)

def load_config():
    working_directory = os.getcwdb()
    print(working_directory)

    config_path = os.path.join(working_directory, CONFIG_PATH)

    with open(config_path) as config_file:
        data = json.load(config_file)

    return data


if __name__ == "__main__":
    main()
