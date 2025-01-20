from django.contrib import admin
from boards.models import Board, BoardFeature, BoardPublication, Event, Group, Repetition, User

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
    list_display = ('id', 'board', 'event', 'user', 'address', 'date', 'description', 'duration', 'interaction', 'time',)

@admin.register(Event)
class AdminPublication(admin.ModelAdmin):
    list_display = ('id', 'audio', 'graphic', 'image', 'text', 'video',)

@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Repetition)
class AdminRepetition(admin.ModelAdmin):
    list_display = ('id', 'board_publication', 'current_cycle', 'is_active', 'repetition_count',)

@admin.register(User)
class AdminPublicationType(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role',)
