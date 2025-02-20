from typing import List, Optional
class JSONFileHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_questions(self) -> dict:
        """Load JSON data from the file."""
        import json
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def parse_questions(self) -> list:
        """Convert raw JSON data into a list of Question objects."""
        raw_data = self.load_questions()
        questions = []
        for item in raw_data:
            question = Question(
                id=item["id"],
                text=item["text"],
                related_kpis=item["related_kpis"]
            )
            questions.append(question)
        return questions


class Question:
    def __init__(self, id: str, text: str, related_kpis: list[str]):
        self.id = id
        self.text = text
        self.related_kpis = related_kpis
    
    def get_question_text(self) -> str:
        return f"Question {self.id}: {self.text}"

    def get_related_kpis(self) -> list[str]:
        return self.related_kpis


class QuestionManager:

    def __init__(self):
        self.questions: List[Question] = []
        self._current_index = 0
        
    def load_questions_from_file(self, file_handler: JSONFileHandler):
        """Load and parse questions using a FileHandler"""
        raw_data = file_handler.load_questions()
        self.questions = file_handler.parse_questions(raw_data)
        self._current_index = 0  # Reset pointer on new load
        
    def get_next_question(self) -> Optional[Question]:
        """Get next question in sequence"""
        if self._current_index < len(self.questions):
            question = self.questions[self._current_index]
            self._current_index += 1
            return question
        return None
    
    def get_question_by_id(self, q_id: str) -> Optional[Question]:
        for i in range(len(self.questions)):
            if self.questions[i].id == q_id:
                return self.questions[i]
        return None