from fastapi import FastAPI, HTTPException
from app.api.schemas import (
    AssignRequest, AssignResponse, ReleaseRequest, UserBikeResponse
)
from app.application.use_cases import (
    AssignBicycle, ReleaseBicycle, ListBikesInUse, GetUserBike
)
from app.infrastructure.in_memory_repo import InMemoryAssignmentRepository
from app.domain.models import UserId, BicycleId, AssignmentId

app = FastAPI(title="Assignment Service", version="0.1.0")

_repo = InMemoryAssignmentRepository()

_assign_uc = AssignBicycle(_repo)
_release_uc = ReleaseBicycle(_repo)
_list_uc = ListBikesInUse(_repo)
_user_bike_uc = GetUserBike(_repo)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/assign", response_model=AssignResponse)
def assign(req: AssignRequest):
    try:
        assignment_id = _assign_uc.execute(UserId(req.user_id), BicycleId(req.bicycle_id))
        return AssignResponse(assignment_id=assignment_id.value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/release")
def release(req: ReleaseRequest):
    try:
        _release_uc.execute(AssignmentId(req.assignment_id))
        return {"status": "released"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bikes-in-use")
def bikes_in_use():
    try:
        return {"bicycles": _list_uc.execute()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/user-bike/{user_id}", response_model=UserBikeResponse)
def user_bike(user_id: str):
    try:
        bike = _user_bike_uc.execute(UserId(user_id))
        return UserBikeResponse(bicycle_id=bike)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
