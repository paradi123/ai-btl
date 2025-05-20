# 🌿 Hệ thống Phát hiện Bệnh Lá Cây & Tư vấn Tự động qua Chatbot

Dự án kết hợp mô hình học sâu **YOLOv8** và **YOLOv11** để phát hiện bệnh trên lá cây, cùng với tích hợp **Gemini Flash** (mô hình ngôn ngữ) và **Telegram Bot** nhằm cung cấp phân tích bệnh và tư vấn cách xử lý qua trò chuyện tự động.

## 🚀 Tính năng chính

- 📸 Phát hiện nhanh các bệnh phổ biến trên lá cây qua ảnh bằng YOLOv8 và YOLOv11.
- 🤖 Tạo chatbot Telegram cho phép người dùng gửi ảnh và nhận kết quả phân tích bệnh.
- 🧠 Gemini Flash được sử dụng để sinh phản hồi tự nhiên, chi tiết về nguyên nhân và cách khắc phục bệnh.
- ☁️ Hỗ trợ triển khai trên môi trường cục bộ hoặc cloud.

## 📷 Mô hình phát hiện bệnh lá cây

Sử dụng mô hình **YOLOv5** được huấn luyện với tập dữ liệu ảnh về lá cây bệnh (ví dụ: cháy lá, đốm nâu, vàng lá, nấm...). Mô hình đầu ra trả về vùng ảnh chứa bệnh và nhãn bệnh tương ứng.

## 🧠 Phân tích bệnh với Gemini Flash

Sau khi YOLO phát hiện loại bệnh, hệ thống gửi kết quả đến **Gemini Flash** để sinh câu trả lời tự nhiên, như:
- Miêu tả bệnh
- Nguyên nhân
- Cách phòng ngừa & điều trị

## 💬 Chatbot Telegram

Người dùng tương tác qua Telegram:
1. Gửi ảnh lá cây
2. Nhận phản hồi tự động:
   - Hình ảnh có vùng bệnh được đánh dấu
   - Tên bệnh
   - Tư vấn chi tiết

## 📦 Cài đặt

### 1. Clone dự án
```bash
git clone https://github.com/ten_tai_khoan/phat-hien-benh-cay-chatbot.git
cd phat-hien-benh-cay-chatbot
