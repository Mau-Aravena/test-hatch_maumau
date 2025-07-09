import cowsay


def saycow(text: str):
    """
    Displays a cow-themed ASCII art message using the 'cowsay' library.

    Parameters
    ----------
    text (str): The message to be shown in the speech bubble above the cow.

    Returns
    -------
    A string of cowsay with the text

    Example
    -------
        >>> print(saycow("Hi, :D"))
        ________
        < Hi :D >
        --------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/
                        ||----w |
                        ||     ||
    """
    return cowsay.get_output_string(char="cow", text=text)


if __name__ == "__main__":
    print(saycow("perro"))
