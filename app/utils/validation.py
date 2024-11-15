def validate_event_data(data):
    required_fields = ['name', 'start_time', 'type']
    missing_fields = [field for field in required_fields if field not in data]
    return missing_fields
