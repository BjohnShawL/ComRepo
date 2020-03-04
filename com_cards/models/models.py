"""Models for the postgres database to be migrated"""
from . import POSTGRES_DB
from .abstractModels import BaseModel

class User(POSTGRES_DB.Model, BaseModel):
    """Defines the model for a user"""

    __tablename__ = 'users'

    user_id = POSTGRES_DB.Column(POSTGRES_DB.Integer, primary_key=True)
    username = POSTGRES_DB.Column(POSTGRES_DB.String)
    password = POSTGRES_DB.Column(POSTGRES_DB.String)
    email = POSTGRES_DB.Column(POSTGRES_DB.String)
    created_on = POSTGRES_DB.Column(POSTGRES_DB.DateTime)
    players = POSTGRES_DB.relationship('Player', backref='user', lazy=True)
class Player(POSTGRES_DB.Model, BaseModel):
    """Defines the model for a player.""" # Players are different from users in that players are attached to a game - a player can leave a game, while retaining their user status

    __tablename__ = 'players'

    player_id = POSTGRES_DB.Column(POSTGRES_DB.Integer, primary_key=True)
    player_name = POSTGRES_DB.Column(POSTGRES_DB.String)
    user_id = POSTGRES_DB.Column(POSTGRES_DB.Integer,POSTGRES_DB.ForeignKey('user.user_id'),nullable=False)
    characters = POSTGRES_DB.relationship('Character', backref='player', lazy=True)
    is_active = POSTGRES_DB.Column(POSTGRES_DB.Boolean)
class Character(POSTGRES_DB.Model, BaseModel):
    """Defines the model for a character.""" 
    __tablename__ = 'characters'

    character_id = POSTGRES_DB.Column(POSTGRES_DB.Integer, primary_key=True)
    character_name = POSTGRES_DB.Column(POSTGRES_DB.String)
    character_rift = POSTGRES_DB.Column(POSTGRES_DB.String)
    player_id = POSTGRES_DB.Column(POSTGRES_DB.Integer,POSTGRES_DB.ForeignKey('player.player_id'),nullable=False)
    game_id = POSTGRES_DB.Column(POSTGRES_DB.Integer,POSTGRES_DB.ForeignKey('game.game_id'),nullable=False)
    themes = POSTGRES_DB.relationship('Theme', backref='character', lazy=True)
    is_active = POSTGRES_DB.Column(POSTGRES_DB.Boolean)
class Game(POSTGRES_DB.Model, BaseModel):
    """Defines the model for a game."""
    __tablename__ = 'games'

    game_id = POSTGRES_DB.Column(POSTGRES_DB.Integer, primary_key=True)
    game_name = POSTGRES_DB.Column(POSTGRES_DB.String)
    characters = POSTGRES_DB.relationship('Character', backref='game', lazy=True)
    created_on = POSTGRES_DB.Column(POSTGRES_DB.DateTime)
    is_active = POSTGRES_DB.Column(POSTGRES_DB.Boolean)
class Theme(POSTGRES_DB.Model,BaseModel):
    """Defines the model for a theme """
    __tablename__ = 'themes'

    theme_id = POSTGRES_DB.Column(POSTGRES_DB.Integer, primary_key=True)
    theme_name = POSTGRES_DB.Column(POSTGRES_DB.String)
    theme_statement = POSTGRES_DB.Column(POSTGRES_DB.String)
    theme_type = POSTGRES_DB.Column(POSTGRES_DB.String)
    theme_attn = POSTGRES_DB.Column(POSTGRES_DB.Integer)
    theme_crack = POSTGRES_DB.Column(POSTGRES_DB.Integer)
    tags = POSTGRES_DB.relationship('Tag', backref='theme', lazy=True)
    character_id = POSTGRES_DB.Column(POSTGRES_DB.Integer,POSTGRES_DB.ForeignKey('.game_id'),nullable=False)
class Tag(POSTGRES_DB.Model, BaseModel):
    """Defines the model for a tag """
    __tablename__ = 'tags'

    tag_id = POSTGRES_DB.Column(POSTGRES_DB.Integer, primary_key=True)
    tag_name = POSTGRES_DB.Column(POSTGRES_DB.String)
    tag_type = POSTGRES_DB.Column(POSTGRES_DB.String) # leave this here now, but consider a lookup table for the three theme types, rather than holding an enum in code
    tag_is_burned = POSTGRES_DB.Column(POSTGRES_DB.Boolean)
    tag_is_invoked = POSTGRES_DB.Column(POSTGRES_DB.Boolean)
    tag_current_use = POSTGRES_DB.Column(POSTGRES_DB.Integer)
    tag_max_use = POSTGRES_DB.Column(POSTGRES_DB.Integer)
    theme_id = POSTGRES_DB.Column(POSTGRES_DB.Integer,POSTGRES_DB.ForeignKey('theme.theme_id'),nullable=True)