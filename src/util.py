#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np

from PIL import Image

SRC_DIR = 'img'
DEST_DIR = 'result'

def get_filenames():
    """Return list of tuples for source and template destination
       filenames(absolute filepath). Only include jpg or png extensions - Siyu """
    file_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir, _ = os.path.split(file_dir)
    src_path = os.path.join(parent_dir, SRC_DIR)
    dest_path = os.path.join(parent_dir, DEST_DIR)

    os.makedirs(dest_path, exist_ok=True)

    image_names = os.listdir(src_path)

    filenames = []
    for name in image_names:
        base, ext = os.path.splitext(name)

        if ext == '.png' or ext == '.jpg':
            tempname = base + '-%s' + ext
            filenames.append((os.path.join(src_path, name),
                              os.path.join(dest_path, tempname)))
    return filenames
