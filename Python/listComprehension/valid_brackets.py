user_input = "[({})]"

symbol_table = {
                    "<" : ">",

                    "{" : "}",

                    "[" : "]",

                    "(" : ")"
}


top = -1

is_valid = True

symbol_stack = []

for symbol in user_input :

    if symbol in symbol_table :

        top += 1

        symbol_stack.append(symbol)

    else :

        if top == -1 :

            is_valid = False

            break

        current_symbol = symbol_stack[top]

        current_symbol_closing = symbol_table[current_symbol]

        if symbol == current_symbol_closing :

            symbol_stack.pop()

            top -= 1

        else :

            is_valid = False

            break

if top != -1 :

    is_valid = False

print(is_valid) 



