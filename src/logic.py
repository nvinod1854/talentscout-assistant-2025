import re

EXIT_KEYWORDS = {"quit","exit","stop","bye"}

def is_exit(text: str) -> bool:
    return any(k in text.lower() for k in EXIT_KEYWORDS)

def validate_phone(phone: str) -> bool:
    digits = re.sub(r"\D", "", phone)
    return 7 <= len(digits) <= 15

def next_missing_field(candidate_dict: dict):
    order = ["full_name","email","phone","years_experience","desired_positions","location","tech_stack"]
    for k in order:
        if k not in candidate_dict or not candidate_dict[k]:
            return k
    return None