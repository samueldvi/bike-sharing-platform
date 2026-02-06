from typing import Optional
from .models import Assignment
from .errors import ConflictError


def ensure_no_active_assignment_for_user(active: Optional[Assignment]):
    if active is not None:
        raise ConflictError("User already has an active assignment")


def ensure_no_active_assignment_for_bicycle(active: Optional[Assignment]):
    if active is not None:
        raise ConflictError("Bicycle already assigned")
