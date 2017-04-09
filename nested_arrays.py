# -*- coding: utf-8 -*-
"""Example for a flatten arrays.

Example:
        $ python nested_arrays.py
"""


def processor_nested_arrays(narrays):
    """Example function for flatten an array of arbitrarily nested arrays
       of integers into a flat array of integers.

    Args:
        narrays: nested arrays.

    Returns:
        The return the flat array of integers.

    """
    result_array = []

    for value in narrays:
        if isinstance(value, list):

            for item in value:
                if isinstance(item, list):

                    for map_item in item:
                        result_array.append(map_item)

                else:
                    result_array.append(item)
        else:
            result_array.append(value)

    return result_array



if __name__ == '__main__':
    MY_ARRAY = [[1, 2, [3]], 4]

    print processor_nested_arrays(narrays=MY_ARRAY)
