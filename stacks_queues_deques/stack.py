import numpy as np
import numpy.typing as npt

class Stack:
    def __init__(self, size: int):
        self.__size: int = size
        self.__pointer: int = -1
        self.__elements: npt.NDArray[np.int_] = np.empty(self.__size, dtype=int)

    def __is_full(self) -> bool:
        return True if self.__pointer == self.__size + 1 else False

    def __is_empty(self) -> bool:
        return True if self.__pointer == -1 else False

    def put(self, element: int) -> None:
        if self.__is_full():
            print("Stack is already full")
        else:
            self.__pointer += 1
            self.__elements[self.__pointer] = element

    def pop(self) -> None:
        if self.__is_empty():
            print("Stack is empty, there are no elements to remove")
        else:
            self.__pointer -= 1

    def peek(self) -> int:
        if self.__is_empty():
            return -1
        else:
            return self.__elements[self.__pointer]



