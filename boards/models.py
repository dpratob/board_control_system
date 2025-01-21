from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Board(models.Model):
    feature = models.ForeignKey('BoardFeature', on_delete=models.CASCADE, related_name='boards_with_feature')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='boards_in_group')
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=10)
    section = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], default=1)
    serial_number = models.CharField(max_length=8, unique=True)
    
    class Meta:
        verbose_name = 'Board Master'
        verbose_name_plural = 'Boards Master'
        db_table = 'board'

    def __str__(self):
        return f"Board {self.id} ({self.location})"


class BoardFeature(models.Model):
    brand = models.CharField(max_length=6)
    model = models.CharField(max_length=10)
    resolution = models.CharField(max_length=9, help_text="e.g., ____x___")
    size_inches = models.DecimalField(validators=[MinValueValidator(5)], max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = "Board Feature"
        verbose_name_plural = "Board Features"
        db_table = "board_feature"
    
    def __str__(self):
        return f"{self.brand} ({self.model})"


class BoardPublication(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='publications_in_board')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='publications_with_event')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='publications_by_user')
    address = models.FileField(upload_to='publication_files/')
    start_date = models.DateField(help_text="e.g., yyyy-mm-dd")
    end_date = models.DateField(help_text="e.g., yyyy-mm-dd")
    description = models.CharField(max_length=27)
    duration = models.PositiveIntegerField(help_text="e.g., ___ min")
    interaction = models.URLField(max_length=18, help_text="e.g., http://example.com")
    time = models.TimeField(help_text="e.g., HH:mm:ss")
    
    class Role(models.IntegerChoices):
        DAILY_INFINITE = 0, 'Daily infinite'
        SCHEDULED = 1, 'Scheduled with repetitions'
        PERPETUAL = 2, 'Perpetual (user-controlled stop)'

    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.DAILY_INFINITE)

    class Meta:
        verbose_name = "Board Publication"
        verbose_name_plural = "Board Publications"
        db_table = "board_publication"

    def __str__(self):
        return f"Publication {self.id} on {self.board.group} at {self.date} {self.time}"


class Event(models.Model):
    audio = models.FileField(upload_to='events/audios/', blank=True)
    graphic = models.ImageField(upload_to='events/graphics/', blank=True)
    image = models.ImageField(upload_to='events/images/', blank=True)
    text = models.TextField(blank=True)
    video = models.FileField(upload_to='events/videos/', blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        db_table = "event"

    def __str__(self):
        return f"{self.id}"


class Group(models.Model):
    name = models.CharField(max_length=12, unique=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        db_table = "group"

    def __str__(self):
        return f"{self.name}"


class Repetition(models.Model):
    board_publication = models.ForeignKey(BoardPublication, on_delete=models.CASCADE, related_name='repetitions_for_publication')
    current_cycle = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    repetition_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Repetition"
        verbose_name_plural = "Repetitions"
        db_table = "repetition"

    def increment_cycle(self):
        if self.board_publication.role == BoardPublication.Role.SCHEDULED and self.is_active:
            self.current_cycle += 1
            if self.repetition_count > 0 and self.current_cycle >= self.repetition_count:
                self.is_active = False
            self.save()

    def __str__(self):
        return f"Repetition for {self.board_publication} (Active: {self.is_active})"


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=7)
    last_name = models.CharField(max_length=8)
    
    class Role(models.IntegerChoices):
        USER = 0, 'User'
        ADMIN = 1, 'Admin'

    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.USER)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
