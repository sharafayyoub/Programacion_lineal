from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de SQLAlchemy
Base = declarative_base()
engine = create_engine("sqlite:///army_solutions.db")
Session = sessionmaker(bind=engine)

# Modelo de la tabla
class Solution(Base):
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    swordsmen = Column(Integer, nullable=False)
    bowmen = Column(Integer, nullable=False)
    horsemen = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)

# Crear la tabla si no existe
Base.metadata.create_all(engine)

# Función para guardar los datos
def save_solution(swordsmen, bowmen, horsemen, power):
    session = Session()
    solution = Solution(swordsmen=swordsmen, bowmen=bowmen, horsemen=horsemen, power=power)
    session.add(solution)
    session.commit()
    session.close()
