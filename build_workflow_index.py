
import re

def parse_file(filename):
    category = ''
    lastline = ''
    records = []

    with open(filename, 'rt') as f:
        for line in f:
            if '----' in line:
                category = lastline.strip()
            elif '*' == line[0] or line[0] == '#':
                if line[0] == '*': # .md
                    regex = '\* \[(.+)]\((.*)\)(?: - (.*)|)'

                    m = re.match(regex, line)

                    name = m.group(1)
                    url = m.group(2)
                    description = m.group(3)

                elif line[0] == '#': # .rest
                    regex = "#. (.*) (http.*)"
                    m = re.match(regex, line)

                    name = m.group(1)
                    url = m.group(2)
                    description = ''

                    if ' http' in name:
                        s = name.split(' http')
                        name = s[0]
                        url = 'http' + s[1]

                row = ( name, url, description, category, filename, line )
                records.append(row)

            lastline = line
    return records


import csv
with open('workflows.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    header = 'name', 'url', 'description', 'category', 'filename', 'line'
    writer.writerow(header)
    for filename in ['sources/awesome-pipeline/README.md',
                 'sources/common-workflow-language-wiki/Existing-Workflow-systems.rest']:

        records = parse_file(filename)
        writer.writerows(records)


