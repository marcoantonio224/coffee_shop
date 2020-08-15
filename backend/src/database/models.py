import os
import json
import re
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Drink
a persistent drink entity, extends the base SQLAlchemy Model
'''
class Drink(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    title = Column(String(80), unique=True)
    # the ingredients blob - this stores a lazy json blob
    # the required datatype is [{'color': string, 'name':string, 'parts':number}]
    recipe =  Column(String(180), nullable=False)

    @validates('title')
    def validate_title(self, key, value):
        # Create a regular expression for special characters
        specialChars = re.compile('[@_!#$%^&*()<>/\|}{~:]')

        # Check to see if values are empty first
        if value == '':
            print('EMPTY TITLE')
            raise AssertionError('Cannot contain empty fields')
        # Check for special characters
        elif specialChars.search(value) is not None:
            print('SPECIAL CHAR TITLE')
            raise AssertionError('Cannot contain special characters')

        # If no errors arise, then proceed.
        return value


    @validates('recipe')
    def validate_recipe(self, recipe, value):
        # Create a regular expression for special characters
        specialChars = re.compile('[@_!#$%^&*()<>/\|}{~:]')

        # Parse the json object to check the values of the recipes
        if recipe == 'recipe':
            # Parse the json object
            for obj in json.loads(value):
                # Iterate the object's keys
                for key in obj:
                    # Check to see if key is empty
                    if obj[key] == '':
                        print('EMPTY RECIPE')
                        raise AssertionError('Cannot contain empty fields')
                    # Check to see if the value of key has special chars
                    elif specialChars.search(obj[key]) is not None:
                        print("SPECIAL CHAR RECEPIE")
                        raise AssertionError('Cannot contain special characters')

                    # Return the value
                    return value

    '''
    short()
        short form representation of the Drink model
    '''
    def short(self):
        short_recipe = [{'color': r['color'], 'parts': r['parts']} for r in json.loads(self.recipe)]
        return {
            'id': self.id,
            'title': self.title,
            'recipe': short_recipe
        }

    '''
    long()
        long form representation of the Drink model
    '''
    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': json.loads(self.recipe)
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=json.dumps(recipe))
            drink.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())