"""
Author: Ikenna Ibezim
Write a program to classify triangles
Test cases for HW1
"""
import unittest
from unittest import mock
from HW_04_Ikenna_Ibezim_api import github_api
from unittest.mock import Mock, patch
from nose.tools import assert_is_none, assert_list_equal
import HW_04_Ikenna_Ibezim_api


class TestGetRepo(unittest.TestCase):

    @mock.patch('HW_04_Ikenna_Ibezim_api.github_api')
    def test_github_api(self, mock_simple_func):
        # print(mock_simple_func)
        # print(HW_04_Ikenna_Ibezim_api.github_api)
        seen = github_api()
        expected =['User: iamikenna', 'Repo: Employee-Appraisal-system Number of commits: 1', 'Repo: Git_api Number of commits: 16', 'Repo: SE_Testing Number of commits: 2', 'Repo: Stevens_Dev Number of commits: 3', 'Repo: tic-tac-toe Number of commits: 1', 'Repo: Triangle_testing Number of commits: 11']
        mock_simple_func.return_value = seen
        result = HW_04_Ikenna_Ibezim_api.github_api()
        self.assertEqual(result, expected)
      
 
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
   
   
   