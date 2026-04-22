def validate_input(input_text: str) -> str:
    """
    Validates the input to ensure it is safe and appropriate.
    """
    # Basic profanity check (replace with a more sophisticated solution)
    profane_words = ["badword1", "badword2"]
    for word in profane_words:
        if word in input_text.lower():
            return "Error: Input contains inappropriate language."
    return input_text

def validate_output(output: str) -> str:
    """
    Validates the output to ensure it is safe and appropriate.
    """
    return output.strip() if output and output.strip() else "Error: Empty response."