def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    temp = []
    for let in phrase:
        if let.lower() == to_swap.lower():
            temp.append(let.upper() if let.islower() else let.lower())
        else:
            temp.append(let)
    
    return "".join(temp)