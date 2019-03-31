from sqlalchemy import (
    MetaData,
    Table,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    Boolean,
    select,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.config import config

Base = declarative_base()


class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    min_value = Column(String(50), nullable=False)
    max_value = Column(String(50), nullable=False)
    format_of_value = Column(String(20), nullable=False)
    size = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)

    def __init__(self, name, min_value, max_value, format_of_value, size, description):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.size = size
        self.format_of_value = format_of_value
        self.description = description

    def __repr__(self):
        return f"<User({self.name}, {self.min_value}, {self.max_value}, {self.size}, {self.format_of_value}, {self.description})>"


class MathOperations(Base):
    __tablename__ = "math_operations"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    type_of_argument = Column(String(50), nullable=False)
    type_of_value = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)

    def __init__(self, name, type_of_argument, type_of_value, description):
        self.name = name
        self.type_of_argument = type_of_argument
        self.type_of_value = type_of_value
        self.description = description

    def __repr__(self):
        return f"<MathOperation({self.name}, {self.type_of_argument}, {self.type_of_value}, {self.description})>"


class Class(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    number_of_methods = Column(Integer, nullable=False)
    number_of_properties = Column(Integer, nullable=False)

    def __init__(self, name, number_of_methods, number_of_properties):
        self.name = name
        self.number_of_methods = number_of_methods
        self.number_of_properties = number_of_properties

    def __repr__(self):
        return f"<Class({self.name}, {self.number_of_methods}, {self.number_of_properties})>"


class DB:
    def __init__(self):
        DSN = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        db_url = DSN.format(**config["postgres"])
        engine = create_engine(db_url)
        self.Session = sessionmaker()
        self.Session.configure(bind=engine)

    def get_class_all(self):

        session = self.Session()
        match = session.query(Class).all()
        session.close()
        result = [
            {
                "name": record.name,
                "number_of_methods": record.number_of_methods,
                "number_of_properties": record.number_of_properties,
                "id": record.id,
            }
            for record in match
        ]
        return result

    def get_class(self, iid):
        """
        Parameters:
            - iid
        """
        session = self.Session()
        result = session.query(Class).filter(Class.id == iid).first()
        session.close()
        if result is None:
            None
        return {
            "name": result.name,
            "number_of_methods": result.number_of_methods,
            "number_of_properties": result.number_of_properties,
            "id": result.id,
        }

    def set_class(self, name, num_of_methods, num_of_fields):
        """
        Parameters:
            - name
            - num_of_methods
            - num_of_fields
        """
        session = self.Session()
        session.add(Class(name, num_of_methods, num_of_fields))
        session.commit()
        session.close()

    def reset_class(self, iid, name, num_of_methods, num_of_fields):
        """
        Parameters:
            - iid
            - name
            - num_of_methods
            - num_of_fields
        """
        session = self.Session()
        session.query(Class).filter(Class.id == iid).update(
            {
                Class.name: name,
                Class.number_of_methods: num_of_methods,
                Class.number_of_properties: num_of_fields,
            },
            synchronize_session="fetch",
        )
        session.commit()
        session.close()

    def delete_class(self, iid):
        """
        Parameters:
            - iid
        """
        session = self.Session()
        session.query(Class).filter(Class.id == iid).delete()
        session.commit()
        session.close()

    def get_math_operations_all(self):
        session = self.Session()
        match = session.query(MathOperations).all()
        session.close()
        result = [
            {
                "name": record.name,
                "type_of_argument": record.type_of_argument,
                "type_of_value": record.type_of_value,
                "description": record.description,
                "id": record.id,
            }
            for record in match
        ]
        return result

    def get_math_operation(self, iid):
        """
        Parameters:
            - iid
        """
        session = self.Session()
        result = session.query(MathOperations).filter(MathOperations.id == iid).first()
        session.close()
        if result is None:
            return None
        return {
            "name": result.name,
            "type_of_argument": result.type_of_argument,
            "type_of_value": result.type_of_value,
            "description": result.description,
            "id": result.id,
        }

    def set_math_operation(self, name, type_of_argument, type_of_value, description):
        """
        Parameters:
            - name
            - type_of_argument
            - type_of_value
            - description
        """
        session = self.Session()
        session.add(MathOperations(name, type_of_argument, type_of_value, description))
        session.commit()
        session.close()

    def reset_math_operation(
        self, iid, name, type_of_argument, type_of_value, description
    ):
        """
        Parameters:
            - iid
            - name
            - type_of_argument
            - type_of_value
            - description
        """
        session = self.Session()
        session.query(MathOperations).filter(MathOperations.id == iid).update(
            {
                MathOperations.name: name,
                MathOperations.type_of_argument: type_of_argument,
                MathOperations.type_of_value: type_of_value,
                MathOperations.description: description,
            },
            synchronize_session="fetch",
        )
        session.commit()
        session.close()

    def delete_math_operation(self, iid):
        """
        Parameters:
            - iid
        """
        session = self.Session()
        session.query(MathOperations).filter(MathOperations.id == iid).delete()
        session.commit()
        session.close()

    def get_type_all(self):
        session = self.Session()
        match = session.query(Type).all()
        session.close()
        result = [
            {
                "name": record.name,
                "min_value": record.min_value,
                "max_value": record.max_value,
                "format_of_value": record.format_of_value,
                "size": record.size,
                "description": record.description,
                "id": record.id,
            }
            for record in match
        ]
        return result

    def get_type(self, iid):
        """
        Parameters:
            - iid
        """
        session = self.Session()
        result = session.query(Type).filter(Type.id == iid).first()
        session.close()
        if result is None:
            return None
        return {
            "name": result.name,
            "min_value": result.min_value,
            "max_value": result.max_value,
            "format_of_value": result.format_of_value,
            "size": result.size,
            "description": result.description,
            "id": result.id,
        }

    def set_type(self, name, min_value, max_value, format_of_value, size, description):
        """
        Parameters:
            - name
            - min_value
            - max_value
            - format
            - size
            - description
        """
        session = self.Session()
        session.add(
            Type(name, min_value, max_value, format_of_value, size, description)
        )
        session.commit()
        session.close()

    def reset_type(
        self, iid, name, min_value, max_value, format_of_value, size, description
    ):
        """
        Parameters:
            - iid
            - name
            - min_value
            - max_value
            - format
            - size
            - description
        """
        session = self.Session()
        session.query(Type).filter(Type.id == iid).update(
            {
                Type.name: name,
                Type.min_value: min_value,
                Type.max_value: max_value,
                Type.format_of_value: format_of_value,
                Type.size: size,
                Type.description: description,
            },
            synchronize_session="fetch",
        )
        session.commit()
        session.close()

    def delete_type(self, iid):
        """
        Parameters:
            - iid
        """
        session = self.Session()
        session.query(Type).filter(Type.id == iid).delete()
        session.commit()
        session.close()
