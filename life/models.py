from life import db

class Category(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(200))
    slug_category=db.Column(db.String(200))
    posts=db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % (self.category_name)

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(200))
    title=db.Column(db.String(350))
    slug_title=db.Column(db.String(350))
    anons=db.Column(db.String(600))
    article=db.Column(db.Text)
    pub_date=db.Column(db.DateTime)
    category_id=db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Post %r>' % (self.title)
