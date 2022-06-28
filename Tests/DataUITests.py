from DataUI import DataUI
import unittest


class DataUITests(unittest.TestCase):

    data_ui = DataUI()

    # Tests the name_crop method
    # Passes two example strings, one that needs cropping, and one that doesn't
    # Validates that the return values are correctly cropped
    def test_name_crop_short_name(self):
        # Arrange
        SHORT_NAME = "The hand that mocked them, and the heart that fed; And on the pedestal, these words appear:"

        # Act
        SHORT_NAME = self.data_ui.crop_names(SHORT_NAME)

        # Assert
        self.assertEqual(
            "The hand that mocked them, and the heart that fed; And on the pedestal, these words appear:", SHORT_NAME)

    def test_name_crop_long_name(self):
        # Arrange
        LONG_NAME = "My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair! Nothing beside remains."

        # Act
        LONG_NAME = self.data_ui.crop_names(LONG_NAME)

        # Assert
        self.assertEqual(
            "My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair! Nothing beside r...", LONG_NAME)
