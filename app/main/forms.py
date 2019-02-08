from flask_wtf import FlaskForm
from wtforms import StringField , BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators= [Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))

'''
When you add any methods that match the pattern validate_<field_name>, WTForms takes those as custom validators 
and invokes them in addition to the stock validators.
'''

class PostForm(FlaskForm):
    post = TextAreaField(_l("Say Something!"), validators=[DataRequired(),Length(1,140)])
    submit= SubmitField(_l("Post"))