from altair import value


def validate_positive_float(value:str)-> float:
    """validates that input is a positive float."""
    float_value=float(value.strip())
    if float_value <= 0:
       raise ValueError("Value must be a positive number.")
    return float_value   

def validate_non_empty_string(value:str)-> str    :
        """validates that input is a non-empty string."""
        val=value.strip()
        if not val:
            raise ValueError("Input cannot be empty. Please enter a valid string.")
        return val