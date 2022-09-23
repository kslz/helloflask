# Flask

## 第一章 初识Flask

### 1、demo

```python
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'
```

启动pipenv shell： `pipenv shell`

powershell中修改FLASK_APP： `$env:FLASK_APP = "hello.py"`

启动flask shell： `flask shell`

#### 1.1、创建实例

向Flask类构造方法中传入模块或包的名称 `__name__` 

#### 1.2、注册路由

我们需要建立处理请求的函数并为其配置对应的URL规则。

使用 `app.route()` 装饰器并传入URL规则作为参数，这个过程被称为注册路由（route），这个函数被称为视图函数（view function）。

#### 1.3、为视图绑定多个URL

```python
@app.route('/hi')
@app.route('/hello')
def say_hello():
	return '<h1>Hello, Flask!</h1>'
```

#### 1.4、动态URL

在URL规则中使用 `<变量名>` 的形式传递变量

```python
@app.route('/greet/<name>')
def greet(name):
	return '<h1>Hello, %s!</h1>' % name
```

为URL规则设置默认name值

```python
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
	return '<h1>Hello, %s!</h1>' % name

# 等价于

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name='Programmer'):
	return '<h1>Hello, %s!</h1>' % name

```

