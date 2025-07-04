import uuid
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 3
    HIGH = 6
    CRITICAL = 12 


class Task:

    def __init__(self, description: str, deadline: datetime, effort_hours: float, priority: Priority):
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string.")
        if not isinstance(deadline, datetime):
            raise ValueError("Deadline must be a datetime object.")
        if not isinstance(effort_hours, (int, float)) or effort_hours <= 0:
            raise ValueError("Effort must be a positive number.")
        if not isinstance(priority, Priority):
            raise ValueError("Priority must be a valid Priority enum member.")

        self.id = uuid.uuid4()
        self.description = description
        self.deadline = deadline
        self.effort_hours = effort_hours
        self.priority = priority
        self.creation_date = datetime.now()

    def __repr__(self):
        
        return (
            f"Task(id={self.id}, desc='{self.description}', "
            f"deadline='{self.deadline.strftime('%Y-%m-%d %H:%M')}', "
            f"effort={self.effort_hours}h, priority={self.priority.name})"
        )