from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import get_database

db = get_database()
    
class GraphType(db.Model):
    __tablename__ = "graph_types"
    name: Mapped[str] = mapped_column(primary_key=True)
    reports: Mapped[list["Report"]] = relationship(
        'Report', 
        back_populates='graph_type',
        cascade= 'all, delete'
    )
    
    def __repr__(self):
        return f'GraphType: {self.name}'
    
class Criterion(db.Model):
    __tablename__ = "criteria"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    reports: Mapped[list["Report"]] = relationship(
        'Report', 
        back_populates='criterion',
        cascade= 'all, delete'
    )
    
    def __repr__(self):
        return f'Criterion: {self.name}'
    
class Report(db.Model):
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column(primary_key=True)
    correct: Mapped[bool]
    level: Mapped[str]
    graph_type_name: Mapped[str] = mapped_column(
        String,
        ForeignKey("graph_types.name")
    )
    criterion_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("criteria.id")
    )
    graph_type: Mapped["GraphType"] = relationship(
        "GraphType",
        back_populates="reports"
    )
    criterion: Mapped["Criterion"] = relationship(
        "Criterion",
        back_populates="reports"
    )
    
    def __repr__(self):
        return f'Report correct: {self.correct} id: {self.id}'