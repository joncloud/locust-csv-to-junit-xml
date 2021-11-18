#!/usr/bin/python

import csv
import datetime
import getopt
import os
import sys
import xml.etree.ElementTree as ET


def main(argv):
    prefix = ''

    try:
        opts, _ = getopt.getopt(argv, 'hp:', ['prefix='])
    except getopt.GetoptError:
        print('main.py -p <prefix>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -p <prefix>')
            sys.exit()
        elif opt in ("-p", "--prefix"):
            prefix = arg

    if prefix == '':
        raise Exception('Prefix was not assigned')

    testsuites, testsuite = create_testsuites()
    append_testcases(prefix, testsuite)

    xml_tree = ET.ElementTree(testsuites)
    xml_file_path = os.path.join(os.getcwd(), 'test_results.xml')
    xml_tree.write(xml_file_path)


def create_testsuites():
    testsuites = ET.Element('testsuites')

    testsuite = ET.SubElement(testsuites, 'testsuite')
    testsuite.set('name', 'Locust Tests')

    timestamp = str(datetime.datetime.now()).replace(
        ' ',
        'T'
    )
    testsuite.set('timestamp', timestamp)

    return (testsuites, testsuite)


def append_testcases(prefix, testsuite):
    test_count = 0
    failure_count = 0
    csv_file_path = os.path.join(os.getcwd(), prefix + '_stats.csv')

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:

            row_method = row['Type']
            row_name = row['Name']

            if row_method != '' and row_method != 'None' and row_name != 'Total':
                testcase = ET.SubElement(testsuite, 'testcase')

                name = f'{row_method}: {row_name}'
                testcase.set('name', name)

                test_count += int(row['Request Count'])
                failure_count += int(row['Failure Count'])
                avg_response_s = float(row['Average Response Time']) / 1000
                testcase.set('time', str(avg_response_s))

        testsuite.set('tests', str(test_count))
        testsuite.set('failures', str(failure_count))


if __name__ == '__main__':
    main(sys.argv[1:])
