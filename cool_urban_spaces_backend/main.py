#!/usr/bin/env python3

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

import cool_urban_spaces_backend.api.user

app = FastAPI()

app.include_router(cool_urban_spaces_backend.api.user.router)

app.mount("/", StaticFiles(directory="static"), name="static")
