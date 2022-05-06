from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class CompetitionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    min_participants = IntegerField("Min Participants", validators=[DataRequired()])
    join_cost = IntegerField("Join Cost", validators=[InputRequired()]) # InputRequired is necessary if 0 is expected
    payout = SelectField("Payout", choices=[('100,0,0', '100,0,0'),
                                            ('70,20,10', '70,20,10'),
                                            ('60,30,10', '60,30,10')])
    starting_reward = IntegerField("Starting Reward", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    min_score = IntegerField("Min. Score", validators=[DataRequired()])
    submit = SubmitField('Create Competition')
