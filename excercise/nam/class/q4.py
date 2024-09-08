import os

class TextManagement:
    def __init__(self, folder) -> None:
        self.folder = folder

    def print_all_files(self):
        list_files = os.listdir(self.folder)
        
        for file in list_files:
            full_path = os.path.join(self.folder, file)
            if os.path.isfile(full_path):
                print(file)

    def read_file_content(self, file_name):
        full_path = os.path.join(self.folder, file_name)
        if os.path.isfile(full_path):
            with open(full_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        else:
            return "File not found."

    def replace_file_content(self, file_name, new_content):
        full_path = os.path.join(self.folder, file_name)
        if os.path.isfile(full_path):
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            return f"File '{file_name}' đã được thay thế nội dung."
        else:
            return "File không tồn tại."

    def create_new_file(self, new_file_name, content):
        full_path = os.path.join(self.folder, new_file_name)
        if not os.path.isfile(full_path):
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return f"File '{new_file_name}' đã được tạo."
        else:
            return f"File '{new_file_name}' đã tồn tại."

    def delete_file(self, file_name):
        full_path = os.path.join(self.folder, file_name)
        if os.path.isfile(full_path):
            os.remove(full_path)
            return f"File '{file_name}' đã bị xóa."
        else:
            return "File không tồn tại."


text_management = TextManagement('d:/test')

# In danh sách các file
text_management.print_all_files()

# Thay thế nội dung của file 'test_document.txt'
# result_replace = text_management.replace_file_content('test_document.txt', 'Siêu nhân đỏ :))')
# print(result_replace)

# Tạo file mới với nội dung do người dùng nhập
# result_create = text_management.create_new_file('new_file.txt', 'Siêu nhân xanh.')
# print(result_create)

# Xóa file 'new_file.txt'
result_delete = text_management.delete_file('new_file.txt')
print(result_delete)