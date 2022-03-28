# -*- coding: utf-8 -*-

import os
import pathlib
import shutil
import re

global ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
global INPUT
INPUT = os.path.join(ROOT_DIR, "input/")
global OUTPUT
OUTPUT = os.path.join(ROOT_DIR, "output/")
pathlib.Path(OUTPUT).mkdir(parents=True, exist_ok=True)
    
def run():
    for filename in os.listdir(INPUT):
        with open(os.path.join(INPUT, filename), 'r') as f:
            new_title = None
            for line in f:
                if re.search("title", line):
                    new_title = line.replace("title: ", "")
                    new_title = re.sub("^第", "", new_title)
            if not new_title:
                new_title = filename.replace(".md","")
            shutil.copy(os.path.join(INPUT, filename),os.path.join(OUTPUT, new_title.strip() + ".txt"))

if __name__ == "__main__":
    run()
