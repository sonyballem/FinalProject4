from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()


class location_edit_form(FlaskForm):
    title = TextAreaField('Title', [validators.DataRequired(), validators.length(max=300)], description="Please add information about the location")
    longitude = TextAreaField('Longitude', [validators.DataRequired(), validators.length(max=300)], description="Please add information about the location")
    latitude = TextAreaField('Latitude', [validators.DataRequired(), validators.length(max=300)], description="Please add information about the location")
    population = IntegerField('Population', [validators.DataRequired()], description="Please add information about the location")
    submit = SubmitField()


class add_location_form(FlaskForm):
    title = TextAreaField('Title', [
        validators.DataRequired(),
        validators.length(max=300)
    ], description="Name of the location")

    longitude = TextAreaField('Longitude', [
        validators.DataRequired(),
        validators.length(max=300)
    ], description="Longitude of the location")

    latitude = TextAreaField('Latitude', [
        validators.DataRequired(),
        validators.length(max=300)
    ], description="Latitude of the location")

    population = IntegerField('Population', [
        validators.DataRequired(),
    ], description="Population of the location")

    submit = SubmitField()
