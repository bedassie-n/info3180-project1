from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, Regexp

class PropertyForm(FlaskForm):
    title = StringField("Property Title", [DataRequired()])
    description = TextAreaField("Description",[DataRequired()])
    rooms = StringField("No. of Rooms", [DataRequired()])
    bathrooms = StringField("No. of Bathrooms",[DataRequired()])
    price = StringField("Price", [DataRequired()])
    ptype = SelectField("Property Type", [DataRequired()], choices=["House", "Apartment"])
    location = StringField("Location", [DataRequired()])
    photo = FileField("Photo", [DataRequired(), Regexp('^[^/\\]+\.((png)|(jpg)|jpeg)$')])
 