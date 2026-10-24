import unittest

from src.agentrisk.baseline_median import calculate_mae


class TestCalculateMAE(unittest.TestCase):
    def test_calculates_mean_absolute_error(self):
        predictions = [2, 2, 2]
        gold_labels = [1, 2, 5]

        self.assertAlmostEqual(
            calculate_mae(predictions, gold_labels),
            4 / 3,
        )

    def test_perfect_predictions_have_zero_mae(self):
        labels = [1, 3, 5]

        self.assertEqual(calculate_mae(labels, labels), 0)

    def test_empty_dataset_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_mae([], [])

    def test_different_lengths_raise_error(self):
        with self.assertRaises(ValueError):
            calculate_mae([2, 3], [2])


if __name__ == "__main__":
    unittest.main()
