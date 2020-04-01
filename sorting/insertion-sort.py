import unittest

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])

class test(unittest.TestCase):
    def test_1(self):
        arr = ["dog", "deer", "deal"]
        self.assertListEqual(['deer', 'deal'], autoComplete1("de", arr))


if __name__ == "__main__":
    unittest.main()

