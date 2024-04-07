def check_fields(req, required_fields=[]):
    missing_fields = [field for field in required_fields if field not in req]
    if missing_fields:
        return f"{', '.join(missing_fields)} {'are' if len(missing_fields) > 1 else 'is'} required"
    return None