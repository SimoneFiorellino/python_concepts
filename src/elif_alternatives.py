"""
Demonstration of:
1) if / elif / else
2) Dictionary dispatch
3) match / case (Python 3.10+)
"""


def handle_if_elif(cmd):
    """Classic if / elif chain."""
    if cmd == "start":
        return "Starting..."
    elif cmd == "stop":
        return "Stopping..."
    elif cmd == "pause":
        return "Pausing..."
    else:
        return "Unknown command"


# ---------------------------
# 2) DICTIONARY DISPATCH
# ---------------------------


def start():
    return "Starting..."


def stop():
    return "Stopping..."


def pause():
    return "Pausing..."


def unknown():
    return "Unknown command"


DISPATCH = {
    "start": start,
    "stop": stop,
    "pause": pause,
}


def handle_dict(cmd):
    """Use a dictionary to dispatch functions."""
    func = DISPATCH.get(cmd, unknown)
    return func()


# ---------------------------
# 3) MATCH / CASE (Python 3.10+)
# ---------------------------


def handle_match(cmd):
    """Structural pattern matching."""
    match cmd:
        case "start":
            return "Starting..."
        case "stop":
            return "Stopping..."
        case "pause":
            return "Pausing..."
        case _:
            return "Unknown command"


# ---------------------------
# MAIN DEMO
# ---------------------------

if __name__ == "__main__":
    for command in ["start", "stop", "pause", "other"]:
        print(f"\nCOMMAND: {command}")

        print(" if/elif:     ", handle_if_elif(command))
        print(" dict:        ", handle_dict(command))
        print(" match/case:  ", handle_match(command))
