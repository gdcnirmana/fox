import unittest


from src.services.dedup import chunked, dedup_keep_order


class TestDedup(unittest.TestCase):
    def test_dedup_keep_order(self):
        result = dedup_keep_order(["a", "b", "a", "c", "b", "d"])
        self.assertEqual(result.unique, ("a", "b", "c", "d"))
        self.assertEqual(result.duplicates, ("a", "b"))

    def test_chunked(self):
        self.assertEqual(chunked([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_chunked_invalid_size(self):
        with self.assertRaises(ValueError):
            chunked([1, 2, 3], 0)


if __name__ == "__main__":
    unittest.main()
