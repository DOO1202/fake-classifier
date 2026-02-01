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
Raw Dataset
   ↓
Text Preprocessing
   ↓
Tokenization (RoBERTa Tokenizer)
   ↓
Deep Learning Model (RoBERTa + Classification Head)
   ↓
Model Training & Evaluation
   ↓
Saved Model Weights
   ↓
Flask Backend API
   ↓
Web Interface (HTML/CSS)
   ↓
Prediction Result
```

---

## 🗂️ Cấu trúc thư mục dự án

```text
fake-classifier/
│
├── data/                              
│   └── Final_enhanced_dataset.*      # Dataset huấn luyện
│
├── static/
│   ├── robot.png                      
│   └── style.css                     # CSS cho web
│
├── templates/
│   └── index.html                    # Giao diện web (Flask + Jinja2)
│
├── app.py                            # Flask app – chạy web demo
├── backend.py                        # Xử lý logic dự đoán
├── model.py                          # Định nghĩa kiến trúc mô hình
│
├── train_model.ipynb                 # Huấn luyện mô hình
├── requirements.txt                  # Danh sách thư viện cần cài đặt
├── .gitignore                        
└── README.md                         # Mô tả dự án
```

---

## Tải dữ liệu

Tải dataset gốc từ Kaggle:
https://www.kaggle.com/datasets/harshdecipher/amazon-enhanced-fake-reviews-datasets

Sau khi xử lý, đặt file dataset vào thư mục:

data/Final_enhanced_dataset.csv

## Tải Model Weights (nếu cần)
Nếu bạn không muốn huấn luyện mô hình từ đầu bằng file **train_model.ipynb** bạn cần tải file model đã huấn luyện sẵn (model_weights.pth)
Đặt file model weights vào thư mục gốc của dự án:

fake-classifier/
├── model_weights.pth
├── app.py
├── backend.py
├── model.py

Tải từ link: 
https://drive.google.com/file/d/1U_RAiJ0BL54ppXmSJbnj_o3G5oow0lz8/view?usp=sharing


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
