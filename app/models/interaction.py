from sqlalchemy import Column, Integer, String, DateTime, Index
from datetime import datetime
from app.core.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False, index=True)
    query = Column(String(512), nullable=False)
    query_type = Column(String(50), nullable=False)
    response = Column(String(1024), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (Index("idx_customer_query", "customer_id", "query"),)

    def as_dict(self):
        return {
            column.name: (
                getattr(self, column.name).isoformat() 
                if isinstance(getattr(self, column.name), datetime) 
                else getattr(self, column.name)
            )
            for column in self.__table__.columns
        }
