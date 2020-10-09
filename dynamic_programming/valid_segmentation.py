import unittest


def valid_segmentation(words, string):
    current_string = ""
    res = []
    for c in string:
        current_string += c
        if current_string in words:
            res.append(current_string)
            current_string = ""
    return "" if current_string else " ".join(res)


def valid_segmentation_2(words, string):
    def valid_segmentation_recursive(start):
        if start == len(string):
            return [], True
        for end in range(start, len(string) + 1):
            word = string[start:end]
            if word in words:
                remaining_words, result = valid_segmentation_recursive(end)
                if result:
                    return [word] + remaining_words, True
        return [""], False

    segmentation, is_valid = valid_segmentation_recursive(0)
    return " ".join(segmentation)


def valid_segmentation_3(words, string):
    cache = [None] * len(string)

    def valid_segmentation_recursive(start):
        if start == len(string):
            return ([], True)

        if start not in cache:
            segmentation, segmentation_exists = "", False
            for end in range(start, len(string) + 1):
                word = string[start:end]
                if word in words:
                    remaining_words, result = valid_segmentation_recursive(end)
                    if result:
                        segmentation_exists = True
                        segmentation = [word] + remaining_words
                        break
            cache[start] = segmentation, segmentation_exists
        return cache[start]

    segmentation, is_valid = valid_segmentation_recursive(0)
    return " ".join(segmentation)


def valid_segmentation_4(words, string):
    cache = [([], False)] * (len(string) + 1)
    cache[0] = ([], True)
    for i in range(len(string)):
        for j in range(i, len(string)):
            word = string[i : j + 1]
            if cache[i][1] and word in words:
                cache[j + 1] = (cache[i][0] + [word], True)
    segmentation, is_valid = cache[-1]
    return " ".join(segmentation) if is_valid else ""


class Test(unittest.TestCase):
    def test_segmentation(self):
        string_1 = "helloworld"
        string_2 = "helloworlds"
        string_3 = "catsand"
        string_4 = "hellocatanddog"
        words = {"hello", "worlds", "and", "cats", "world", "cat"}

        self.assertEqual("hello world", valid_segmentation(words, string_1))
        self.assertEqual("hello world", valid_segmentation_2(words, string_1))
        self.assertEqual("hello world", valid_segmentation_3(words, string_1))
        self.assertEqual("hello world", valid_segmentation_4(words, string_1))

        self.assertEqual("", valid_segmentation(words, string_3))
        self.assertEqual("cats and", valid_segmentation_2(words, string_3))
        self.assertEqual("cats and", valid_segmentation_3(words, string_3))
        self.assertEqual("cats and", valid_segmentation_4(words, string_3))

        self.assertEqual("", valid_segmentation(words, string_4))
        self.assertEqual("", valid_segmentation(words, string_4))
        self.assertEqual("", valid_segmentation(words, string_4))
        self.assertEqual("", valid_segmentation(words, string_4))
