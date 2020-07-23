from wtforms import StringField, StringField, validators, Form, TextAreaField

# Text Form Input Validation
class TextForm(Form):
    algo = StringField("Algorithm", [validators.DataRequired()])
    keyword = StringField("Keyword", [validators.DataRequired()])
    content = TextAreaField("Content", [validators.DataRequired()])

# Scrapper Form Input Validation
class ScrapperForm(Form):
    algo = StringField("Algorithm", [validators.DataRequired()])
    keyword = StringField("Keyword", [validators.DataRequired()])
    url = StringField("Target URL", [validators.DataRequired(), validators.URL()])
    