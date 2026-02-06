from typing import Optional
from .models import Assignment


def ensure_no_active_assignment_for_user(active: Optional[Assignment]):
    if active is not None:
        raise ValueError("User already has an active assignment")


def ensure_no_active_assignment_for_bicycle(active: Optional[Assignment]):
    if active is not None:
        raise ValueError("Bicycle already assigned")
