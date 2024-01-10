file_open=open('csv_data.txt','r')
file_read=file_open.readlines()
file_open.close()

lines=[line.strip() for line in file_read[1:]]

for line in lines:
    person_data=line.split(',')
    name=person_data[0].title()
    age=person_data[1]
    univ=person_data[2].capitalize()

    print(f'{name} is {age}, studing in {univ}')

sample_csv=','.join(['a','20','mit'])
print(sample_csv)