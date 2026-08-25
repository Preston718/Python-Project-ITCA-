def calculate(expression: str) -> str:
    """Evaluate a calculator expression with arbitrary precision for large numbers."""
    try:
        # Only allow simple arithmetic operators.
        allowed_chars = set('0123456789+-*/.() ')
        if not set(expression) <= allowed_chars:
            return 'Error: only digits and + - * / . ( ) are allowed.'

        result = eval(expression, {'__builtins__': None}, {})
        
        # Format the result with proper handling of large numbers
        if isinstance(result, float):
            # For decimal results, round to 2 places and format
            rounded = round(result, 2)
            # Check if it's effectively a whole number
            if rounded == int(rounded):
                return f'{int(rounded):,}'
            else:
                return f'{rounded:,.2f}'
        else:
            # For integer results, use comma separator
            return f'{int(result):,}'
    except ZeroDivisionError:
        return 'Error: division by zero.'
    except Exception:
        return 'Error: invalid expression.'


def main():
    print('Simple Calculator')

    while True:
        expression = input('> ').strip()
        if expression.lower() in {'quit', 'exit'}:
            print('Goodbye!')
            break
        if not expression:
            continue

        output = calculate(expression)
        print(output)
        print('do you wish to continue? (yes/no)')
        cont = input('> ').strip().lower()
        if cont not in {'yes', 'y'}:
            print('Goodbye!')
            break

if __name__ == '__main__':
    main()
