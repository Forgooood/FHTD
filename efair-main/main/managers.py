from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, iin, first_name, last_name, email, country, city, street, home_number, phone, password, **additional_fields):
        if not iin:
            raise ValueError('Введите индивидуальный идентификационный номер пользователя')
        user = self.model(
            iin=iin,
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            city=city,
            street=street,
            home_number=home_number,
            phone=phone,
            **additional_fields
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **additional_fields):
        additional_fields.setdefault('is_staff', True)
        additional_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **additional_fields)