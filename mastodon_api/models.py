# pylint: disable=too-few-public-methods
from typing import List
from pydantic import BaseModel, Field


class Member(BaseModel):
    """
    Model to members and ex-members of Mastodon
    """
    id: int = Field(..., alias='_id')
    name: str = Field(...)
    birth_date: str = Field(...)
    instruments: List[str] = Field(...)
    first_year: str = Field(...)
    last_year: str = Field(...)
    discography: List[str] = Field(...)


class Album(BaseModel):
    """
    Model to albums of Mastodon
    """
    id: int = Field(..., alias='_id')
    name: str = Field(...)
    release_date: str = Field(...)
    length: str = Field(...)
    labels: List[str] = Field(...)
    members: List[str] = Field(...)
    track_list: List[str] = Field(...)
