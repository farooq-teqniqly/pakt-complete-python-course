import file_lesson.file_operations as fops

fops.save("Hello World!", "foo.txt")
print(fops.read_as_string("foo.txt"))


