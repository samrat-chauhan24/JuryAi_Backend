from fastapi import HTTPException


def validator_node(state):

    jurisdiction = state["jurisdiction"]
    countries = state["countries"]
    mode = state["mode"]

    if jurisdiction == "global":
        if len(countries) != 0:
            raise HTTPException(
                status_code=400,
                detail="Global requires no countries"
            )

    elif jurisdiction == "specific country":
        if len(countries) != 1:
            raise HTTPException(
                status_code=400,
                detail="Specific country requires one country"
            )

    elif jurisdiction == "comparison":
        if len(countries) != 2:
            raise HTTPException(
                status_code=400,
                detail="Comparison requires two countries"
            )

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid jurisdiction"
        )

    if mode not in ["basic", "advanced"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid mode"
        )

    return state