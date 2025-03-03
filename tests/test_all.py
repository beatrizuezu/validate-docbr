import unittest
# Classes
import tests.test_cpf
import tests.test_cns
import tests.test_cnpj


def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTests(loader.loadTestsFromModule(tests.test_cpf))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cns))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cnpj))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
