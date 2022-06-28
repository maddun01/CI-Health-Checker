from dataUI import DataUI
import unittest


class DataUITests(unittest.TestCase):

    data_ui = DataUI()

    # Tests the name_crop method
    # Passes two example strings, one that needs cropping, and one that doesn't
    # Validates that the return values are correctly cropped
    def test_name_crop_short_name(self):
        # Arrange
        short_name = "The hand that mocked them, and the heart that fed; And on the pedestal, these words appear:"

        # Act
        short_name = self.data_ui.crop_names(short_name)

        # Assert
        self.assertEqual(
            "The hand that mocked them, and the heart that fed; And on the pedestal, these words appear:", short_name)

    def test_name_crop_long_name(self):
        # Arrange
        long_name = "My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair! Nothing beside remains."

        # Act
        long_name = self.data_ui.crop_names(long_name)

        # Assert
        self.assertEqual(
            "My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair! Nothing beside r...", long_name)
