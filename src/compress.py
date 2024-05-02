from typing import List


class Solution:
    def compress(self, c: List[str]) -> int:
        write, index, current = 0, 0, 0

        # append a dummy character to the end of the list to avoid out of index error also simplify the logic
        c.append("\0")

        while True:
            current += 1

            # If the current character is the last character, return the last write position + 1
            if current == len(c):
                return write

            # If the current character is the same as the previous character, continue
            if c[index] == c[current]:
                continue

            write = self.do_write(write, index, current, c)

            index = current

    # this solution has to skip non-alphabet characters
    def compress_2(self, c: List[str]) -> int:
        write, index, current, offset = 0, 0, 0, 0

        c.append("\0")

        while not self.is_alphabet(c[current]):
            index += 1
            current += 1

        while True:
            current += 1

            # If the current character is the last character, return the last write position + 1
            if current == len(c):
                return write

            if not self.is_alphabet(c[current]) and current is not len(c) - 1:
                offset += 1
                continue

            # If the current character is the same as the previous character, continue
            if c[index] == c[current]:
                continue

            write = self.do_write_2(write, index, current, offset, c)

            index = current
            offset = 0

    def is_alphabet(self, s):
        dec = ord(s)
        return 122 >= dec >= 97 or 90 >= dec >= 65

    def do_write(
            self, write: int, index: int, current: int, char: List[str]
    ) -> int:
        """
        Modify original list in place and return next write position.

        Returns:
            int: Return next write position.
        """
        length = current - index

        char[write] = char[index]
        if length > 1:
            for v in str(length):
                char[write + 1] = v
                write += 1

        return write + 1

    def do_write_2(
            self, write: int, index: int, current: int, offset: int, char: List[str]
    ) -> int:
        """
        Modify original list in place and return next write position.

        Returns:
            int: Return next write position.
        """
        length = current - index - offset

        char[write] = char[index]
        if length > 1:
            for v in str(length):
                char[write + 1] = v
                write += 1

        return write + 1
