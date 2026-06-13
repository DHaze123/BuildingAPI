@mechanic_bp.route("/<int:id>", methods=["DELETE"])
def delete_mechanic(id):

    mechanic = Mechanic.query.get_or_404(id)

    db.session.delete(mechanic)
    db.session.commit()

    return jsonify({
        "message": "Mechanic deleted"
    }), 200