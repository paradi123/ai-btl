from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from ultralytics import YOLO
import google.generativeai as genai
import uuid
from PIL import Image
import os
import io
import cv2

# --- Khai báo token và API key ---
TELEGRAM_TOKEN = '8120349122:AAFwbTdyisQL5D6OpTMel1hR6NacHCqpCTo'
GEMINI_API_KEY = 'AIzaSyDIX83r8PTKLtenZQiSTz3UWnZhC-na4OY'
CHAT_ID = 5694039871  # Thay bằng Chat ID thật

# --- Load mô hình YOLO ---
model = YOLO("best.pt")

# --- Khởi tạo Gemini ---
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('models/gemini-2.0-flash')

# --- Vẽ kết quả lên ảnh ---
def draw_boxes(image_path, results):
    img = cv2.imread(image_path)
    r = results[0]

    if not r.boxes:
        return image_path

    for box in r.boxes:
        cls_id = int(box.cls)
        label = r.names[cls_id]
        conf = float(box.conf[0]) if hasattr(box.conf, '__getitem__') else float(box.conf)
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{label} ({conf:.2f})", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    output_path = "output.jpg"
    cv2.imwrite(output_path, img)
    return output_path

# --- Xử lý ảnh và gọi Gemini ---
def detect_and_describe(image_path):
    results = model(image_path)
    output_image = draw_boxes(image_path, results)

    label_names = set()
    for r in results:
        if not r.boxes:
            continue
        for box in r.boxes:
            cls_id = int(box.cls)
            label_names.add(r.names[cls_id])

    if not label_names:
        return "Không phát hiện bệnh nào trên lá lúa.", output_image

    prompt = f"Mô tả ngắn gọn bệnh trên lá lúa sau: {', '.join(label_names)}."
    gemini_response = gemini_model.generate_content(prompt)
    return gemini_response.text, output_image

# --- Xử lý ảnh gửi từ Telegram ---
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    photo_file = await photo.get_file()

    img_path = f"input_{uuid.uuid4().hex}.jpg"
    await photo_file.download_to_drive(img_path)

    try:
        description, output_image = detect_and_describe(img_path)
    except Exception as e:
        await update.message.reply_text(f"Lỗi xử lý ảnh: {str(e)}")
        return

    with open(output_image, 'rb') as f:
        img_bytes = f.read()

    await update.message.reply_photo(photo=InputFile(io.BytesIO(img_bytes)), caption=description)

    os.remove(img_path)
    os.remove(output_image)

# --- Gửi tin nhắn khởi động ---
async def send_startup_message(app):
    await app.bot.send_message(chat_id=CHAT_ID, text="🌾 Bot phát hiện bệnh lá lúa đã khởi động!")

# --- Chạy bot ---
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🤖 Bot đang chạy...")
    app.post_init = send_startup_message
    app.run_polling()

if __name__ == "__main__":
    main()
