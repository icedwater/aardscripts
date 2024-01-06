#! /usr/bin/env python3

"""
Convert map item line to JSON
"""

def map_convert(map_line: str)-> dict:
    """
    @param map_line: text line containing attributes
    @return map_dict: attributes converted to dict
    """
    # We expect a line containing n attributes: string or list values in braces, integers by themselves
    # Convert each attribute to a key-value pair.
    # ObjectType: attribute1={string value}, attribute2={list value one, list value two}, attribute3=12
    # { "objecttype": { "attribute1": "...", "attribute2": [ "...", "..." ], "attribute3": ... } }

    map_dict = dict()

    try:
        map_fields = map_line.split(':')
        object_name = map_fields[0]
        object_details = ':'.join(map_fields[1:]).strip()

        details_dict = dict()
        object_details = object_details.replace(", ", '@').replace("}@", "}#")
        object_attributes = [ attribute for attribute in object_details.split('#') ]

        for attribute in object_attributes:
            attr_name, attr_value = attribute.split('=')
            if attr_value[0] == '{' and attr_value[-1] == '}':
                if '@' in attr_value:  # multiple key-value pairs
                    attr_values = attr_value[1:-1].split('@')
                else:
                    attr_values = attr_value[1:-1]
            else:
                attr_values = int(attr_value)
            details_dict[attr_name] = attr_values

        map_dict[object_name] = details_dict
    except Exception as err:
        print(err)

    return map_dict

def main():
    import sys
    
    try:
        test = sys.argv[1]
    except IndexError:
        test = "ObjectType: b={hi, ho}, f={hello}, c=2"

    print(f"We got {test} as input. The output is:\n{map_convert(test)}.")

if __name__ == "__main__":
    main()
