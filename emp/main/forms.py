from django.forms import ModelForm
from django import forms
from .models import Post

PURPOSE = [
    ('Purpose 1', 'Purpose 1'),
    ('Purpose 2', 'Purpose 2'),
    ('Purpose 3', 'Purpose 3'),
    ('Purpose 4', 'Purpose 4'),
    ]

MODE = [
    ('Mode 1', 'Mode 1'),
    ('Mode 2', 'Mode 2'),
    ('Mode 3', 'Mode 3'),
    ('Mode 4', 'Mode 4'),
    ]

PLACES = [
    ('Place 1', 'Place 1'),
    ('Place 2', 'Place 2'),
    ('Place 3', 'Place 3'),
    ('Place 4', 'Place 4'),
    ]

ETD = [
    ('Etd 1', 'Etd 1'),
    ('Etd 2', 'Etd 2'),
    ('Etd 3', 'Etd 3'),
    ('Etd 4', 'Etd 4'),
    ]

CLASSES = [
    ('Class 1', 'Class 1'),
    ('Class 2', 'Class 2'),
    ('Class 3', 'Class 3'),
    ('Class 4', 'Class 4'),
    ]

BOOKING_TYPE = [
    ('Booking_type 1', 'Booking_type 1'),
    ('Booking_type 2', 'Booking_type 2'),
    ('Booking_type 3', 'Booking_type 3'),
    ('Booking_type 4', 'Booking_type 4'),
    ]

CHOICES = [('one way journey', 'one way journey'),
           ('return journey', 'return journey'),
           ('multicity journey', 'multicity journey'),]


CHOICES_ = [('yes', 'yes'),
           ('no', 'no'),]

mode = []



class DateInput(forms.DateInput):
    input_type = 'date'


class mainform(forms.ModelForm):
    travel_type = forms.CharField()
    purpose = forms.CharField(widget=forms.Select(choices=PURPOSE))
    purpose_desc = forms.Textarea()
    journey_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    mode = forms.CharField(widget=forms.Select(choices=MODE))
    from_place = forms.CharField(widget=forms.Select(choices=PLACES))
    to_place = forms.CharField(widget=forms.Select(choices=PLACES))
    etd = forms.CharField(widget=forms.Select(choices=ETD))
    classs = forms.CharField(widget=forms.Select(choices=CLASSES))
    air_train = forms.CharField()
    booking_type = forms.CharField(widget=forms.Select(choices=BOOKING_TYPE))
    advance_req = forms.ChoiceField(choices=CHOICES_, widget=forms.RadioSelect)
    checker = forms.BooleanField()

    class Meta:
        model = Post
        fields = ('travel_type','purpose','purpose_desc','journey_type','mode','from_place','to_place','travel_date','etd','classs','air_train','booking_type','advance_req')
        widgets = {
            'travel_date': DateInput(),
        }
