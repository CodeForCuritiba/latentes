#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests



def download_file(url, folder=None, name_override=None, force_overwrite=False):
    """ Downloads a file from a website
    params:
        - url (mandatory)
        - folder - Destination folder;
        - name_override - If provided, override the name of file,
                          if not pick latest part of url
        - force_overwrite - (bool) - Default False
    returns:
        - local_filename - The path of downloaded file
        - file_encoding
    """
    local_filename = url.split('/')[-1] if not name_override else name_override
    local_filename = local_filename if not folder \
        else f'{folder}/{local_filename}'

    print('Downloading File...')

    file_encoding = None
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_encoding = r.encoding

        if os.path.isfile(local_filename):
            print('File Already exists!')

            if not force_overwrite:
                print('No download needed.')
                return local_filename, file_encoding
            else:
                print('Forcing download anyway...')

        with open(local_filename, 'wb') as file_handler:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    file_handler.write(chunk)

    print('Download Sucessful')
    return local_filename, file_encoding

