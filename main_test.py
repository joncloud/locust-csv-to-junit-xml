from main import main
import junitparser
import os
import unittest

def convert_results(prefix: str) -> str:
  xml_file_path = os.path.join(
    os.getcwd(),
    'test_results.xml'
  )
  if os.path.isfile(xml_file_path):
    os.remove(xml_file_path)

  argv = [
    '--prefix', prefix
  ]
  main(argv)
  return xml_file_path

class TestMain(unittest.TestCase):

  def assert_file(self, prefix: str, test_case_names: list[str]) -> None:
    xml_file_path = convert_results(prefix)
    self.assertTrue(os.path.isfile(xml_file_path))

    junit_xml = junitparser.JUnitXml.fromfile(xml_file_path)

    test_suites = list(junit_xml)
    self.assertEqual(len(test_suites), 1)

    test_suite = test_suites[0]
    self.assertEqual(test_suite.name, 'Locust Tests')
    self.assertGreater(test_suite.tests, 0)
    self.assertGreater(test_suite.failures, 0)

    test_cases = list(test_suite)
    self.assertEqual(len(test_cases), len(test_case_names))

    for index, test_case_name in enumerate(test_case_names):
      self.assertEqual(test_cases[index].name, test_case_name)
      self.assertEqual(type(test_cases[index].time), float)

    return

  def test_conversion(self):
    self.assert_file('prefix1', [
      'GET\t/ Average response time',
      'GET\t/fail Average response time',
    ])

    self.assert_file('prefix2', [
      'GET\t/ Average response time',
      'GET\t/fail Average response time',
    ])
    return

if __name__ == '__main__':
  unittest.main()
