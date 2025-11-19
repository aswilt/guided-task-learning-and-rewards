"""
Learning API Stub
----------------
Simulates integration with an external learning platform for portfolio purposes.
"""

class LearningAPIStub:
    def get_lesson(self, task_id, step_number):
        return f"Sample lesson content for task {task_id}, step {step_number}"

    def mark_completed(self, user_id, lesson_id):
        print(f"Lesson {lesson_id} marked complete for user {user_id}")
