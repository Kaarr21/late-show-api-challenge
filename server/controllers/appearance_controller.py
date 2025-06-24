from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint("appearance_bp", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")
    rating = data.get("rating")

    if not guest_id or not episode_id or not rating:
        return jsonify({"error": "guest_id, episode_id, and rating are required"}), 400

    # Optional: Validate guest and episode exist
    if not Guest.query.get(guest_id):
        return jsonify({"error": "Invalid guest_id"}), 404
    if not Episode.query.get(episode_id):
        return jsonify({"error": "Invalid episode_id"}), 404

    try:
        appearance = Appearance(guest_id=guest_id, episode_id=episode_id, rating=rating)
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            "id": appearance.id,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "rating": appearance.rating
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
