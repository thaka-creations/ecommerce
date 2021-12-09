from rest_framework import serializers
from users.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type':'password'}, required=True)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
        extra_kwargs = {'password': {'write_only':True, 'style':{'input_type':'password'}}}
        read_only_fields = ('email',)
         

    def save(self):
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'email':'Email already exists'})
        else:
            user = User(email = self.validated_data['email'], username = self.validated_data['username'])

            password = self.validated_data['password']
            password2 = self.validated_data['confirm_password']

            if password is not None and password != password2:
                raise serializers.ValidationError({'password':'Passwords must match'})

            user.set_password(password)  #hashing of password
            user.save()
            return user



        



    

