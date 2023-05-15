from sqlalchemy import (
    Column,
    SmallInteger,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Date,
)
from db_config.connect import Base
from sqlalchemy.orm import relationship


"""
    One to many relationship between Truck and Drivers.
    Truck can have multiple drivers but each drivers associated with only one Truck.
"""


class Trucks(Base):
    __tablename__ = "trucks"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    license_plate = Column(String(10), unique=True, index=False)
    manufactured_by = Column(String, index=False, unique=False)
    model = Column(Integer, unique=False, index=False)
    year = Column(SmallInteger, unique=False, index=False)
    capacity = Column(Integer, unique=False, index=False)
    status = Column(Boolean, unique=False, index=False)

    drivers = relationship("Drivers", back_populates="trucks")
    shipments = relationship("Shipments", back_populates="trucks")


class Drivers(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False, index=False)
    license_number = Column(String, unique=False, index=False)
    address = Column(String, unique=False, index=False)
    city = Column(String, index=False, unique=False)
    state = Column(String, index=False, unique=False)
    zipcode = Column(Integer, index=False, unique=False)
    phone_no = Column(Integer, unique=True, index=False)
    email = Column(String, unique=True, index=False)

    """
    Many to one relationship between Truck and drivers.
    Mutiple Drivers associated with only one Trucks.
    """
    truck_id = Column(Integer, ForeignKey("trucks.id"))
    trucks = relationship("Trucks", back_populates="drivers")

    """
    One to many relationship between Drivers and Shipments.
    Each Truck with Multiple Shipments and each Shipments associated with one Truck. 
    """
    shipments = relationship("Shipments", back_populates="drivers")


class Goods(Base):
    __tablename__ = "goods"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False, index=False)
    description = Column(String, unique=False, index=False)
    quantity = Column(Integer, unique=False, index=False)
    weights = Column(Integer, unique=False, index=False)
    value = Column(Integer, index=False, unique=False)

    """
    One to Many relationship between Goods and Shipment.
    Multiple Goods can be shipped at each shipments but each good can only associated with one Shipments.
    """
    shipments_id = Column(Integer, ForeignKey("shipments.id"))
    shipments = relationship("Shipments", back_populates="goods")


class Shippers(Base):
    __tablename__ = "shippers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False, index=False)
    address = Column(String, unique=False, index=False)

    """
    One to many relationship between Shippers and Shipments.
    Each Shipper associated with only multiple Shipments but each Shipments associated with only one Shipper. 
    """
    shipments = relationship("Shipments", back_populates="shippers")


class Shipments(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    shipment_Date = Column(DateTime, index=False, unique=False)
    origin = Column(String, index=False, unique=False)
    destination = Column(String, index=False, unique=False)

    """
    Many to One relationship between Truck and Shipments
    """
    truck_id = Column(Integer, ForeignKey("trucks.id"))
    trucks = relationship("Trucks", back_populates="shipments")

    """
    Many to one relationship between Drivers and Shipments
    """
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    drivers = relationship("Drivers", back_populates="shipments")
    """

    Many to one relationship between Shipper and Shipments
    """
    shipper_id = Column(Integer, ForeignKey("shippers.id"))
    shippers = relationship("Shippers", back_populates="shipments")

    """
    One to many relationship between Goods and Shipments
    """
    goods = relationship("Goods", back_populates="shipments")

    date = Column(Date, index=False, unique=False)
