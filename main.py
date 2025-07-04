from datetime import datetime, timedelta
from task import Task, Priority
from scheduler import Scheduler

def main():
    
    now = datetime.now()
    tasks = [
        Task(
            description="Finalize Q3 report",
            deadline=now + timedelta(days=2, hours=4),
            effort_hours=6,
            priority=Priority.HIGH
        ),
        Task(
            description="Fix critical login bug",
            deadline=now + timedelta(hours=8), # Due today!
            effort_hours=3,
            priority=Priority.CRITICAL
        ),
        Task(
            description="Plan team offsite event",
            deadline=now + timedelta(days=14),
            effort_hours=5,
            priority=Priority.LOW
        ),
        Task(
            description="Submit expense report",
            deadline=now + timedelta(days=1), # Due tomorrow
            effort_hours=0.5,
            priority=Priority.MEDIUM
        ),
        Task(
            description="Create marketing presentation",
            deadline=now + timedelta(days=4),
            effort_hours=8,
            priority=Priority.HIGH
        ),
        Task(
            description="Review intern code submissions",
            deadline=now + timedelta(days=3),
            effort_hours=4,
            priority=Priority.MEDIUM
        ),
        Task(
            description="Update server SSL certificate",
            deadline=now - timedelta(hours=2), # PAST DUE!
            effort_hours=2,
            priority=Priority.CRITICAL
        ),
        Task(
            description="Long-term strategy document",
            deadline=now + timedelta(days=20),
            effort_hours=12, # Oversized task
            priority=Priority.LOW
        ),
        Task(
            description="Quick project status check-in",
            deadline=now + timedelta(days=1, hours=2),
            effort_hours=0.5,
            priority=Priority.HIGH
        )
    ]


    task_scheduler = Scheduler(hours_per_day=8.0)
    for t in tasks:
        task_scheduler.add_task(t)

    schedule_result = task_scheduler.create_schedule(days_to_schedule=5)


    Scheduler.format_schedule(schedule_result)


if __name__ == "__main__":
    main()