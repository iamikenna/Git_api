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
        expected =['User: iamikenna',
                    'Repo: Employee-Appraisal-system Number of commits: ',
                    'Repo: Github_Api Number of commits: ', 'Repo: SE_Testing Number of commits: ',
                    'Repo: Stevens_Dev Number of commits: ', 'Repo: tic-tac-toe Number of commits: ','Repo: Triangle_testing Number of commits: ']
        self.assertEqual(github_api(), expected)
 
    def test_bad_user_name(self):
        self.assertNotEqual(github_api(), 'unable to fetch repos from user')
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

  