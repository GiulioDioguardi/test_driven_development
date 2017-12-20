#!/usr/bin/python

import unittest

def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    median = 0
    median_index = int(len(nums) / 2)
    if len(nums) % 2 == 0:
        median = (nums[median_index] + nums[median_index - 1]) / 2.0
    else:
        median = float(nums[median_index])
    return median

class TestMedian(unittest.TestCase):
    def test_uneven_count(self):
        self.assertEquals(2.0, find_median_sorted_arrays([1,3], [2]))

    def test_even_count(self):
        self.assertEquals(2.5, find_median_sorted_arrays([1, 2], [3, 4]))

if __name__ == "__main__":
    unittest.main()
