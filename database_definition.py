from pymodm import MongoModel, fields


class Patient(MongoModel):
    name = fields.CharField()
    id = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    test_name = fields.ListField()
    test_result = fields.ListField()

