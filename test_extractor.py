import unittest

from conversation_to_tasks.conversation_to_tasks import extract_tasks


class TestConversationToTasks(unittest.TestCase):
    def test_bullet_points(self):
        lines = [
            "- Finish the ORA workbench prototype.",
            "* Check GPU VRAM requirements.",
            "• Review notes from yesterday's meeting.",
        ]
        expected = [
            "Finish the ORA workbench prototype.",
            "Check GPU VRAM requirements.",
            "Review notes from yesterday's meeting.",
        ]
        self.assertEqual(extract_tasks(lines), expected)

    def test_numbered_list(self):
        lines = [
            "1. Schedule a meeting with the design team.",
            "2) Prepare the README and documentation.",
            "10. Publish the repository.",
        ]
        expected = [
            "Schedule a meeting with the design team.",
            "Prepare the README and documentation.",
            "Publish the repository.",
        ]
        self.assertEqual(extract_tasks(lines), expected)

    def test_todo_keywords(self):
        lines = [
            "We need to work on this soon.",
            "TODO: Refactor the extraction logic.",
            "task: Write integration tests.",
        ]
        expected = [
            "Refactor the extraction logic.",
            "Write integration tests.",
        ]
        self.assertEqual(extract_tasks(lines), expected)

    def test_empty_input(self):
        self.assertEqual(extract_tasks([]), [])


if __name__ == "__main__":
    unittest.main()