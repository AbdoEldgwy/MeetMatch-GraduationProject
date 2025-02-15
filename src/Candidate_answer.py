from datetime import datetime
class CandidateAnswer:
    def __init__(self,question_id:int ,answer_text:str, timestamp: datetime):
        self.question_id = question_id
        self.answer_text = answer_text
        self.timestamp = timestamp
        
        
    def get_answer(self):
        # code to get the answer for the given question using the Speech to Text Api
        pass