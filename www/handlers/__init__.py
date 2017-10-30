#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Shawling'

' url handlers '

from apis import Page, APIValueError, APIResourceNotFoundError
from aiohttp import web
from config import configs
import logging

import markdown

logging.basicConfig(level=logging.WARNING)
