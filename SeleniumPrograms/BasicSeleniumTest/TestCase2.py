import unittest


def setupmodule():
    print('this is setup module method')


def tear_down_module():
    print('this is tear down module method')


class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setup class method' + '\n')

    @classmethod
    def tearDownClass(cls):
        print('this is tear down class method')

    @classmethod
    def setUp(cls):
        print('this is setup method')

    @classmethod
    def tearDown(cls):
        print('this is tear down method')

    def test001_login_method(self):
        print('this is login method')

    def test002_logout_method(self):
        print('this is logout method')


if __name__ == '__main__':
    unittest.main
