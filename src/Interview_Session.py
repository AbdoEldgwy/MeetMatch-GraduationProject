from .Candidate_answer import CandidateAnswer
from datetime import datetime
class InterviewSession:
    def __init__(self, sessino_id:int, start_time: datetime , end_time: datetime):
        self.sessino_id = sessino_id
        self.start_time = start_time
        self.end_time = end_time
        
    def start_session(self):
        print("Session started at", self.start_time)
        return self.start_time
    
    def end_session(self):
        print("Session ended at", self.end_time)
        return self.end_time
    
    def record_answer(self, question_id:int, answer_text:str):
        self.start_session()
        answer = CandidateAnswer(question_id, answer_text, datetime.now())
        print("Answer recorded for question", question_id, "with answer", answer_text)
        return {"session_id": self.sessino_id, "timestamp": answer.timestamp}