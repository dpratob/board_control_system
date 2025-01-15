from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Board(models.Model):
    feature = models.ForeignKey('BoardFeature', on_delete=models.CASCADE, related_name='boards_with_feature', default='')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='boards_in_group', default='')
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=10)
    section = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], default=1)
    
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
    serial_number = models.CharField(max_length=8, unique=True)
    size_inches = models.DecimalField(validators=[MinValueValidator(5)], max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = "Board Feature"
        verbose_name_plural = "Board Features"
        db_table = "board_feature"
    
    def __str__(self):
        return f"{self.brand} ({self.model})"


class BoardPublication(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board_publications')
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE, related_name='publication_on_boards', default='')
    date = models.DateField(help_text="e.g., yyyy-mm-dd")
    time = models.TimeField(help_text="e.g., HH:mm:ss")
    duration = models.PositiveIntegerField(help_text="e.g., ___ min")

    class Meta:
        verbose_name = "Board Publication"
        verbose_name_plural = "Board Publications"
        db_table = "board_publication"

    def __str__(self):
        return f"Publication {self.publication.id} on {self.board.group} at {self.date} {self.time}"


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


class Interaction(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_interactions')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_interactions')
    interaction_date = models.DateTimeField(help_text="e.g., yyyy-mm-dd, HH:mm:ss")
    interaction_type = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Interaction"
        verbose_name_plural = "Interactions"
        db_table = "interaction"

    def __str__(self):
        return f"Interaction by {self.user} on {self.event} ({self.interaction_type}) at {self.interaction_date}"


class Publication(models.Model):
    description = models.CharField(max_length=27)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        db_table = "publication"

    def __str__(self):
        return f"{self.description}"


class PublicationType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_publication_types')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='publication_types')
    address = models.FileField(upload_to='publication_files/')
    
    class Meta:
        verbose_name = "Publication Type"
        verbose_name_plural = "Publication Types"
        db_table = "publication_type"

    def __str__(self):
        return f"Type for {self.publication}"


class Repetition(models.Model):
    board_publication = models.ForeignKey(BoardPublication, on_delete=models.CASCADE, related_name='publication_repetitions')
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Repetition"
        verbose_name_plural = "Repetitions"
        db_table = "repetition"

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