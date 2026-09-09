from datetime import date
from django.db import models
from members.models import Member
from items.models import Item
from django.db.models import F


class Payment(models.Model):
    member_id = models.ForeignKey(
        Member,
        related_name='payment',
        on_delete=models.CASCADE
    )
    item_id = models.ForeignKey(
        Item,
        related_name="item",
        on_delete=models.CASCADE
    )
    personal_contribution = models.IntegerField(
        null=True,
        blank=True
    )
    amount_paid = models.IntegerField()
    balance = models.GeneratedField(
        expression=F("cost") - F("amount_paid"),
        output_field=models.IntegerField(),
        db_persist=True
    )
    paid_on = models.DateField(default=date.today)