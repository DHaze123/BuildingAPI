@mechanic_bp.route("/", methods=["GET"])
def get_mechanics():

    mechanics = Mechanic.query.all()

    return mechanics_schema.jsonify(mechanics), 200