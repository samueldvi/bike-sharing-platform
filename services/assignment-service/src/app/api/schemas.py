from pydantic import BaseModel


class AssignRequest(BaseModel):
    user_id: str
    bicycle_id: str


class AssignResponse(BaseModel):
    assignment_id: str
