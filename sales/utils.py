import uuid

from customers.models import Customer
from profiles.models import Profile


def generate_transaction_id_code():
    code = str(uuid.uuid4()).replace("-", ""[:12])
    return code.upper()


def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username


def get_customer_from_id(val):

    customer = Customer.objects.get(id=val)
    return customer
