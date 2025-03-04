from flask import Flask, request, jsonify

app = Flask(__name__)

# 首页路由，返回一个简单的欢迎信息
@app.route('/')
def home():
    return 'Welcome to the Flask application!'

# 动态路由，接收一个参数并返回问候信息
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

# 获取查询参数，返回包含查询参数的消息
@app.route('/search')
def search():
    query = request.args.get('query', '')  # 获取 URL 中的查询参数，默认为空
    return f'You searched for: {query}'

# # 处理 POST 请求，接收 JSON 数据
@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()  # 获取 JSON 请求体
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    result = num1 + num2

    return jsonify({'result': result})

# curl -X POST http://127.0.0.1:5000/add \
#     -H "Content-Type: application/json" \
#     -d '{"num1": 5, "num2": 10}' linux命令行



# # 路由示例，处理上传文件
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['file']  # 获取上传的文件
#     filename = file.filename
#     file.save(f'./uploads/{filename}')  # 保存文件到指定路径
#     return f'File {filename} uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
