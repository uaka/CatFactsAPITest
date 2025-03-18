
# **🐱 Cat Facts API Test**
This project contains **automated tests** for the [Cat Facts API](https://catfact.ninja/) using **pytest** and **requests**.  

The tests verify that the API correctly returns **random cat facts** and **multiple facts**, ensuring the response format and data integrity.  
Many thanx to GPT and cats Kuzia 🐈‍⬛ and Bulka 😺 with supporting me during implementing this test task. This is my first python test automation experience!
---

## **📌 Test Cases**
| Test Name | Description | Expected Result | Validation |
|-----------|------------|----------------|------------|
| `test_get_random_fact` | Fetches a random cat fact from `/fact` | Response contains a `"fact"` field (non-empty string) and `"length"` field | Check status code (`200`), `"fact"` is a string, `"length"` matches fact length |
| `test_get_multiple_facts` | Fetches multiple cat facts from `/facts?limit=3` | Response contains `"data"` field, which is a list of 3 facts | Check status code (`200`), `"data"` is a list, each fact is a string |

---

## **⚙️ Setup & Installation**
### **1️⃣ Install Dependencies**
Make sure you have Python installed, then run:
```sh
pip install -r requirements.txt
```
_(If you don’t have `requirements.txt`, install manually with: `pip install requests pytest`)_  

### **2️⃣ Run the Tests**
Run all tests using pytest:
```sh
pytest test_cat_facts.py
```
Run a specific test:
```sh
pytest -k "test_get_random_fact"
```

---

## **📸 GIF – Test Execution**
![Test Run](assets/test_run.gif)  
_(This GIF demonstrates the script running locally, verifying API responses.)_

---

## **🛠️ Technologies Used**
- **Python** (3.x)
- **pytest** (for test execution)
- **requests** (for API calls)

---

## **📩 Submission**
1. Upload the project to **GitHub**.  
2. Ensure the **GIF** (`test_run.gif`) is included in `assets/`.  
3. Send the **GitHub repository link** to the recruiter.  

---

### 🎯 **Happy Testing! 🚀**  

Let me know if you need modifications! 😊