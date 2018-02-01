from app import db, productos

db.create_all()


test_rec = productos(
        'Ibuprofeno1',
        '600 mg tabletas',
        '5 euros',
        '12345'
        )

db.session.add(test_rec)
db.session.commit()
