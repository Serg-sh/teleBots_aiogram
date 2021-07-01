from sqlalchemy import sql, Sequence, Column

from l_008_multiLevelMenu.utils.db_api.database import db


class Item(db.Model):
    __tablename__ = 'items'
    query: sql.Select

    id = Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    category_code = Column(db.String(20))
    category_name = Column(db.String(50))

    subcategory_code = Column(db.String(20))
    subcategory_name = Column(db.String(50))

    name = Column(db.String(50))
    photo = Column(db.String(250))
    price = Column(db.Integer)

    def __repr__(self):
        return f'''
        Товар №{self.id} - {self.name}
        Цена: {self.price}
        '''
