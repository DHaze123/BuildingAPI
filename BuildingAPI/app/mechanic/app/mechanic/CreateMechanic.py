@mechanic_bp.route("/", methods=["POST"])
def create_mechanic():

    mechanic = mechanic_schema.load(request.json)

    db.session.add(mechanic)
    db.session.commit()

    return mechanic_schema.jsonify(mechanic), 201