from server.app import db, create_app
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="karoki")
    user.password = "Karokin35!"
    db.session.add(user)

    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Smith", occupation="Comedian")
    guest3 = Guest(name="Elon Musk", occupation="Entrepreneur")

    episode1 = Episode(date="2024-06-20", number=101)
    episode2 = Episode(date="2024-06-21", number=102)
    episode3 = Episode(date="2024-06-22", number=103)

    db.session.add_all([guest1, guest2, guest3, episode1, episode2, episode3])
    db.session.commit()

    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode3.id)

    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()

