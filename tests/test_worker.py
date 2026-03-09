import unittest


from src.services.woker import InMemoryWorker, Job


class TestWorker(unittest.TestCase):
    def test_fifo_and_drain(self):
        worker: InMemoryWorker[int] = InMemoryWorker()
        worker.enqueue(Job(id="1", payload=10))
        worker.enqueue(Job(id="2", payload=20))

        seen = []

        def handler(job: Job[int]) -> None:
            seen.append((job.id, job.payload))

        processed = worker.drain(handler)
        self.assertEqual(processed, 2)
        self.assertEqual(seen, [("1", 10), ("2", 20)])
        self.assertEqual(worker.size(), 0)

    def test_pop_empty(self):
        worker = InMemoryWorker()
        self.assertIsNone(worker.pop())


if __name__ == "__main__":
    unittest.main()
