from datetime import datetime
class CandidateAnswer:
    def __init__(self,question_id:int ,answer_text:str):
        self.question_id = question_id
        self.answer_text = answer_text
        self.timestamp = datetime.now()
        
        
    def get_answer(self):
        # code to get the answer for the given question using the Speech to Text Api
        return {
            'question_id': self.question_id,
            'answer_text': self.answer_text,
            'timestamp': self.timestamp.isoformat()
        }
