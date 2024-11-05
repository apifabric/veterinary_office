# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, DateTime, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Owner(Base):
    """description: Stores information about pet owners"""
    __tablename__ = 'owner'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)

class Animal(Base):
    """description: Stores information about animals treated at the clinic"""
    __tablename__ = 'animal'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)

class Appointment(Base):
    """description: Records appointments with the vet"""
    __tablename__ = 'appointment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animal.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    reason = Column(String, nullable=True)
    vet_id = Column(Integer, ForeignKey('vet.id'), nullable=False)

class Vet(Base):
    """description: Contains information about veterinarians in the clinic"""
    __tablename__ = 'vet'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=True)

class Treatment(Base):
    """description: Records treatment procedures administered during appointments"""
    __tablename__ = 'treatment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id'), nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=True)

class Medicine(Base):
    """description: Lists medicines prescribed to animals"""
    __tablename__ = 'medicine'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)

class Prescription(Base):
    """description: Links prescribed medicines to treatments"""
    __tablename__ = 'prescription'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    treatment_id = Column(Integer, ForeignKey('treatment.id'), nullable=False)
    medicine_id = Column(Integer, ForeignKey('medicine.id'), nullable=False)
    dosage = Column(String, nullable=True)

class Supplier(Base):
    """description: Information about suppliers providing medicines"""
    __tablename__ = 'supplier'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

class MedicineSupply(Base):
    """description: Links medicines with suppliers and records quantity supplied"""
    __tablename__ = 'medicine_supply'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    medicine_id = Column(Integer, ForeignKey('medicine.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    supply_date = Column(DateTime, nullable=False)

class Schedule(Base):
    """description: Schedules for vet availability"""
    __tablename__ = 'schedule'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    vet_id = Column(Integer, ForeignKey('vet.id'), nullable=False)
    day_of_week = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

class Payment(Base):
    """description: Records payments made for treatments"""
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)

class Allergy(Base):
    """description: Stores known allergies of animals"""
    __tablename__ = 'allergy'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animal.id'), nullable=False)
    allergy_name = Column(String, nullable=False)
    severity = String = Column(String, nullable=True)


# Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
owner1 = Owner(name='John Doe', phone_number='123-456-7890', email='johndoe@example.com', address='123 Elm St')
owner2 = Owner(name='Jane Smith', phone_number='987-654-3210', email='janesmith@example.com', address='456 Oak Rd')

animal1 = Animal(name='Fido', species='Dog', breed='Labrador', age=5, owner_id=1)
animal2 = Animal(name='Whiskers', species='Cat', breed='Siamese', age=3, owner_id=2)

vet1 = Vet(name='Dr. Emily Clark', specialization='General Practice')
vet2 = Vet(name='Dr. Sarah Brown', specialization='Surgery')

appointment1 = Appointment(animal_id=1, date_time=datetime.datetime.now(), reason='Vaccination', vet_id=1)
appointment2 = Appointment(animal_id=2, date_time=datetime.datetime.now() + datetime.timedelta(days=1), reason='Checkup', vet_id=2)

treatment1 = Treatment(appointment_id=1, description='Rabies Vaccine', cost=50.0)
treatment2 = Treatment(appointment_id=2, description='Health Check', cost=75.0)

medicine1 = Medicine(name='Antibiotics', description='General antibiotics', price=20.0)
medicine2 = Medicine(name='Pain Reliever', description='To relieve pain', price=15.0)

prescription1 = Prescription(treatment_id=1, medicine_id=1, dosage='1 pill daily for 5 days')
prescription2 = Prescription(treatment_id=2, medicine_id=2, dosage='2 pills after meal')

supplier1 = Supplier(name='Vet Supplies Ltd.', contact_phone='111-222-3333', email='contact@vetsupplies.com')

medicine_supply1 = MedicineSupply(medicine_id=1, supplier_id=1, quantity=100, supply_date=datetime.datetime.now())
medicine_supply2 = MedicineSupply(medicine_id=2, supplier_id=1, quantity=200, supply_date=datetime.datetime.now())

schedule1 = Schedule(vet_id=1, day_of_week='Monday', start_time=datetime.datetime.combine(datetime.date.today(), datetime.time(9, 0)), end_time=datetime.datetime.combine(datetime.date.today(), datetime.time(17, 0)))
schedule2 = Schedule(vet_id=2, day_of_week='Tuesday', start_time=datetime.datetime.combine(datetime.date.today(), datetime.time(10, 0)), end_time=datetime.datetime.combine(datetime.date.today(), datetime.time(18, 0)))

payment1 = Payment(appointment_id=1, amount=50.0, payment_date=datetime.datetime.now())
payment2 = Payment(appointment_id=2, amount=75.0, payment_date=datetime.datetime.now())

allergy1 = Allergy(animal_id=1, allergy_name='Peanut Allergy', severity='Mild')
allergy2 = Allergy(animal_id=2, allergy_name='Pollen Allergy', severity='Severe')

# Add instances to the session
entities = [owner1, owner2, animal1, animal2, vet1, vet2,
            appointment1, appointment2, treatment1, treatment2,
            medicine1, medicine2, prescription1, prescription2,
            supplier1, medicine_supply1, medicine_supply2, schedule1,
            schedule2, payment1, payment2, allergy1, allergy2]

session.add_all(entities)
session.commit()
