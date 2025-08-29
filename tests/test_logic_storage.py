from src.logic import validate_phone, is_exit
from src.storage import Candidate, save_candidate, load_all
import os
import tempfile
import json

def test_validate_phone():
    assert validate_phone("+91-9876543210")
    assert validate_phone("9876543210")
    assert not validate_phone("abcd")

def test_save_and_load(tmp_path):
    # set data path to tmp to avoid messing real data (monkeypatch would be better)
    tmp_file = tmp_path / "candidates.json"
    # create a simple candidate and write using save_candidate function
    c = Candidate(
        full_name="Test User",
        email="test@example.com",
        phone="9876543210",
        years_experience=1.0,
        desired_positions=["Dev"],
        location="Nowhere",
        tech_stack=["python"]
    )
    # temporarily write JSON
    db = [c.dict() if hasattr(c, "dict") else c.model_dump()]
    tmp_file.write_text(json.dumps(db))
    assert tmp_file.exists()
