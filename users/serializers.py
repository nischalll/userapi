from .models import User
from rest_framework import serializers



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only = True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'password','password2','email','userid','mobileno']
        
    def save(self):
        user = User(
          email = self.validated_data['email'],
          username =  self.validated_data['username'],
          first_name = self.validated_data['first_name'],
          last_name = self.validated_data['last_name'],
          userid = self.validated_data['userid'],
          mobileno = self.validated_data['mobileno'],
          
        )
        password =  self.validated_data['password'],
        password2 =  self.validated_data['password2'],
        
        if password!=password2:
            raise serializers.ValidationError({'password' : 'Passwords must match.'})
        user.set_password(self.validated_data['password'])
        user.save()
        return user
    
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','userid','mobileno']