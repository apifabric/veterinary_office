# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 05, 2024 16:32:19
# Database: sqlite:////tmp/tmp.5Cnji1tgZ3/veterinary_office/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Medicine(SAFRSBaseX, Base):
    """
    description: Lists medicines prescribed to animals
    """
    __tablename__ = 'medicine'
    _s_collection_name = 'Medicine'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    MedicineSupplyList : Mapped[List["MedicineSupply"]] = relationship(back_populates="medicine")
    PrescriptionList : Mapped[List["Prescription"]] = relationship(back_populates="medicine")



class Owner(SAFRSBaseX, Base):
    """
    description: Stores information about pet owners
    """
    __tablename__ = 'owner'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AnimalList : Mapped[List["Animal"]] = relationship(back_populates="owner")



class Supplier(SAFRSBaseX, Base):
    """
    description: Information about suppliers providing medicines
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_phone = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    MedicineSupplyList : Mapped[List["MedicineSupply"]] = relationship(back_populates="supplier")



class Vet(SAFRSBaseX, Base):
    """
    description: Contains information about veterinarians in the clinic
    """
    __tablename__ = 'vet'
    _s_collection_name = 'Vet'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="vet")
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="vet")



class Animal(SAFRSBaseX, Base):
    """
    description: Stores information about animals treated at the clinic
    """
    __tablename__ = 'animal'
    _s_collection_name = 'Animal'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("AnimalList"))

    # child relationships (access children)
    AllergyList : Mapped[List["Allergy"]] = relationship(back_populates="animal")
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="animal")



class MedicineSupply(SAFRSBaseX, Base):
    """
    description: Links medicines with suppliers and records quantity supplied
    """
    __tablename__ = 'medicine_supply'
    _s_collection_name = 'MedicineSupply'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    medicine_id = Column(ForeignKey('medicine.id'), nullable=False)
    supplier_id = Column(ForeignKey('supplier.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    supply_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    medicine : Mapped["Medicine"] = relationship(back_populates=("MedicineSupplyList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("MedicineSupplyList"))

    # child relationships (access children)



class Schedule(SAFRSBaseX, Base):
    """
    description: Schedules for vet availability
    """
    __tablename__ = 'schedule'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vet_id = Column(ForeignKey('vet.id'), nullable=False)
    day_of_week = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    vet : Mapped["Vet"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class Allergy(SAFRSBaseX, Base):
    """
    description: Stores known allergies of animals
    """
    __tablename__ = 'allergy'
    _s_collection_name = 'Allergy'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    animal_id = Column(ForeignKey('animal.id'), nullable=False)
    allergy_name = Column(String, nullable=False)
    severity = Column(String)

    # parent relationships (access parent)
    animal : Mapped["Animal"] = relationship(back_populates=("AllergyList"))

    # child relationships (access children)



class Appointment(SAFRSBaseX, Base):
    """
    description: Records appointments with the vet
    """
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    animal_id = Column(ForeignKey('animal.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    reason = Column(String)
    vet_id = Column(ForeignKey('vet.id'), nullable=False)

    # parent relationships (access parent)
    animal : Mapped["Animal"] = relationship(back_populates=("AppointmentList"))
    vet : Mapped["Vet"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="appointment")
    TreatmentList : Mapped[List["Treatment"]] = relationship(back_populates="appointment")



class Payment(SAFRSBaseX, Base):
    """
    description: Records payments made for treatments
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    appointment_id = Column(ForeignKey('appointment.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    appointment : Mapped["Appointment"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class Treatment(SAFRSBaseX, Base):
    """
    description: Records treatment procedures administered during appointments
    """
    __tablename__ = 'treatment'
    _s_collection_name = 'Treatment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    appointment_id = Column(ForeignKey('appointment.id'), nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float)

    # parent relationships (access parent)
    appointment : Mapped["Appointment"] = relationship(back_populates=("TreatmentList"))

    # child relationships (access children)
    PrescriptionList : Mapped[List["Prescription"]] = relationship(back_populates="treatment")



class Prescription(SAFRSBaseX, Base):
    """
    description: Links prescribed medicines to treatments
    """
    __tablename__ = 'prescription'
    _s_collection_name = 'Prescription'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    treatment_id = Column(ForeignKey('treatment.id'), nullable=False)
    medicine_id = Column(ForeignKey('medicine.id'), nullable=False)
    dosage = Column(String)

    # parent relationships (access parent)
    medicine : Mapped["Medicine"] = relationship(back_populates=("PrescriptionList"))
    treatment : Mapped["Treatment"] = relationship(back_populates=("PrescriptionList"))

    # child relationships (access children)
