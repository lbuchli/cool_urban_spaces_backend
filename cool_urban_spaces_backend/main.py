#!/usr/bin/env python3

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import cool_urban_spaces_backend.api.user
import cool_urban_spaces_backend.api.suggestion
import cool_urban_spaces_backend.api.messages

app = FastAPI()

origins = [
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cool_urban_spaces_backend.api.user.router)
app.include_router(cool_urban_spaces_backend.api.suggestion.router)
app.include_router(cool_urban_spaces_backend.api.messages.router)
