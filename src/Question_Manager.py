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