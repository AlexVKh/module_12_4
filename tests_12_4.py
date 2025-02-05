import module_12_4 as m
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            a = m.Runner('John', int(-10))
            for i in range(10):
                a.walk()
            logging.info("test_walk выполнен успешно")
        except ValueError as exc_value:
            logging.error("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            b = m.Runner([2], 10)
            for i in range(10):
                b.run()
            logging.info("test_run выполнен успешно")
            self.assertEqual(b.distance, 100)
        except TypeError:
            logging.error("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == '__main__':
        unittest.main()

