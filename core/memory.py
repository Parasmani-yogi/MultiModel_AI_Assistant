def get_recent_history(messages, limit=5):
    return messages[-limit:]


def add_message(messages, role, content, image=None):
    msg = {
        "role": role,
        "content": content
    }

    if image:
        msg["image"] = image

    messages.append(msg)
    return messages