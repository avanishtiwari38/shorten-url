from .base_model import *
from .serialiser import BaseSchema


class Url(Base):
    __tablename__ = "url"
    token_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), nullable=False, unique=True)
    url = db.Column(db.String(100), nullable=False)
    expire_date = db.Column(db.TIMESTAMP)
    deleted = db.Column(db.Boolean, default=False)


class UrlSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Url
        transient = True