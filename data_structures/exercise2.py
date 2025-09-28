def normalize_and_sum_amounts(lines: list[str]) -> None:
    """
    Each string may contain a money amount in mixed formats, e.g.:
      "Paid: 1,250.50 USD", "amount=€2.300,75", "RON 3 000", "750"
    Rules:
      - Accept digits with optional thousand separators (comma, dot, or space).
      - Decimal separator may be '.' or ',' but not both.
      - Ignore currency symbols/letters.
      - Sum valid amounts; skip invalid tokens (e.g., '12,34,56').
      - Return the sum as float rounded to 2 decimals.
    """

    # Holding values in a list to work with them later
    values = []
    temp = ""
    for line in lines:
        for i in range(len(line)):
            if line[i].isdigit():
                temp += line[i]
            elif line[i] in ".,":
                temp += line[i]

        values.append(temp)
        temp = ""

    # Removing unnecesary dots
    for value in values:
        for i in range(len(value)):
            if value[i] in ".,":
                value.remove(value[i])
                break
    for value in values:
        print(values)


lines = ["Paid 2.453.02 USD", "amount=€2.300,75", "RON 3 000", "750"]
x = normalize_and_sum_amounts(lines)
