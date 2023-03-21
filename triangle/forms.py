from django.core.validators import MinValueValidator
from django.forms import fields, forms


class TriangleForm(forms.Form):
    leg1 = fields.FloatField(label="Leg 1", validators=[MinValueValidator(0.0000000000000000001)])
    leg2 = fields.FloatField(label='Leg 2', validators=[MinValueValidator(0.0000000000000000001)])