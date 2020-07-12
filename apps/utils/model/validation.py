from wtforms import StringField, StringField, validators, Form, TextAreaField

class TextForm(Form):
    algo = StringField("Algorithm", [validators.required()])
    keyword = StringField("Keyword", [validators.required()])
    content = TextAreaField("Content", [validators.required()])