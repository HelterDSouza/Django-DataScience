import uuid


def generate_transaction_id_code():
    code = str(uuid.uuid4()).replace("-", ""[:12])
    return code.upper()
