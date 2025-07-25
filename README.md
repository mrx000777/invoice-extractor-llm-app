
# 🧾 Invoice Extractor App using Google Gemini Pro Vision

A modern LLM-powered web application to extract structured invoice information from images and PDF files. This project leverages **Google Gemini Pro Vision (multimodal large model)** to intelligently identify and extract fields like **invoice number, date, total amount**, and more using **natural language understanding and visual parsing**.

---

## 🚀 Features

- 📸 Upload image/PDF invoices and extract key data fields instantly
- 🤖 Powered by Google Gemini Pro Vision (multimodal LLM)
- ⚡ Real-time extraction with structured JSON output
- 🧠 Intelligent text interpretation using advanced vision-language model
- 🖥️ Clean and simple UI built with **Streamlit**

---

## 🧠 Tech Stack

| Component       | Tech Used                          |
|----------------|-------------------------------------|
| LLM API        | Google Gemini Pro Vision            |
| Frontend       | Streamlit                           |
| Backend        | Python                              |
| Deployment     | Streamlit Cloud / Docker (optional) |
| Model Type     | Multimodal Large Language Model     |

---

## 📝 Input Example

Upload a file like this:

```
Invoice # 14567  
Date: 2024-12-01  
Total: ₹ 5,500  
Vendor: ABC Pvt. Ltd.
```

---

## 📤 Output Format

```json
{
  "invoice_number": "14567",
  "date": "2024-12-01",
  "total_amount": "₹5,500",
  "vendor_name": "ABC Pvt. Ltd."
}
```

---

## 📦 How to Run Locally

```bash
git clone https://github.com/yourusername/invoice-extractor-gemini.git
cd invoice-extractor-gemini
pip install -r requirements.txt
streamlit run app.py
```

> 💡 Make sure to add your **Google Gemini API key** in a `.env` or `config.py` file.

---

## 📁 Project Structure

```
invoice-extractor-gemini/
├── app.py
├── utils.py
├── requirements.txt
├── README.md
└── sample_invoices/
```

---

## 🔐 Environment Variables

Add your API key to a `.env` or config:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## 📸 Screenshots

![Upload Interface](./screenshots/upload_ui.png)  
*Upload PDF or image invoices and view the extracted fields in real-time.*
<img width="1204" height="416" alt="Screenshot 2025-07-25 181823" src="https://github.com/user-attachments/assets/e8376077-384f-4a38-adb9-f009b3a0c729" />

---
<img width="1144" height="614" alt="Screenshot 2025-07-25 170514" src="https://github.com/user-attachments/assets/5ae2a75e-201e-47cc-8226-0b2b9b2d536c" />

## 🙌 Acknowledgements

- [Google Gemini Pro Vision](https://deepmind.google/technologies/gemini/)
- [Streamlit](https://streamlit.io/)
- [Python](https://www.python.org/)

---

## 📬 Contact

**Manish Thakur**  
[LinkedIn](https://www.linkedin.com/in/manish-thakur-2b3176236) | [GitHub](https://github.com/mrx000777)

---

## 🏷️ Tags

`LLM` `Google Gemini` `Multimodal AI` `Invoice OCR` `Streamlit` `Computer Vision` `Document AI`
