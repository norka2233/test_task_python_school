from datetime import datetime
from flask import request, jsonify
from app import app, db
from app.models import Driver, Vehicle
from app.helpers import generate_plate


@app.route('/drivers/driver/', methods=['GET'])
def driver_list():
    q = Driver.query
    if request.args.get('created_at__gte'):
        min_bound = datetime.strptime(request.args.get('created_at__gte'), "%d-%m-%Y")
        q = q.filter(Driver.registered_at > min_bound)
    if request.args.get('created_at__lte'):
        max_bound = datetime.strptime(request.args.get('created_at__lte'), "%d-%m-%Y")
        q = q.filter(Driver.registered_at < max_bound)
    struct = [{
        'id': d.id,
        'firstname': d.firstname,
        'lastname': d.lastname,
        'registered_at': d.registered_at.strftime("%d/%m/%Y %H:%M:%S"),
        'updated_at': d.updated_at.strftime("%d/%m/%Y %H:%M:%S")
    } for d in q.all()]

    return jsonify(struct)


@app.route('/drivers/driver/', methods=['POST'])
def create_driver():
    first_name = request.args.get('firstname')
    last_name = request.args.get('lastname')
    registered_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    driver = Driver(firstname=first_name, lastname=last_name, registered_at=registered_at, updated_at=updated_at)
    db.session.add(driver)
    db.session.commit()

    return str(driver), 201


@app.route('/drivers/driver/<driver_id>/', methods=['PATCH'])
def edit_driver(driver_id):
    driver = Driver.query.filter_by(id=driver_id).first()
    driver.firstname = request.args.get('firstname', driver.firstname)
    driver.lastname = request.args.get('lastname', driver.lastname)
    driver.updated_at = datetime.utcnow()
    db.session.commit()

    return jsonify(f"Driver #{driver.id} was updated.")


@app.route('/drivers/driver/<driver_id>/', methods=['DELETE'])
def delete_driver(driver_id):
    driver = Driver.query.filter_by(id=driver_id).first()
    db.session.delete(driver)
    db.session.commit()

    return jsonify(f"Driver #{driver_id} was deleted.")


@app.route('/vehicles/vehicle/', methods=['GET'])
def vehicle_list():
    q = Vehicle.query
    if request.args.get('with_driver').lower() == 'yes':
        q = q.filter(Vehicle.driver_id != None)
    if request.args.get('with_driver').lower() == 'no':
        q = q.filter(Vehicle.driver_id == None)

    struct = [{
        'id': d.id,
        'driver_id': d.driver_id,
        'make': d.make,
        'model': d.model,
        'plate_number': d.plate_number,
        'registered_at': d.registered_at, #.strftime("%d/%m/%Y %H:%M:%S"),
        'updated_at': d.updated_at#.strftime("%d/%m/%Y %H:%M:%S"),

    } for d in q.all()]

    return jsonify(struct)


@app.route('/vehicles/vehicle/<vehicle_id>', methods=['GET'])
def driver(vehicle_id):

    return Vehicle.query.filter_by(id=vehicle_id).first_or_404()


@app.route('/vehicles/vehicle/', methods=['POST'])
def create_vehicle():
    # driver_id = request.args.get('driver_id')
    make = request.args.get('make')
    model = request.args.get('model')
    plate_number = request.args.get('plate_number') or generate_plate()
    registered_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    vehicle = Vehicle(make=make, model=model, plate_number=plate_number, registered_at=registered_at, updated_at=updated_at)
    db.session.add(vehicle)
    db.session.commit()

    return str(vehicle), 201


@app.route('/vehicles/vehicle/<vehicle_id>/', methods=['PATCH'])
def edit_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    vehicle.make = request.args.get('make', vehicle.make)
    vehicle.model = request.args.get('model', vehicle.model)
    vehicle.updated_at = datetime.utcnow()
    vehicle.driver_id = request.args.get('driver_id')
    db.session.commit()

    return jsonify(f"Vehicle #{vehicle.id} was updated")


@app.route('/vehicles/vehicle/<vehicle_id>/', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    db.session.delete(vehicle)
    db.session.commit()

    return jsonify(f"Vehicle #{vehicle_id} was deleted.")


