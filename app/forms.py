# Here goes your forms such as login, register, etc.

# This is what a Login form could look like

"""
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Length(max=100)], render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=100)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login") 
"""

# For this you will need to install Flask-WTF