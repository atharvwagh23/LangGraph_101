def stock_router(state):
    if state["stock_available"]:
        return "confirm"

    return "reject"