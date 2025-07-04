from datetime import datetime, timedelta
from typing import List, Dict, Tuple
from task import Task

class Scheduler:
    

    def __init__(self, hours_per_day: float = 8.0):
        
        if hours_per_day <= 0:
            raise ValueError("Hours per day must be positive.")
        self.hours_per_day = hours_per_day
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        
        self.tasks.append(task)

    def _calculate_urgency(self, task: Task) -> float:
        
        
        now = datetime.now()
        hours_until_deadline = (task.deadline - now).total_seconds() / 3600
        
        if hours_until_deadline < 0:
            urgency_deadline = 1000 + abs(hours_until_deadline) 

        elif hours_until_deadline < 1:
            urgency_deadline = 100
        else:
            urgency_deadline = 100 / (hours_until_deadline + 1)

        priority_weight = task.priority.value

      
        final_urgency = priority_weight * urgency_deadline
        
        return final_urgency

    def create_schedule(self, days_to_schedule: int = 7) -> Dict[str, List]:
       
        scored_tasks = [
            (self._calculate_urgency(task), task) for task in self.tasks
        ]

       
        sorted_tasks = sorted(scored_tasks, key=lambda x: x[0], reverse=True)
        
        
        schedule: Dict[int, Dict[str, any]] = {
            day: {"tasks": [], "remaining_hours": self.hours_per_day}
            for day in range(days_to_schedule)
        }
        
        oversized_tasks: List[Task] = []
        unscheduled_tasks: List[Task] = [task for _, task in sorted_tasks]

        for _, task in sorted_tasks:
            if task.effort_hours > self.hours_per_day:
                oversized_tasks.append(task)
                unscheduled_tasks.remove(task)
                continue # Skip to next task

            allocated = False
            for day_index in range(days_to_schedule):
                if schedule[day_index]["remaining_hours"] >= task.effort_hours:
                    schedule[day_index]["tasks"].append(task)
                    schedule[day_index]["remaining_hours"] -= task.effort_hours
                    unscheduled_tasks.remove(task)
                    allocated = True
                    break
            
           

        return {
            "schedule": schedule,
            "oversized_tasks": oversized_tasks,
            "unscheduled_tasks": unscheduled_tasks
        }

    @staticmethod
    def format_schedule(result: Dict[str, List]) -> None:
        
        print("="*60)
        print("           Intelligent Task Schedule           ")
        print("="*60)

        schedule = result["schedule"]
        for day_index, day_data in schedule.items():
            day_date = datetime.now().date() + timedelta(days=day_index)
            print(f"\n--- Day {day_index + 1} ({day_date.strftime('%A, %Y-%m-%d')}) ---")
            print(f"    Available Hours: {day_data['remaining_hours']:.1f} / {sum(t.effort_hours for t in day_data['tasks']) + day_data['remaining_hours']:.1f}")
            if not day_data["tasks"]:
                print("    No tasks scheduled.")
            else:
                for task in day_data["tasks"]:
                    print(f"    - [{task.priority.name}] {task.description} ({task.effort_hours}h) - Due: {task.deadline.strftime('%m-%d %H:%M')}")
        
        if result["oversized_tasks"]:
            print("\n" + "="*20 + " OVERSIZED TASKS " + "="*20)
            print("These tasks are too large to fit in a single day and need to be broken down:")
            for task in result["oversized_tasks"]:
                print(f"    - {task}")

        if result["unscheduled_tasks"]:
            print("\n" + "="*20 + " UNSCHEDULED TASKS " + "="*19)
            print("These tasks could not be scheduled in the given timeframe:")
            for task in result["unscheduled_tasks"]:
                print(f"    - {task}")
        
        print("\n" + "="*60)