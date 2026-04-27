from flask import Flask, request
import os

app = Flask(__name__)

# ===== صفحة سياسة الخصوصية =====
@app.route('/privacy-policy')
def privacy():
    return '''
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>سياسة الخصوصية</title>
    </head>
    <body style="font-family: Arial; padding: 40px; line-height: 1.8;">
        <h1>سياسة الخصوصية</h1>
        <p>نحن لا نجمع أي بيانات شخصية من المستخدمين.</p>
        <p>هذا البوت يستخدم فقط للرد على الاستفسارات عبر Messenger.</p>
        <p>للتواصل: salahde43@gmail.com</p>
    </body>
    </html>
    '''
# ================================

# Webhook الخاص بـ Messenger (الموجود لديك)
@app.route('/webhook', methods=['GET'])
def verify():
    verify_token = request.args.get('hub.verify_token')
    if verify_token == os.getenv('VERIFY_TOKEN'):
        return request.args.get('hub.challenge')
    return 'Error', 403

@app.route('/webhook', methods=['POST'])
def webhook():
    # هنا كود معالجة الرسائل + RAG
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
