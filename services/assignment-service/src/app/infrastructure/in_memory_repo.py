from typing import List, Optional
from app.application.use_cases import AssignmentRepository
from app.domain.models import (
    Assignment, AssignmentId, UserId, BicycleId, AssignmentStatus
)


class InMemoryAssignmentRepository(AssignmentRepository):
    def __init__(self):
        self._items: List[Assignment] = []

    def find_active_by_user(self, user_id: UserId) -> Optional[Assignment]:
        return next(
            (a for a in self._items
             if a.user_id == user_id and a.status == AssignmentStatus.ACTIVE),
            None
        )

    def find_active_by_bicycle(self, bicycle_id: BicycleId) -> Optional[Assignment]:
        return next(
            (a for a in self._items
             if a.bicycle_id == bicycle_id and a.status == AssignmentStatus.ACTIVE),
            None
        )

    def get_by_id(self, assignment_id: AssignmentId) -> Optional[Assignment]:
        return next((a for a in self._items if a.id == assignment_id), None)

    def list_active(self) -> List[Assignment]:
        return [a for a in self._items if a.status == AssignmentStatus.ACTIVE]

    def save(self, assignment: Assignment) -> None:
        self._items.append(assignment)
