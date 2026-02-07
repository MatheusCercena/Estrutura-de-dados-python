import numpy as np
from dataclasses import dataclass, field
import numpy.typing as npt

class RoundQueue:
    def __init__(self, size: int):
        self.size: int = size
        self.__start: int = 0
        self.__end: int = -1
        self.__queued_elements: int = 0
        self.__queue: npt.NDArray[np.int_] = np.empty(self.size, dtype=int)

    def is_empty(self) -> bool:
        return True if self.__start > self.__end else False
            
    def is_full(self) -> bool:
        return True if self.__end > self.__start else False

    def enqueue(self, value: int) -> None:
        if self.is_full():
            return
        self.move_end_pointer()
        self.__queue[self.__end] = value
        self.__queued_elements += 1

    def __pointer_movement(self, pointer_position: int) -> int:
        return 1 if pointer_position == self.size - 1 else -1

    def move_end_pointer(self) -> None:
        self.__end += self.__pointer_movement(self.__end)

    def move_start_pointer(self) -> None:
        self.__start += self.__pointer_movement(self.__start)

    def unqueue(self) -> None:
        if self.is_empty():
            return
        self.move_start_pointer()
        self.__queued_elements -= 1

