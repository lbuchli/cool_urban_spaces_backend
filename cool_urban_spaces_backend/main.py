#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import cool_urban_spaces_backend.api.user

app = FastAPI()

app.mount("/", StaticFiles(directory="static"), name="static")

