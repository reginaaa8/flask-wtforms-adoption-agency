from app import db
from models import Pet

db.drop_all()
db.create_all()

sparkles = Pet(name="Sparkles", 
               species="dog", 
               photo_url="https://images.unsplash.com/photo-1534361960057-19889db9621e?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZG9nfGVufDB8fDB8fHww", 
               age=3, 
               notes="Super energetic! Loves to snuggle.")

buddy = Pet(name="Buddy", 
               species="dog", 
               photo_url="https://images.unsplash.com/photo-1503256207526-0d5d80fa2f47?q=80&w=2848&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
               age=8, 
               notes="Will play all day long. Will do just about anything for a hot dog.")

doug = Pet(name="Doug", 
               species="cat", 
               photo_url="https://plus.unsplash.com/premium_photo-1673967831980-1d377baaded2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2F0c3xlbnwwfHwwfHx8MA%3D%3D", 
               age=7, 
               notes="Loves to nap.")

bella = Pet(name="Bella", 
               species="cat", 
               photo_url="https://images.unsplash.com/photo-1472491235688-bdc81a63246e?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2F0fGVufDB8fDB8fHww", 
               age=9, 
               notes="Will nap all day if you let her.")

perry = Pet(name="Perry", 
               species="porcupine", 
               photo_url="https://images.unsplash.com/photo-1639501483504-0db53233a4d5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cG9yY3VwaW5lfGVufDB8fDB8fHww", 
               age=1, 
               notes="Food motivated - will do anything for a treat.", 
               available=False)

db.session.add(sparkles)
db.session.add(buddy)
db.session.add(doug)
db.session.add(bella)
db.session.add(perry)
db.session.commit()