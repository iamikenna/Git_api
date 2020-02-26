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
    """Mocking the git_hub function in order to reduce its dependency"""
    @mock.patch('HW_04_Ikenna_Ibezim_api.github_api')
    def test_github_api(self, mock_simple_func):
        expected =['User: iamikenna', 'Repo: Employee-Appraisal-system Number of commits: 1', 'Repo: Git_api Number of commits: 15', 'Repo: SE_Testing Number of commits: 2', 'Repo: Stevens_Dev Number of commits: 3', 'Repo: tic-tac-toe Number of commits: 1', 'Repo: Triangle_testing Number of commits: 11']
        mock_simple_func.return_value = "you have mocked it"
        result = HW_04_Ikenna_Ibezim_api.github_api()
        self.assertEqual(result, "you have mocked it")
        
        mock_simple_func.return_value = github_api()
        result2 = HW_04_Ikenna_Ibezim_api.github_api()
        
        self.assertEqual(result2, expected)
        self.assertNotEqual(result2, 'unable to fetch repos from user')
        print(result, result2)
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
   
   
   