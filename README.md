# VN Phone Number

Thư viện này tái sử dụng thư viện [python-phonenumbers ](https://github.com/daviddrysdale/python-phonenumbers.git) để làm những việc sau:
- Chuẩn hóa các kiểu viết số điện thoại của người dùng VN về dạng 10 số `0981234567`.
- Tách tất cả số điện thoại trong văn bản và chuẩn hóa về dạng 10 số như trên.

Cài đặt (thêm vào project như một sub-module):
```
$ git submodule add https://github.com/vic4key/phone-number-extract-and-normalize.git vn_phone_number
```

Sử dụng:
```python
from vn_phone_number import *
normalize_phone_number(text: str) -> str
extract_phone_numbers(text: str) -> list
```

Một kiểu viết đã được chuẩn hóa ví dụ như dưới đây:
```python
# None
981234567
98 123 4567
98.123.4567
98-123-4567

# 098
0981234567
098 123 4567
098.123.4567
098-123-4567

# 84
84981234567
84 98 123 4567
84 98.123.4567
84 98-123-4567

# 84 098
840981234567
84 098 123 4567
84 098.123.4567
84 098-123-4567

# (84)
(84)981234567
(84) 98 123 4567
(84) 98.123.4567
(84) 98-123-4567

# (84) 098
(84)0981234567
(84) 098 123 4567
(84) 098.123.4567
(84) 098-123-4567

# +84
+84981234567
+84 98 123 4567
+84 98.123.4567
+84 98-123-4567

# +84 098
+840981234567
+84 098 123 4567
+84 098.123.4567
+84 098-123-4567

# (+84)
(+84)981234567
(+84) 98 123 4567
(+84) 98.123.4567
(+84) 98-123-4567

# (+84) 098
(+84)0981234567
(+84) 098 123 4567
(+84) 098.123.4567
(+84) 098-123-4567
```
