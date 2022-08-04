from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add data to tables
arlene = Pet(name="Arlene", species="dog", photo_url="https://www.hepper.com/wp-content/uploads/2021/11/rsz_shutterstock_1402786178.jpg", age="1", notes="", available=True)
dorris = Pet(name="Dorris", species="dog", photo_url="https://static.toiimg.com/thumb/msid-83277549,imgsize-538470,width-400,resizemode-4/83277549.jpg", age="2", notes="", available=True)
brenda = Pet(name="Brenda", species="cat", photo_url="https://images.hindustantimes.com/rf/image_size_630x354/HT/p2/2019/08/08/Pictures/_6bda0940-b9ad-11e9-98cb-e738ad509720.jpg", age="4", notes="", available=True)

# Add pets to db session
db.session.add(arlene)
db.session.add(dorris)
db.session.add(brenda)

# Commit session
db.session.commit()