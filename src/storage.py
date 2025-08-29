from pydantic import BaseModel, EmailStr
from pathlib import Path
import json
from typing import List, Dict, Any
from datetime import datetime

# Path to store candidate data
DATA_PATH = Path(__file__).parent / "candidates.json"

# ----------------------------
# Candidate Model
# ----------------------------
class Candidate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    years_experience: int
    desired_positions: List[str]
    location: str
    tech_stack: List[str]
    answers: Dict[str, str] = {}
    created_at: datetime = datetime.now()

# ----------------------------
# Save Candidate Function
# ----------------------------
def save_candidate(candidate: Candidate):
    try:
        db = []
        if DATA_PATH.exists():
            db = json.loads(DATA_PATH.read_text())

        # use model_dump_json to ensure datetime is serializable
        db.append(json.loads(candidate.model_dump_json()))

        DATA_PATH.write_text(json.dumps(db, indent=2, default=str))
    except Exception as e:
        print(f"❌ Error saving candidate: {e}")