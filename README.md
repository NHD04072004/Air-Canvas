# Air Canvas

Vẽ sử dụng cử chỉ tay, không sử dụng chuột. Xây dựng với `Mediapipe` và `Opencv`

## Tổng quan về hệ thống

Thay vì sử dụng MS Pain truyền thống để vẽ, chúng ta có thể tương tác trực tiếp trên màn hình mà không sử dụng chuột. Đơn giản là sử dụng cử chỉ tay.

**Mediapipe:**  Theo dõi bàn tay theo dõi và nhận diện cử chỉ tay.

**Opencv:** Đọc, xử lý và hiển thị hình ảnh.

## Cài đặt

1. Clone dự án

```commandline
git clone https://github.com/NHD04072004/Air-Canvas.git
```

2. Tạo môi trường ảo

```commandline
python -m venv aircanvas

# Linux/MacOS
source aircanvas/bin/activate
# On Windows
aircanvas\Scripts\activate
```

3. Cài đặt gói thư viện

```commandline
pip install -r requirements.txt
```

4. Chạy

```commandline
python main.py
```

## Hướng dẫn sử dụng

### Cử chỉ vẽ

Ngón tay để tư thế như đang sử dụng bút để viết. Sau đó di chuyển để tạo nét như mong muốn.

### Chọn màu sắc

Trỏ một ngón tay đứng thẳng sau đó di chuyển về màu mà bạn mong muốn

### Xóa nét vẽ

Xòe cả bàn tay ra sau đó di chuyển qua các nét cần xóa

### Tính năng 
- Vị trí chọn màu ở thanh bên phải
- Ấn nút `q` trên bàn phím để thoát chương trình

## Demo ứng dụng

![Demo](demo.gif)