def entry_point(event, context):
    name = event['name']
    return {'hello': name}
