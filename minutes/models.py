from django.db import models
from datetime import date

class Minutes(models.Model):
    heading = models.TextField()
    sub_heading = models.TextField()
    date = models.DateField(default=date.today)
    opening = models.TextField()
    members_present = models.TextField()
    members_absent = models.TextField()
    agenda_approval = models.TextField()
    approval_of_minutes = models.TextField()
    business_from_previous_meeting = models.TextField()
    new_business = models.TextField()
    agenda_for_next_meeting = models.TextField()
    closure = models.TextField()
    minutes_submitted_by = models.CharField()
    approved_by = models.CharField()



"""

id, heading, subheading, Date, Opening, members_present, members_absent, agenda_approval, 
approval_of_minutes, business_from_previous_meeting, new_business, agenda_for_next_meeting, 
closure, minutes_submitted_by, approved_by.
"""