# Χρήση της επίσημης βασικής εικόνας της Python
FROM python:3.9

# Ορισμός του εργασιακού φακέλου μέσα στον εκτελέσιμο χώρο του container
WORKDIR /app

# Αντιγραφή του αρχείου requirements.txt στον container
COPY requirements.txt .

# Εγκατάσταση των εξαρτήσεων της Python
RUN pip install --no-cache-dir -r requirements.txt

# Αντιγραφή των υπόλοιπων αρχείων της εφαρμογής στον container
COPY . .

# Εκτέλεση της εφαρμογής όταν ξεκινά ο container
CMD ["python", "app.py"]

