from pydantic import BaseModel


class AssignRequest(BaseModel):
    user_id: str
    bicycle_id: str


class AssignResponse(BaseModel):
    assignment_id: str


class ReleaseRequest(BaseModel):
    assignment_id: str


class UserBikeResponse(BaseModel):
    bicycle_id: str | None
