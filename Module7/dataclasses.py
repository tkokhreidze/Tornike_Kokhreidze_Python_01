from dataclasses import dataclass
import csv
import json
import pickle
from typing import List, Type, TypeVar

T = TypeVar('T', bound='BaseModel')

@dataclass
class BaseModel:
    @classmethod
    def saveCsv(cls: Type[T], items: List[T], filename: str) -> None:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[field.name for field in cls.__dataclass_fields__.values()])
            writer.writeheader()
            for item in items:
                writer.writerow(item.__dict__)

    @classmethod
    def loadCsv(cls: Type[T], filename: str) -> List[T]:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return [cls(**row) for row in reader]

    @classmethod
    def saveJson(cls: Type[T], items: List[T], filename: str) -> None:
        with open(filename, mode='w') as file:
            json.dump([item.__dict__ for item in items], file)

    @classmethod
    def loadJson(cls: Type[T], filename: str) -> List[T]:
        with open(filename, mode='r') as file:
            data = json.load(file)
            return [cls(**item) for item in data]

    @classmethod
    def savePickle(cls: Type[T], items: List[T], filename: str) -> None:
        with open(filename, mode='wb') as file:
            pickle.dump(items, file)

    @classmethod
    def loadPickle(cls: Type[T], filename: str) -> List[T]:
        with open(filename, mode='rb') as file:
            return pickle.load(file)


@dataclass
class Address(BaseModel):
    address_id: int
    address_line1: str
    address_line2: str
    city: str
    state_province: str
    postal_code: str
    modified_date: str
    country_region: str

@dataclass
class Category(BaseModel):
    category_id: int
    parent_category_id: int
    name: str
    modified_date: str

@dataclass
class Customer(BaseModel):
    customer_id: int
    name_style: int
    title: str
    first_name: str
    middle_name: str
    last_name: str
    suffix: str
    company_name: str
    sales_person: str
    email_address: str
    phone: str
    modified_date: str

@dataclass
class CustomerAddress(BaseModel):
    customer_id: int
    address_id: int
    address_type: str
    modified_date: str

@dataclass
class Order(BaseModel):
    order_number: int
    order_id: int
    revision_number: int
    order_date: str
    ship_date: str
    status: str
    online_order_flag: int
    purchase_order_number: str
    account_number: str
    customer_id: int
    ship_address_id: int
    bill_to_address_id: int
    ship_method: str
    credit_card_approval_code: str
    sub_total: float
    tax_amt: float
    freight: float
    total_due: float
    comment: str
    modified_date: str

@dataclass
class OrderDetail(BaseModel):
    order_id: int
    order_detail_id: int
    order_qty: int
    product_id: int
    unit_price: float
    unit_price_discount: float
    line_total: float
    modified_date: str

@dataclass
class Product(BaseModel):
    product_id: int
    name: str
    color: str
    standart_cost: float
    list_price: float
    size: str
    weight: float
    product_category_id: int
    prdocut_model_id: int
    sell_start_date: str
    sell_end_date: str
    discontinued_date: str
    modified_date: str

@dataclass
class ProductModel(BaseModel):
    name: str
    category_description: str
    modified_date: str
