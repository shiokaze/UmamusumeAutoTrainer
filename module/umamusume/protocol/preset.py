from pydantic import BaseModel


class AddPresetRequest(BaseModel):
    preset: str



