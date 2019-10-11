

def build_update_expression(data):
    """Builds a string thats a dynamo friendly
    expression"""
    keys = [f'{key} = :{key}' for key, value in data.items()]
    key_expression = ', '.join(keys)
    return f'SET {key_expression}'

def build_expression_attribute_values(data):
    """Builds an object that contains ':'
    prepended to the key to make a dynamo
    friendly ExpressionAttributeValues"""
    res = {}
    for key, value in data.items():
        res[f':{key}'] = value
    return res

def build_key(id):
    """Used to build the proper Key object
    for dynamo"""
    key = { 'id': id }
    if isinstance(id, dict):
        key = id
    return key

def build_condition_expression(id):
    attribute_name = 'id' # default
    attribute_value = id # default
    if isinstance(id, dict):
        keys = list(id.keys())
        attribute_name = keys[0]
        attribute_value = id[keys[0]]
    return {
        "name": attribute_name,
        "value": attribute_value
    }
