from pathlib import Path

PROMPTS_DIR = Path("prompts")


def load_prompt(filename: str) -> str:
    return (PROMPTS_DIR / filename).read_text()


def router_node(state):

    system_prompt = load_prompt("system.txt")

    jurisdiction = state["jurisdiction"]
    mode = state["mode"]

    # Jurisdiction prompt
    if jurisdiction == "global":
        jurisdiction_prompt = load_prompt(
            "global.txt"
        )

    elif jurisdiction == "specific country":

        jurisdiction_prompt = load_prompt(
            "country.txt"
        )

        country = state["countries"][0]

        jurisdiction_prompt += (
            f"\n\nCountry: {country}"
        )

    elif jurisdiction == "comparison":

        jurisdiction_prompt = load_prompt(
            "comparison.txt"
        )

        countries = ", ".join(
            state["countries"]
        )

        jurisdiction_prompt += (
            f"\n\nCountries: {countries}"
        )

    else:
        raise ValueError(
            f"Invalid jurisdiction: {jurisdiction}"
        )

    # Mode prompt
    if mode == "advanced":
        mode_prompt = load_prompt(
            "advanced.txt"
        )
    else:
        mode_prompt = load_prompt(
            "basic.txt"
        )

    state["prompt"] = (
        system_prompt
        + "\n\n"
        + jurisdiction_prompt
        + "\n\n"
        + mode_prompt
    )

    print("\n=== ROUTER ===")
    print(state["prompt"])
    print("==============\n")

    return state