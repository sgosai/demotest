import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
# import demistomock as demisto
# from CommonServerPython import *
# from CommonServerUserPython import *

def multiply_logic(args: dict): #-> CommandResults:
    num1 = int(args.get('num1', 0))
    num2 = int(args.get('num2', 0))

    result = num1 * num2
    return result
    # return CommandResults(
    #     outputs_prefix='Math.Result',
    #     outputs={'Value': result},
    #     readable_output=f'The result is {result}'
    # )

def main():
    try:
        return_results(multiply_logic(demisto.args()))
    except Exception as e:
        return_error(f'Failed to execute: {str(e)}')

# This block ensures the script only runs inside XSOAR, not during pytest imports.
if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
