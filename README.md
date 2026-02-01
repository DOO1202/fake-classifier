# 🛡️ Review Fraud Detection System

## 📌 Giới thiệu

Dự án **Xây dựng hệ thống phát hiện gian lận trong đánh giá sản phẩm (Review Fraud Detection)** nhằm mục tiêu tự động nhận diện các đánh giá (review) **giả mạo / gian lận** trên các nền tảng thương mại điện tử dựa trên **xử lý ngôn ngữ tự nhiên (NLP)** và **Deep Learning**.

Hệ thống bao gồm:

* Pipeline **tiền xử lý dữ liệu → triển khai web**
* Mô hình học sâu dựa trên **RoBERTa + Classification Head**
* **Web demo bằng Flask** cho phép người dùng nhập review và nhận kết quả dự đoán

---

## 🧠 Kiến trúc tổng thể

```
Dataset (.csv)
   ↓
Text Preprocessing
   ↓
Tokenization (RoBERTa)
   ↓
Model Training
   ↓
Save model (.pth)
   ↓
Flask Backend
   ↓
Web UI Prediction
```

---

## 🗂️ Cấu trúc thư mục dự án

```text
fake-classifier/
│
├── data/
│   └── Final_enhanced_dataset.csv      # Dataset
│
├── static/
│   ├── robot.png                      
│   └── style.css                       # CSS cho web
│
├── templates/
│   └── index.html                      # Giao diện web (Flask + Jinja2)
│
├── app.py                              # Flask app – chạy web demo
├── backend.py                          # Xử lý logic dự đoán
├── model.py                            # Định nghĩa kiến trúc mô hình
├── model_weights.pth                   # Trọng số mô hình đã huấn luyện
│
├── train_model.ipynb                   # Huấn luyện mô hình
├── requirements.txt                    # Danh sách thư viện cần cài đặt
└── venv/                               # Môi trường ảo
```

---

## 📊 Dataset

* File: `data/Final_enhanced_dataset.csv`
* Bao gồm:

  * Văn bản đánh giá sản phẩm (review text)
  * Nhãn phân loại: **Fake / Genuine**
* Dataset đã được:

  * Làm sạch
  * Chuẩn hóa
  * Cân bằng và tăng cường dữ liệu (enhanced)

---

## 🌐 Web Demo (Flask)

### Chức năng

* Nhập nội dung review
* Model dự đoán:

  * Fake Review ❌
  * Genuine Review ✅
* Hiển thị kết quả trực tiếp trên giao diện web

### Luồng hoạt động

```text
User Input → Flask (app.py)
          → backend.py
          → model.py + model_weights.pth
          → Prediction
          → Render index.html
```

---

## ▶️ Hướng dẫn cài đặt & chạy dự án

### 1️⃣ Clone repository

```bash
git clone https://github.com/DOO1202/fake-classifier.git
cd fake-classifier
```

---

### 2️⃣ Tạo môi trường ảo

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Chạy web demo

```bash
python app.py
```

Sau đó mở trình duyệt và truy cập:

```
http://127.0.0.1:5000
```

---

## 🧠 Công nghệ sử dụng

* Python 3.10+
* PyTorch
* HuggingFace Transformers (RoBERTa)
* Flask
* Pandas, NumPy
* Matplotlib
* HTML / CSS / JavaScript

---

## 🎯 Mục tiêu & ứng dụng

* Phát hiện đánh giá gian lận trên các nền tảng thương mại điện tử
* Hỗ trợ người tiêu dùng ra quyết định mua hàng chính xác hơn
* Làm demo/đồ án môn Học Máy – Xử lý ngôn ngữ tự nhiên

---

## 🚀 Hướng phát triển

* Fine-tune toàn bộ RoBERTa
* Thêm Explainable AI (LIME / SHAP)
* Lưu lịch sử dự đoán + feedback người dùng
* Mở rộng sang các thể loại đánh giá trong lĩnh vực khác
* Deploy lên cloud (Render / HuggingFace Spaces)

---

## 👨‍💻 Tác giả

* Nhóm sinh viên thực hiện BTL Học Máy - Nhóm 3
* Mục đích: học tập & nghiên cứu

---
