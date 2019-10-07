# CSV


CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format.

- Read a file


              import csv

              with open('uni_rec.csv', 'r') as csv_file:
                  csv_reader = csv.reader(csv_file)

                  for line in csv_reader:
                      print(line)
                      
 
- Ignoring the header in a file

              import csv

              with open('uni_rec.csv', 'r') as csv_file:
                  csv_reader = csv.reader(csv_file)
                  next(csv_reader)     // It will ignore the heading row
                  for line in csv_reader:
                      print(line)
                      
- Write a new file from existing data

              import csv

              with open('uni_rec.csv', 'r') as csv_file:
                  csv_reader = csv.reader(csv_file)

                  with open('new_uni_rec.csv','a+') as csv_new:
                      csv_writter = csv.writer(csv_new, delimiter=',')
                      for line in csv_reader:
                          csv_writter.writerow(line)
                          
                          
 - Dict_Reader and Dict_Writter
 
              import csv

              with open('uni_rec.csv', 'r') as csv_file:
                  csv_reader = csv.DictReader(csv_file)

                  with open('new_uni_rec.csv','w+') as csv_file_new:
                      fieldnames = ['name','branch','year','cgpa']
                      csv_writter = csv.DictWriter(csv_file_new, fieldnames=fieldnames, delimiter='\t')
                      csv_writter.writeheader()
                      for line in csv_reader:
                          csv_writter.writerow(line)
                          
- Delimeter Example

              import csv

              with open('uni_rec.csv', 'r') as csv_file:
                  csv_reader = csv.reader(csv_file)
                  with open('new_uni_rec.csv','w+') as csv_file_new:
                      csv_writter = csv.writer(csv_file_new, delimiter='\t')  // Delimiter shoud be anything like ',','/n','-','_'
                      for line in csv_reader:
                          csv_writter.writerow(line)
                          
- Read the content in Dictory format to filer the data

              import csv

              with open('uni_rec.csv', 'r') as csv_file:
                  csv_reader = csv.DictReader(csv_file)  // Read the data in dictory format

                  for line in csv_reader:
                      print(line['year'])  // dictory filter
