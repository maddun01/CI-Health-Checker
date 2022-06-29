from statistic import Statistic
import unittest


class StatisticTests(unittest.TestCase):

    stat = Statistic()

    # Test the get_stats method by adding items to the file,
    # then calling the method and checking the length is correct.
    # The test also makes sure the header is deleted from the list
    def test_get_stats(self):
        # Arrange
        file = open("stats.csv", "w")
        file.write("This line should be deleted\n")
        for i in range(5):
            file.write(f"This is line {i}\n")
        file.close()
        ls = ["This line should be deleted"]

        # Act
        self.stat.get_stats()
        file = open("stats.csv", "w")
        file.truncate(0)
        file.close()

        # Assert
        self.assertEqual(5, len(self.stat.stats_list))
        self.assertNotIn(ls, self.stat.stats_list)

# Test the clear_stats method by adding items to stats_list,
# then calling the method and verifying the list is empty
    def test_clear_stats_list(self):
        # Arrange
        for i in range(10):
            self.stat.stats_list.append(i)

        # Act
        self.stat.clear_stats_list()

        # Assert
        self.assertEqual(0, len(self.stat.stats_list))
