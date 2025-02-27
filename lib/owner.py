from __init__ import CURSOR, CONN

class Owner:
  def __init__(self, name, id=None):
    self.name = name
    self.id = id

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if (type(name) == str and len(name) > 0):
      self._name = name
    else:
      raise Exception("Must have a name and name should be a string")

  def save(self):
    if not self.id:
      sql = '''
        INSERT INTO owners (name) VALUES (?)
      '''

      CURSOR.execute(sql, (self.name,))
      CONN.commit()

      sql = '''
        SELECT * FROM owners ORDER BY id DESC limit 1
      '''

      id = CURSOR.execute(sql).fetchone()[0]
      self.id = id
    else:
      sql = '''
        UPDATE owners
        SET name = (?)
        WHERE id = (?)
      '''
      CURSOR.execute(sql, (self.name, self.id))

      CONN.commit()

  @property
  def pets(self):
    from pet import Pet
    sql = '''
      SELECT * FROM pets WHERE owner_id = (?)
    '''

    rows = CURSOR.execute(sql, (self.id,)).fetchall()
    return [Pet.create_from_row(row) for row in rows]

    
  def delete(self):
    for pet in self.pets:
      pet.delete()

    sql = '''
      DELETE FROM owners
      WHERE id = (?)
    '''

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    self.id = None

  @classmethod
  def drop_table(cls):
    sql = '''
      DROP TABLE owners;
    '''

    CURSOR.execute(sql)

  @classmethod
  def create_table(cls):
    sql = '''
      CREATE TABLE IF NOT EXISTS owners (
        id INTEGER PRIMARY KEY,
        name TEXT
      );
    '''

    CURSOR.execute(sql)

  @classmethod
  def find_by_id(cls, id):
    sql = '''
      SELECT * FROM owners WHERE id = (?)
    '''

    row = CURSOR.execute(sql, (id,)).fetchone()
    if row:
      return cls.create_from_row(row)
    else:
      return None
  
  @classmethod
  def all(cls):
    sql = '''
      SELECT * FROM owners
    '''
    rows = CURSOR.execute(sql).fetchall()
    return [Owner.create_from_row(row) for row in rows]
  
  @classmethod
  def create_from_row(cls, row):
    return Owner(id=row[0], name=row[1])

  @classmethod
  def create(cls, name):
    owner = cls(name=name)
    owner.save()
    return owner

  def __repr__(self):
    return f'<Owner id={self.id} name="{self.name}">'