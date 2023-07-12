import csv, _csv

# with open('test.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([1, 'elly', 432])
#     writer.writerow([2, 'bill', 65])
#     writer.writerow([3, 'john', 123])

# def csv_reader_to_dict(csv_reader: _csv.reader) -> list:
#     res_list = list()
#     first_line = list()
#
#     for line in csv_reader:
#         first_line = line
#         break
#
#     for line in csv_reader:
#         res_dict = dict()
#         for i in range(len(first_line)):
#             res_dict[first_line[i]] = line[i]
#         res_list.append(res_dict)
#
#     return res_list

# Or

def csv_reader_to_dict(csv_reader: _csv.reader) -> list:
    res_list = []
    first_line = next(csv_reader)

    for line in csv_reader:
        res_dict = dict(zip(first_line, line))
        res_list.append(res_dict)

    return res_list

with open('test.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    print(reader)  # <_csv.reader object at 0x000001DD8586AE60>
    print(type(reader))  # <class '_csv.reader'>

    # print(list(reader))

    # for line in reader:
    #     print(reader.line_num)
    #     print(line)

    # for line in reader:
    #     print(reader.line_num)
    #     print(line)

    print(csv_reader_to_dict(reader))






