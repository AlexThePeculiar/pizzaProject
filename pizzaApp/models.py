# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


from ast import literal_eval

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cheese(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheese'


class Crust(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crust'


class Diameter(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diameter'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fish(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fish'


class Fruits(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fruits'


class Meat(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meat'


class Mushrooms(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mushrooms'


class Orders(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    clock = models.DateTimeField(blank=True, null=True)
    clockfinish = models.DateTimeField(db_column='clockFinish', blank=True, null=True)  # Field name made lowercase.
    payment = models.CharField(max_length=15, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    orderitems = models.TextField(db_column='orderItems', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Pizzas(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=40, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:

            price = 5
            pizza = literal_eval(self.ingredients)
            for topping in pizza['toppings']:
                if topping[:3] == 'TME':
                    elem = Meat.objects.get(id=topping).price
                elif topping[:3] == 'TMU':
                    elem = Mushrooms.objects.get(id=topping).price
                elif topping[:3] == 'TFR':
                    elem = Fruits.objects.get(id=topping).price
                elif topping[:3] == 'TFI':
                    elem = Fish.objects.get(id=topping).price
                elif topping[:2] == 'TV':
                    elem = Vegetables.objects.get(id=topping).price
                elif topping[:2] == 'TS':
                    elem = Sauce.objects.get(id=topping).price
                else:
                    elem = Cheese.objects.get(id=topping).price
                price += elem
            price += Diameter.objects.get(id=pizza['diameter']).price
            self.price = round(price, 2)
            self.save()
        except:
            pass

    class Meta:
        managed = False
        db_table = 'pizzas'


class Sauce(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sauce'


class Saucebase(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saucebase'


class Vegetables(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vegetables'
