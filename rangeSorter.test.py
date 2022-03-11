import unittest
import rangeSorter

class rangeSorterTest(unittest.TestCase):

    def test_smallest_possible_failing(self):
        self.assertNotEqual(rangeSorter.sort_in_ranges([4,5]),"4-5, 2")

    def test_smallest_possible_passing(self):
        self.assertEqual(rangeSorter.sort_in_ranges([4,5]),"3-5,2\n10-12,0\n")

    def test_not_int_range(self): # just for 100% coverage
        self.assertEqual(rangeSorter.sort_in_ranges([0]),"3-5,0\n10-12,0\n")

    # def test_range_class_methods(self): # Not necesary for 100% coverage 
    #     # Create dummy object to test
    #     rangeExampleObject = rangeSorter.range(-2,8)
    #     # Test is_in_range_num() method with a number NOT in the range
    #     self.assertEqual(rangeExampleObject.is_in_range_num(-3),0)
    #     # Test is_in_range_num() method with a number in range
    #     self.assertEqual(rangeExampleObject.is_in_range_num(8),1)
    #     # Test get_comma_separated_line() method with a number in range and another not in range
    #     rangeExampleObject.analyze_list([5,23])
    #     self.assertEqual(rangeExampleObject.get_comma_separated_line(),"-2-8,1")

    # def unnecesary_extra_test(self):
    #     self.assertEqual(rangeSorter.sort_in_ranges([4,16,-1,3,9.-2,8]),"3-5,1\n10-12,0\n")

if __name__ == '__main__':
    unittest.main()