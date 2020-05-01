from unittest import TestCase
from testing_lesson.printer import Printer, PrinterError


class PrinterTests(TestCase):
    def setUp(self):
        self._printer = Printer(105, 3.0)

    def test_print_when_successful_returns_expected_report(self):
        # Act
        report = self._printer.print(51)

        # Assert
        self.assertEqual((51, 17.0, 54), report)

    def test_print_when_not_enough_paper_raises_PrinterError(self):
        # Arrange, Act, and Assert
        with self.assertRaises(PrinterError):
            self._printer.print(106)

    def test_print_remaining_capacity_reduced_after_print(self):
        # Arrange
        self._printer.print(55)

        # Act
        self.assertEqual(50, self._printer.remaining_capacity)

    def test_print_remaining_capacity(self):
        # Act
        self._printer.print(self._printer.remaining_capacity)

        # Assert
        self.assertEqual(0, self._printer.remaining_capacity)

    def test_speed_rounding(self):
        # Act
        report = self._printer.print(11)

        # Assert
        self.assertEqual(3.7, report.pages_per_second)
