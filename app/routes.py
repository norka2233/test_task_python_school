from flask import request, jsonify
from app import app, db
from app.models import Driver #, Vehicle
from datetime import datetime


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
    return "Vehicle List"


@app.route('/vehicles/vehicle/', methods=['POST'])
def vehicle_create():
    return "Vehicle Created"


@app.route('/vehicles/vehicle/?with_drivers=yes/', methods=['GET'])
def vehicle_driver_list():
    return "Vehicle with Drivers"


@app.route('/vehicles/vehicle/?with_drivers=no/', methods=['GET'])
def vehicle_without_driver_list():
    return "Vehicle without Drivers"


@app.route('/vehicles/vehicle/?<vehicle_id>/', methods=['UPDATE'])
def vehicle_edit():
    return "Vehicle was Edited"


@app.route('/vehicles/vehicle/?<vehicle_id>/', methods=['DELETE'])
def vehicle_delete():
    return "Vehicle was Deleted"




