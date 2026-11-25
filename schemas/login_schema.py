LOGIN_SCHEMA = {
    "type": "object",
    "required": ["token", "email", "role"],
    "properties": {
        "token": {"type": "string"},
        "email": {"type": "string"},
        "role": {"type": "string"},
        "fullName": {"type": "string"},
        "permissions": {"type": "array"},
    },
}
