from market import app,db
from market import app
from market import db
from market.models import Item

""" item9=Item(name="Playstation 5",price=105000, description="Sony Computer Entertainment PS5 Playstation 5 Console Standard Disc Version 825GB")
app.app_context().push()
db.session.add(item9)
db.session.commit()
 """
""" app.app_context().push()
item=Item.query.get(1)
item.price=239999
db.session.commit() """

#Checks if the run.py file has executed directly and not imported

if __name__ == '__main__':
    app.run(debug=True)