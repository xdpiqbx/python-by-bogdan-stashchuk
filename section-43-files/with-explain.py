# ================================== Without with
test_file = open('test.txt', 'w')
test_file.write("first\n")
test_file.write("second\n")
test_file.close()  # <-----=== You need to close file

test_file = open('test.txt')
print(test_file.read())
test_file.close()  # <-----=== You need to close file

# ================================== Use with. Here you do not need to close
with open('test.txt', 'w') as open_to_write_file:
    open_to_write_file.write("first ===\n")
    open_to_write_file.write("second ===\n")

with open('test.txt') as open_to_read_file:
    print(open_to_read_file.read())