from dataclasses import dataclass, field

@dataclass
class ExpressionValidator:
    __expression: str
    __expr_array: list[str] = field(default_factory=list, init=False)

    def __is_empty(self) -> bool:
        return True if len(self.__expr_array) == 0 else False

    def __validate(self, char: str) -> bool:
        last_item: str = self.__expr_array[-1] if not self.__is_empty() else ''
        if char == '{' and (last_item in '{' or self.__is_empty() == True):
            return True
        elif char == '[' and (last_item in '{' or last_item == ''):
            return True
        elif char == '(' and last_item in '[(':
            return True
        elif char == ')' and last_item in '()':
            return True
        elif char == ']' and last_item == '[':
            return True
        elif char == '}' and last_item == '{':
            return True
        else:
            return False

    def __manipulate_array(self, char: str) -> None:
        expr_array: list[str] = self.__expr_array
        if char in '{[(':
            expr_array.append(char)
        else:
            expr_array.pop()

    def validate_expr(self) -> bool:
        for char in self.__expression:
            if char in '{[()]}':
                if self.__validate(char):
                    self.__manipulate_array(char)
                else:
                    return False
        return True


expr = ExpressionValidator('{5*[5*()8]}')
print(expr.validate_expr())
