from django.contrib import admin
from boards.models import Board, BoardFeature, BoardPublication, Event, Group, Interaction, Publication, PublicationType, Repetition, User

@admin.register(Board)
class AdminBoards(admin.ModelAdmin):
    list_display = ('id', 'feature', 'group', 'is_active', 'location', 'section', 'serial_number',)
    # list_filter = ('',)
    # search_fields = ('',)

@admin.register(BoardFeature)
class AdminBoardFeature(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'resolution', 'size_inches',)

@admin.register(BoardPublication)
class AdminBoardPublication(admin.ModelAdmin):
    list_display = ('id', 'board', 'publication', 'date', 'time', 'duration',)

@admin.register(Event)
class AdminPublication(admin.ModelAdmin):
    list_display = ('id', 'audio', 'graphic', 'image', 'text', 'video',)

@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Interaction)
class AdminGroup(admin.ModelAdmin):
    list_display = ('id', 'event', 'user', 'interaction_date', 'interaction_type',)

@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    list_display = ('id', 'description',)

@admin.register(PublicationType)
class AdminPublicationType(admin.ModelAdmin):
    list_display = ('id', 'event', 'publication', 'address',)

@admin.register(Repetition)
class AdminRepetition(admin.ModelAdmin):
    list_display = ('id', 'board_publication', 'is_active',)

@admin.register(User)
class AdminPublicationType(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role',)
