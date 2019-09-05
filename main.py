#!/usr/bin/python

import csv, datetime, getopt, sys
import xml.etree.ElementTree as ET

def main(argv):
    prefix = ''

    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'hp:',['prefix='])
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
    xml_tree.write("test_results.xml")

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

    with open(prefix + '_requests.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                testcase = ET.SubElement(testsuite, 'testcase')
                testcase.set('name', f'{row["Method"]}\t{row["Name"]} Average response time')
                test_count += int(row['# requests'])
                failure_count += int(row['# failures'])
                testcase.set('time', row['Average response time'])
            line_count += 1
        
        testsuite.set('tests', str(test_count))
        testsuite.set('failures', str(failure_count))

if __name__ == '__main__':
    main(sys.argv[1:])
