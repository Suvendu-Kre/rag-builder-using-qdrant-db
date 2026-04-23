def validate_input(input: str) -> str:
    """
    Validates the input to ensure it is not malicious or harmful.
    """
    # Basic input sanitization (can be expanded)
    input = input.strip()
    if not input:
        return "Error: Input cannot be empty."
    return input

def validate_output(output: str) -> str:
    """
    Validates the output to ensure it is safe and appropriate.
    """
    return output.strip() if output and output.strip() else "Error: Empty response."