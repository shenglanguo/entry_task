# 导入Flask类
from flask import Flask, jsonify
from flask import render_template
from flask import request
import json
# 实例化，可视为固定格式
app = Flask(__name__)

@app.route('/query.html')
def query_html():
    # 使用render_template()方法重定向到templates文件夹下查找post.html文件
    return render_template('query.html')

@app.route('/queryresult', methods = ['GET', 'POST'])
def deal_request():
    student_list = [{'name': '张三', 'age': '18'}, {'name': '李四','age': '17'}, {'name': 'wangwu','age': '18'}, {'name': '张无忌','age': '22'}]
    query_list = []
    #默认返回内容
    return_dict = {'return_code': 200, 's': 'success!', 'result': False}
    if request.method == "GET":
        get_name = request.args.get("name", "").strip("")
        if get_name == '' or get_name == None:
            return {'return_code': 200, 'return_info': 'Please input word wanted to be query!', 'result': False}
        else:
            for i in student_list:
                if str(i['name']).startswith(get_name):
                    query_list.append(i)
            return_dict['result'] = query_list
            return json.dumps(return_dict, ensure_ascii=False)
    elif request.method == "POST":
        # return render_template("result.html", result="Bad request method!")
        return {'return_code': 404, 'return_info': 'Bad request method!', 'result': False}


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    app.run()