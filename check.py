import os

# Khai báo đúng kiểu dict và dùng raw string r'' để tránh lỗi escape
paths = {
    'Train': r'RiceLeaf_Yolov8_Version\train\images',
    'Validation': r'RiceLeaf_Yolov8_Version\valid\images',
    'Test': r'RiceLeaf_Yolov8_Version\test\images'
}

# Đếm số lượng file ảnh có đuôi jpg/jpeg/png
for name, path in paths.items():
    try:
        count = len([f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        print(f"{name}: {count} ảnh")
    except FileNotFoundError:
        print(f"{name}: Không tìm thấy thư mục ({path})")
