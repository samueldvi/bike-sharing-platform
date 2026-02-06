from fastapi import FastAPI, HTTPException
from app.api.schemas import AssignRequest, AssignResponse
from app.application.use_cases import AssignBicycle
from app.infrastructure.in_memory_repo import InMemoryAssignmentRepository
from app.domain.models import UserId, BicycleId

app = FastAPI(title="Assignment Service", version="0.1.0")

_repo = InMemoryAssignmentRepository()
_assign_uc = AssignBicycle(_repo)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/assign", response_model=AssignResponse)
def assign(req: AssignRequest):
    try:
        assignment_id = _assign_uc.execute(
            UserId(req.user_id),
            BicycleId(req.bicycle_id),
        )
        return AssignResponse(assignment_id=assignment_id.value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
