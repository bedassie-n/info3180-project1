"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/property', methods=["GET", "POST"])
def prop():
    form = PropertyForm()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        rooms = form.rooms.data
        bathrooms = form.bathrooms.data
        price = form.price.data
        ptype = form.ptype.data
        location = form.location.data
        photo = request.files['photo']
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            prop = Property(title, description, rooms, bathrooms, price, ptype, location, filename)
            db.session.add(prop)
            db.session.commit()
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Property added successfully', 'success')
            return redirect('/properties')
        else:
            flash("Photo must be either png or jpg.")
    else:
        flash_errors(form)
    return render_template("add_property.html", form=form)

@app.route('/properties')
def properties():
    properties = db.session.query(Property).all()
    return render_template("properties.html", properties=properties)


@app.route('/property/<int:propertyid>')
def get_prop():
    pass

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join('..', app.config['UPLOAD_FOLDER']), filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
