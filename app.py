from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        ip_address = request.form.get('ip', '')

        # LỖ HỔNG NẰM Ở ĐÂY
        cmd = "ping -c 3 " + ip_address
        result = os.popen(cmd).read()

    # Template đơn giản, không cần file riêng
    return render_template_string("<h1>Ping</h1><form method=post><input name=ip><input type=submit></form><pre>{{result}}</pre>", result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
