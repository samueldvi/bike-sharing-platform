from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class AssignmentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


@dataclass(frozen=True)
class AssignmentId:
    value: str


@dataclass(frozen=True)
class UserId:
    value: str


@dataclass(frozen=True)
class BicycleId:
    value: str


@dataclass
class Assignment:
    id: AssignmentId
    user_id: UserId
    bicycle_id: BicycleId
    start_at: datetime
    end_at: Optional[datetime]
    status: AssignmentStatus

    def release(self, end_at: datetime):
        if self.status != AssignmentStatus.ACTIVE:
            raise ValueError("Assignment is not active")
        self.end_at = end_at
        self.status = AssignmentStatus.CLOSED
