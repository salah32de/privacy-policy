from flask import Flask

app = Flask(__name__)

@app.route('/privacy-policy')
def privacy():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>سياسة الخصوصية</title>
    </head>
    <body style="font-family: Arial; padding: 40px; line-height: 1.8;">
        <h1>سياسة الخصوصية</h1>
        <p>نحن لا نجمع أي بيانات شخصية من المستخدمين.</p>
        <p>هذا الموقع مخصص لعرض سياسة الخصوصية فقط.</p>
        <p>للتواصل: salahde43@gmail.com</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
