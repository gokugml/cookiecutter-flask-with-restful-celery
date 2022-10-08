from {{cookiecutter.app_name}}.database import Column, PkModel, db


class Sample(PkModel):
    """Basic sample model"""

    __tablename__ = "sample"
    # id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80), nullable=False)
    email = Column(db.String(80), nullable=True)

    def __repr__(self):
        return "<name %s>" % self.name
