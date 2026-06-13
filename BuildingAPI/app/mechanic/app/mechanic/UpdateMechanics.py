@mechanic_bp.route("/<int:id>", methods=["PUT"])
def update_mechanic(id):

    mechanic = Mechanic.query.get_or_404(id)

    mechanic.name = request.json.get("name", mechanic.name)
    mechanic.email = request.json.get("email", mechanic.email)

    db.session.commit()

    return mechanic_schema.jsonify(mechanic), 200