class Operations:
    def __init__(self):
        pass

    def rshift(self, value, count: int):
        return (value >> count)

    def lshift(self, value, count: int):
        return (value << count)

    def rshift(self, matrix):
        new = matrix
        first = matrix[0]

        for i in range(0, len(matrix) - 2):
            new[i] = matrix[i + 1]
        new[len(matrix) - 1] = first

class EEA:
    def __init__(self, block_size):
        self.key = None
        self.block_size = None

        self.Operations = Operations()
        
        self.__check__(block_size)

    def __check__(self, block_size):
        authorized = [
            "16",
            "32",
            "64",
            "128",
            "256"
        ]

        if (f"{block_size}" in authorized):
            self.block_size = block_size
        else:
            raise Exception("block size must be: {}".format(
                ', '.join(authorized)
            ))

    def new(self, key: str):
        size = len(key)

        if (size >= self.block_size):
            if (size % self.block_size == 0):
                self.key = key
            else:
                raise Exception("key must be align to {} characters".format(self.block_size))
        else:
            raise Exception("key size must be at least {} characters long".format(self.block_size))

    def encode(self, data: str):
        padded = self.__pad__(data)

        return (padded)

    def decode(self, data: str, pad):
        self.__unpad__(data, pad)

    def __pad__(self, data: str):
        size = len(data)
        new_data = data
        next_align = size + (self.block_size - size % self.block_size)
        pad = next_align - size

        for i in range(0, pad):
            new_data += '0'

        return ({
            "raw": new_data,
            "pad": pad
        })

    def __unpad__(self, data: str, pad):
        print(data[:-pad])

class Core:
    def __init__(self):
        self.EEA = EEA(16)
        self.EEA.new("0000000000000000")

        self.main()

    def main(self):
        encoded = self.EEA.encode("abcdefghijkl")
        self.EEA.decode(encoded["raw"], encoded["pad"])

if (__name__ == "__main__"):
    Core()