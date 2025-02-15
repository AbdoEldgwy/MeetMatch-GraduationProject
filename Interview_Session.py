from .Candidate_answer import CandidateAnswer
from datetime import datetime
class InterviewSession:
    def __init__(self, sessino_id:int, timestamp: datetime):
        self.sessino_id = sessino_id