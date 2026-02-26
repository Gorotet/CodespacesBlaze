# test_codespacesblaze.py
"""
Tests for CodespacesBlaze module.
"""

import unittest
from codespacesblaze import CodespacesBlaze

class TestCodespacesBlaze(unittest.TestCase):
    """Test cases for CodespacesBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodespacesBlaze()
        self.assertIsInstance(instance, CodespacesBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodespacesBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
