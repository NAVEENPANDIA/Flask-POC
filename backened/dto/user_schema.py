from marshmallow import Schema, fields, validate





class UserSchema(Schema):
    print("Schema")
    
    user_name = fields.String(required= True, validate=validate.Length(min=5))
    password = fields.String(required = True )
    
    email_address = fields.String()
    dob = fields.String()
    address = fields.String()
    uid = fields.UUID(error_messages={'null': 'Sorry, Id field cannot be null',
                      'invalid_uuid': 'Sorry, Id field must be a valid UUID'})

    print("access")


    class Meta:
        # Fields to show when sending data
        fields = ('id', 'user_name', 'password',
                  'email_address', 'dob', 'address', 'uid')
        