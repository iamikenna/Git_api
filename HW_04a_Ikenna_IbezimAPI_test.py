"""
Author: Ikenna Ibezim
Write a program to classify triangles
Test cases for HW1
"""
import unittest
from HW_04_Ikenna_Ibezim_api import github_api
""" Iteration test for all functions"""

class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected =['User: iamikenna', 'Repo: Employee-Appraisal-system Number of commits: 1', 'Repo: Git_api Number of commits: 7', 'Repo: SE_Testing Number of commits: 2', 'Repo: Stevens_Dev Number of commits: 3', 'Repo: tic-tac-toe Number of commits: 1', 'Repo: Triangle_testing Number of commits: 9']
        self.assertEqual(github_api(), expected)
 
    def test_bad_user_name(self):
        self.assertNotEqual(github_api(), 'unable to fetch repos from user')
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

  
