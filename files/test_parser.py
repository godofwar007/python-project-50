from gendiff.file_parser import load_json

file1_data = load_json('file1.json')
file2_data = load_json('file2.json')

print("file1.json:", file1_data)
print("file2.json:", file2_data)
