from __init__ import CONN, CURSOR

class Pet:
  def __init__(self, name, species, owner_id=None, id=None):
    self.name = name
    self.species = species
    self.id = id
    self.owner_id = owner_id


  def save(self):
    if not self.id:
      sql = '''
        INSERT INTO pets (name, species) VALUES (?, ?)
      '''

      CURSOR.execute(sql, (self.name, self.species))
      CONN.commit()

      sql = '''
        SELECT * FROM pets ORDER BY id DESC limit 1
      '''

      id = CURSOR.execute(sql).fetchone()[0]
      self.id = id
    else:
      sql = '''
        UPDATE pets
        SET name = (?), species = (?), owner_id = (?)
        WHERE id = (?)
      '''
      CURSOR.execute(sql, (self.name, self.species, self.owner_id, self.id))

      CONN.commit()


  @property
  def owner(self):
    from owner import Owner
    sql = '''
      SELECT * FROM owners WHERE id = (?)
    '''

    row = CURSOR.execute(sql, (self.owner_id,)).fetchone()
    return Owner.create_from_row(row)
  
  @owner.setter
  def owner(self, owner):
    sql = '''
      UPDATE pets
      SET owner_id = (?)
      WHERE id = (?)
    '''

    CURSOR.execute(sql, (owner.id, self.id))
    CONN.commit()

    self.owner_id = owner.id

    
  def delete(self):
    sql = '''
      DELETE FROM pets
      WHERE id = (?)
    '''

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    self.id = None

  @classmethod
  def drop_table(cls):
    sql = '''
      DROP TABLE pets;
    '''

    CURSOR.execute(sql)

  @classmethod
  def create_table(cls):
    sql = '''
      CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        owner_id INTEGER
      );
    '''

    CURSOR.execute(sql)

  @classmethod
  def find_by_id(cls, id):
    sql = '''
      SELECT * FROM pets WHERE id = (?)
    '''

    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.create_from_row(row)
  
  @classmethod
  def all(cls):
    sql = '''
      SELECT * FROM pets
    '''
    rows = CURSOR.execute(sql).fetchall()
    return [Pet.create_from_row(row) for row in rows]
  
  @classmethod
  def create_from_row(cls, row):
    return Pet(id=row[0], name=row[1], species=row[2], owner_id=row[3])



  def __repr__(self):
    return f'<Pet id={self.id} name="{self.name}" species="{self.species}" owner_id={self.owner_id}>'