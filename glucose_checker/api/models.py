from django.db import models


class GlucoseReading(models.Model):
    """Model for storing a single glucose reading."""

    class ReadingType(models.IntegerChoices):
        """Reading type choices."""

        # Had to be "creative" with what the `Aufzeichnungstyp` stands for
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6

    user_id = models.CharField(max_length=64, primary_key=True)
    device = models.CharField(
        max_length=128,
        help_text="Device used to make the glucose reading",
    )
    serial_id = models.CharField(
        max_length=64,
        help_text="Serial number of the used device",
    )
    reading_time = models.DateTimeField(help_text="Time of the reading")
    reading_type = models.IntegerField(
        choices=ReadingType.choices,
        help_text="Type of the reading",
    )

    # Not clear how `Glukosewert-Verlauf mg/dL` is different from `Glukose-Scan mg/dL`
    # It seems both values can be missing
    glucose_value = models.IntegerField(
        null=True,
        help_text="Current glucose value, mg/dL",
    )
    glucose_scan = models.IntegerField(
        null=True,
        help_text="Current glucose scan value, mg/dL",
    )

    # Did not add all other extra fields, as they appeared to be missing values and
    # the task description was focused on the glucose value
