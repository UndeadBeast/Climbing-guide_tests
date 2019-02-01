# -*- coding: utf-8 -*-
import os
from pathlib import Path
from shutil import copyfile
import yaml


class Config:
    def __init__(self):
        script_path = os.path.dirname(os.path.dirname(__file__))
        local_config = Path(os.path.join(script_path, 'common.yaml'))
        if not local_config.is_file():
            default_config = Path(os.path.join(script_path, 'default.yaml'))
            copyfile(default_config, local_config)

        with open(local_config, 'r') as stream:
            data_loaded = yaml.load(stream)
            self.main_url = data_loaded['cgn']['host']
            self.user = data_loaded['account']['username']
            self.password = data_loaded['account']['password']
            self.email = data_loaded['account']['email']
