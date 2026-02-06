from datetime import datetime
from typing import Optional
from uuid import uuid4

from app.domain.models import (
    Assignment, AssignmentId, UserId, BicycleId, AssignmentStatus
)
from app.domain.policies import (
    ensure_no_active_assignment_for_user,
    ensure_no_active_assignment_for_bicycle
)


class AssignmentRepository:
    def find_active_by_user(self, user_id: UserId) -> Optional[Assignment]:
        raise NotImplementedError

    def find_active_by_bicycle(self, bicycle_id: BicycleId) -> Optional[Assignment]:
        raise NotImplementedError

    def save(self, assignment: Assignment) -> None:
        raise NotImplementedError


class AssignBicycle:
    def __init__(self, repo: AssignmentRepository):
        self.repo = repo

    def execute(self, user_id: UserId, bicycle_id: BicycleId) -> AssignmentId:
        ensure_no_active_assignment_for_user(
            self.repo.find_active_by_user(user_id)
        )
        ensure_no_active_assignment_for_bicycle(
            self.repo.find_active_by_bicycle(bicycle_id)
        )

        assignment = Assignment(
            id=AssignmentId(str(uuid4())),
            user_id=user_id,
            bicycle_id=bicycle_id,
            start_at=datetime.utcnow(),
            end_at=None,
            status=AssignmentStatus.ACTIVE,
        )

        self.repo.save(assignment)
        return assignment.id
