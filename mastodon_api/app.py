from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

from .models import Album, Member
from . import db

from typing import List, Optional

from decouple import config

description = """
A Public API to consult infos about the awesome band Mastodon.
"""

app = FastAPI(
    title="Mastodon API",
    description=description,
    version="0.1.0",
    contact={
        "name": "Pery Lemke",
        "email": "pery.lemke@gmail.com",
    },
    docs_url="/",
    redoc_url=None
)

# Config CORS
origins = [
    "http://mastodon-api.com",
    "https://mastodon-api.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = config(
    'API_URL',
    default='http://localhost:8080',
    cast=str
)


@app.get('/api/', include_in_schema=False)
def home():
    home_text = {
        'Albums': f'{API_URL}/api/albums/',
        'Members': f'{API_URL}/api/members/'
    }
    return home_text


@app.get('/api/healthz/', include_in_schema=False)
def status():
    return {'Message': "It's Alive!"}


@app.get('/api/albums/', response_model=List[Album])
async def get_albums(
    name: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        regex="^[\sa-zA-Z]*\D\S$")
):
    if name:
        albums_res = await db.mastodondb.albums.find(
            {'name': {'$regex': name, '$options': 'i'}}).to_list(1000)
        if not albums_res:
            raise HTTPException(status_code=404, detail="Album not found.")
    else:
        albums_res = await db.mastodondb.albums.find().to_list(1000)
    return albums_res


@app.get('/api/albums/{id}/', response_model=Album)
async def get_albums_by_id(
    id: int = Path(..., ge=1)
):
    album_res = await db.mastodondb.albums.find_one({'_id': id})
    if not album_res:
        raise HTTPException(status_code=404, detail="Album not found.")
    return album_res


@app.get('/api/members/', response_model=List[Member])
async def get_members(
    name: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        regex="^[\sa-zA-Z]*\D\S$")
):
    if name:
        members_res = await db.mastodondb.members.find(
            {'name': {'$regex': name, '$options': 'i'}}).to_list(1000)
        if not members_res:
            raise HTTPException(status_code=404, detail="Member not found.")
    else:
        members_res = await db.mastodondb.members.find().to_list(1000)
    return members_res


@app.get('/api/members/{id}/', response_model=Member)
async def get_members_by_id(
    id: int = Path(..., ge=1)
):
    member_res = await db.mastodondb.members.find_one({'_id': id})
    if not member_res:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member_res
