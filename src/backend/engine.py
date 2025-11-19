from rules_engine import RulesEngine
from task_service import TaskService
from reward_service import RewardService

class TaskEngine:
    def __init__(self):
        self.task_service = TaskService()
        self.reward_service = RewardService()
        self.rules_engine = RulesEngine()

    def execute_task(self, user_id, task_id):
        steps = self.task_service.get_task_steps(task_id)
        for step in steps:
            print(f"User {user_id} completing step {step}")
            print(f"Displaying guidance for step {step}")
            if self.rules_engine.is_reward_applicable(user_id, task_id, step):
                self.reward_service.award_points(user_id, task_id, step)

if __name__ == "__main__":
    engine = TaskEngine()
    engine.execute_task("user_123", "task_001")
