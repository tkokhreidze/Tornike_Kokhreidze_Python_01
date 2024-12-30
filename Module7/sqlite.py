import sqlite3
from dataclasses import dataclass

@dataclass
class BaseRepository:
    table_name: str

    def __post_init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def create(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join('?' for _ in kwargs)
        sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, tuple(kwargs.values()))
        self.conn.commit()

    def get_all(self):
        sql = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_by_id(self, record_id):
        sql = f"SELECT * FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(sql, (record_id,))
        return self.cursor.fetchone()

    def update(self, record_id, **kwargs):
        columns = ', '.join(f"{k} = ?" for k in kwargs)
        sql = f"UPDATE {self.table_name} SET {columns} WHERE id = ?"
        self.cursor.execute(sql, (*kwargs.values(), record_id))
        self.conn.commit()

    def delete_by_id(self, record_id):
        sql = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(sql, (record_id,))
        self.conn.commit()

@dataclass
class ProductRepository(BaseRepository):
    table_name: str = 'products'

@dataclass
class CategoryRepository(BaseRepository):
    table_name: str = 'categories'

@dataclass
class CustomerRepository(BaseRepository):
    table_name: str = 'customers'

@dataclass
class AddressRepository(BaseRepository):
    table_name: str = 'addresses'

@dataclass
class CustomerAddressRepository(BaseRepository):
    table_name: str = 'customer_addresses'

@dataclass
class OrderRepository(BaseRepository):
    table_name: str = 'orders'

@dataclass
class OrderDetailRepository(BaseRepository):
    table_name: str = 'order_details'

@dataclass
class ProductModelRepository(BaseRepository):
    table_name: str = 'product_models'
