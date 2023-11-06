def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    low_to_print = None
    high_to_print = None
    for num in nums:
        if num < lowest or num > highest:
            continue
        elif not low_to_print and not high_to_print:
            low_to_print = num
            high_to_print = num
        else:
            if num <= low_to_print:
                low_to_print = num
            elif num >= high_to_print:
                high_to_print = num
            else:
                continue
        
    print(f"{low_to_print} fits\n{high_to_print} fits")

in_range([10, 20, 30, 40, 50], 15, 30)            
