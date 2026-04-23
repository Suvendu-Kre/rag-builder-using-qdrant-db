def validate_input(input: str) -> str:
    """
    Validates the input to ensure it meets certain criteria.
    """
    if not input or not input.strip():
        return "Error: Input cannot be empty."
    return input.strip()

def validate_output(output: str) -> str:
    """
    Validates the output to ensure it meets certain criteria.
    """
    return output.strip() if output and output.strip() else "Error: Empty response."