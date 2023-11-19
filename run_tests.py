import unittest


def create_test_suite():
    loader = unittest.TestLoader()
    start_dir = 'tests'  # Specify the starting directory for tests discovery
    suite = loader.discover(start_dir, pattern='test_*.py', top_level_dir='.')
    return suite


if __name__ == '__main__':
    test_suite = create_test_suite()

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
