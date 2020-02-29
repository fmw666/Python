from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import NewsForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:fmw19990718@localhost:3306/net_news?charset=utf8'
app.config['SECRET_KEY'] = 'a random string'
db = SQLAlchemy(app)

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300), )
    author = db.Column(db.String(20), )
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    # 新闻首页
    # news_list = News.query.all()
    news_list = News.query.filter_by(is_valid=1)
    return render_template('index.html', news_list=news_list)

@app.route('/cat/')
@app.route('/cat/<name>/')
def cat(name=None):
    # 新闻类别，查询类别为 name 的新闻数据
    news_list = News.query.filter(News.types==name)
    return render_template('cat.html', name=name, news_list=news_list)

@app.route('/detail/<int:pk>/')
def detail(pk):
    # 新闻详情信息
    news_obj = News.query.get(pk)
    return render_template('detail.html', news_obj=news_obj)

@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    # 新闻后台管理首页
    if page is None:
        page = 1
    news_list = News.query.filter_by(is_valid=True).paginate(page=page, per_page=5)
    return render_template('admin/index.html', news_list=news_list)

@app.route('/admin/add/', methods=('GET', 'POST'))
def add():
    # 新闻后台数据新增
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        new_obj = News(
            title = form.title.data,
            content = form.content.data,
            types = form.types.data,
            image = form.image.data,
            created_at = datetime.now(),
            is_valid = True
        )
        # 保存数据
        db.session.add(new_obj)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('admin/add.html', form=form)

@app.route('/admin/update/<int:pk>/', methods=('GET', 'POST'))
def update(pk):
    # 新闻后台数据修改
    news_obj = News.query.get(pk)
    # 如果没有数据，则返回
    if not news_obj:
        return redirect(url_for('admin'))
    form = NewsForm(obj=news_obj)
    if form.validate_on_submit():
        # 获取数据
        news_obj.title = form.title.data
        news_obj.content = form.content.data
        # 保存数据
        db.session.add(news_obj)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('admin/update.html', form=form)

@app.route('/admin/delete/<int:pk>/', methods=('GET', 'POST'))
def delete(pk):
    # 新闻后台数据删除
    news_obj = News.query.get(pk)
    if not news_obj:
        return 'no'
    news_obj.is_valid = False
    db.session.add(news_obj)
    db.session.commit()
    return 'yes'


if __name__ == "__main__":
    app.run(debug=True)