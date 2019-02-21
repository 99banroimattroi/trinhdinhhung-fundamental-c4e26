#/////////////////////////////////////////// Anser-Trịnh Đình Hùng-C4E26-TECHKIDS /////////////////////////////////////////////////
# - How to check a variable’s type ?
#
#   Anser: Để kiểm tra kiểu dữ liệu giá trị của một biến đã khởi tạo ta sử dụng hàm type()
#          Cú pháp: type(<tên biến>) # <tên biến> ở đây có thể là là một giá trị nào đó, không nhất thiết phải là biến
#   Example: 
n = 13
print(type(n))
#   =>>> Khi chạy chương trình trên sẽ cho kết quả:   <class 'int'> - Cho biết biến n có giá trị là kiểu số (int)
#
#
#
# - In what cases, you will get SyntaxError from the compiler telling you that some of your variables have invalid names?
#   Can you give 3 different examples of invalid names?
#
#   Anser: Khi ta nhập tên biến không hợp lệ
#   
#   Example 1:
# 
t = 123a
print(t)
#   =>>> SyntaxError: invalid syntax - Lỗi do nhập cú pháp không hợp lệ cụ thể khi gán n =123 là kiểu số(Int) cho đến khi thêm 
#   kí tự a vào là n = 123a thì lúc này chương trình sẽ hiểu đây là kiểu dữ liệu lưu trữ văn bản (Str). 
#   Vậy cú pháp đúng sẽ là:    t = "123a"
#
#   Example 2:
#
1 = "123a"
print(1)
#   =>>> SyntaxError: can't assign to literal - Lỗi do đối tượng bên trái của câu lệnh gán không thể là a literal
#   A literal là một string, number, tuple, list, dict, boolean, or None.
#   Vậy cú pháp đúng sẽ là:    d = "123a"
#
#   Example 3:
#
not = 1
print(not)
#
#   =>>> SyntaxError: invalid syntax - Lỗi do "not" là một định danh trong python. Nó giúp phân biệt thực thể này với thực thể khác
#   cho nên ta không thể đặt tên cho các thực thể như class, function, biến trùng với định danh cụ thể ở đây là "not".
#   Vậy cú pháp đúng sẽ là:    h = 1
#
#
#
#/////////////////////////////////////////////////////////////END/////////////////////////////////////////////////////////////////
