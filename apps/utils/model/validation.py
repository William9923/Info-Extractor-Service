from wtforms import StringField, StringField, validators, Form, TextAreaField

class TextForm(Form):
    algo = StringField("Algorithm", [validators.DataRequired()])
    keyword = StringField("Keyword", [validators.DataRequired()])
    content = TextAreaField("Content", [validators.DataRequired()])

class ScrapperForm(Form):
    algo = StringField("Algorithm", [validators.DataRequired()])
    keyword = StringField("Keyword", [validators.DataRequired()])
    url = StringField("Target URL", [validators.DataRequired(), validators.URL()])
    