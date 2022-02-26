# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from apps.authentication.models import User
# from django.contrib.auth.models import Group,Permission
# from django.contrib.contenttypes.models import ContentType
# from apps.address.models import Country,Currency,City,State,UserCountry
# from apps.customers.models import ( Customer,CustomerCall,CustomerAgent,
#     CustomerPayment,CustomerTeam,CustomerPackage,CustomerPackageService,
#     CustomerCallParticipant,CustomerAgentShift,CustomerAgentShiftsAttendant)
# from apps.packages.models import (Package,PackageBillingType,PackageService)
# from apps.services.models import Service
# from apps.teams.models import Team
# from apps.telecoms.models import (TelecomNumber,TelecomOperator)
#
#
# # this signal is fired automatically after adding new user
# # it checks the user's type and add it to its group
# #
# # ("customer", "Customer"),
# # ("customer_administrator", "Administrator Customer"),
# # ("agent", "Agent"),
# # ("team_leader", "Team Leader"),
# # ("administrator", "Administrator"),
# # ("special_administrator", "Special Administrator"),
# # ("monitor", "Monitor"),
# ouloug_admin = {
#     'name' : "ouloug_admin",
#     'permissions': {
#
#
#     }
#
# }
# new_group, created = Group.objects.get_or_create(name='ouloug_admin')
# # Code to add permission to group ???
# country_content_type = ContentType.objects.get_for_model(Country)
# city_content_type = ContentType.objects.get_for_model(City)
# state_content_type = ContentType.objects.get_for_model(State)
# user_country_content_type = ContentType.objects.get_for_model(UserCountry)
# currency_content_type = ContentType.objects.get_for_model(Currency)
# customer_content_type = ContentType.objects.get_for_model(Customer)
# customer_call_content_type = ContentType.objects.get_for_model(CustomerCall)
# customer_agent_content_type = ContentType.objects.get_for_model(CustomerAgent)
# customer_payment_content_type = ContentType.objects.get_for_model(CustomerPayment)
# customer_team_content_type = ContentType.objects.get_for_model(CustomerTeam)
# customer_package_content_type = ContentType.objects.get_for_model(CustomerPackage)
# customer_package_service_content_type = ContentType.objects.get_for_model(CustomerPackageService)
# customer_call_participant_content_type = ContentType.objects.get_for_model(CustomerCallParticipant)
# customer_agent_shift_content_type = ContentType.objects.get_for_model(CustomerAgentShift)
# customer_agent_shift_attendants_content_type = ContentType.objects.get_for_model(CustomerAgentShiftsAttendant)
# package_content_type = ContentType.objects.get_for_model(Package)
# package_service_content_type = ContentType.objects.get_for_model(PackageService)
# package_billing_type_content_type = ContentType.objects.get_for_model(PackageBillingType)
# service_content_type = ContentType.objects.get_for_model(Service)
# team_content_type = ContentType.objects.get_for_model(Team)
# telecom_number_content_type = ContentType.objects.get_for_model(TelecomNumber)
# telecom_operator_content_type = ContentType.objects.get_for_model(TelecomOperator)
# """
# Address Permissions
# """
# # city permissions
# add_city_permission = Permission.objects.get_or_create(codename='add_city',
#                                    name='Can add city',
#                                    content_type=city_content_type)
# change_city_permission = Permission.objects.get_or_create(codename='change_city',
#                                    name='Can change city',
#                                    content_type=city_content_type)
# delete_city_permission = Permission.objects.get_or_create(codename='delete_city',
#                                    name='Can delete city',
#                                    content_type=city_content_type)
# view_city_permission = Permission.objects.get_or_create(codename='view_city',
#                                    name='Can view city',
#                                    content_type=city_content_type)
# # *****************
# # country permissions
# add_country_permission = Permission.objects.get_or_create(codename='add_country',
#                                    name='Can add country',
#                                    content_type=country_content_type)
# change_country_permission = Permission.objects.get_or_create(codename='change_country',
#                                    name='Can change country',
#                                    content_type=country_content_type)
# delete_country_permission = Permission.objects.get_or_create(codename='delete_country',
#                                    name='Can delete country',
#                                    content_type=country_content_type)
# view_country_permission = Permission.objects.get_or_create(codename='view_country',
#                                    name='Can view country',
#                                    content_type=country_content_type)
# # *****************
# # state permissions
# add_state_permission = Permission.objects.get_or_create(codename='add_state',
#                                    name='Can add state',
#                                    content_type=state_content_type)
# change_state_permission = Permission.objects.get_or_create(codename='change_state',
#                                    name='Can change state',
#                                    content_type=state_content_type)
# delete_state_permission = Permission.objects.get_or_create(codename='delete_state',
#                                    name='Can delete state',
#                                    content_type=state_content_type)
# view_state_permission = Permission.objects.get_or_create(codename='view_state',
#                                    name='Can view state',
#                                    content_type=state_content_type)
# # *****************
# # currency permissions
# add_currency_permission = Permission.objects.get_or_create(codename='add_currency',
#                                    name='Can add currency',
#                                    content_type=currency_content_type)
# change_currency_permission = Permission.objects.get_or_create(codename='change_currency',
#                                    name='Can change currency',
#                                    content_type=currency_content_type)
# delete_currency_permission = Permission.objects.get_or_create(codename='delete_currency',
#                                    name='Can delete currency',
#                                    content_type=currency_content_type)
# view_currency_permission = Permission.objects.get_or_create(codename='view_currency',
#                                    name='Can view currency',
#                                    content_type=currency_content_type)
# # *****************
# # user country permissions
# add_user_country_permission = Permission.objects.get_or_create(codename='add_usercountry',
#                                    name='Can add user country',
#                                    content_type=user_country_content_type)
# change_user_country_permission = Permission.objects.get_or_create(codename='change_usercountry',
#                                    name='Can change user country',
#                                    content_type=user_country_content_type)
# delete_user_country_permission = Permission.objects.get_or_create(codename='delete_usercountry',
#                                    name='Can delete user country',
#                                    content_type=user_country_content_type)
# view_user_country_permission = Permission.objects.get_or_create(codename='view_usercountry',
#                                    name='Can view user country',
#                                    content_type=user_country_content_type)
# # *****************
# """
# Customer Permissions
# """
# # customer permissions
# add_customer_permission = Permission.objects.get_or_create(codename='add_customer',
#                                    name='Can add customer',
#                                    content_type=customer_content_type)
# change_customer_permission = Permission.objects.get_or_create(codename='change_customer',
#                                    name='Can change customer',
#                                    content_type=customer_content_type)
# delete_customer_permission = Permission.objects.get_or_create(codename='delete_customer',
#                                    name='Can delete customer',
#                                    content_type=customer_content_type)
# view_customer_permission = Permission.objects.get_or_create(codename='view_customer',
#                                    name='Can view customer',
#                                    content_type=customer_content_type)
# # *****************
# """
# Group Permissions
# """
# # group permissions
# add_group_permission = Permission.objects.get_or_create(codename='add_currency',
#                                    name='Can add currency',
#                                    content_type=currency_content_type)
# change_group_permission = Permission.objects.get_or_create(codename='change_currency',
#                                    name='Can change currency',
#                                    content_type=currency_content_type)
# delete_group_permission = Permission.objects.get_or_create(codename='delete_currency',
#                                    name='Can delete currency',
#                                    content_type=currency_content_type)
# view_group_permission = Permission.objects.get_or_create(codename='view_currency',
#                                    name='Can view currency',
#                                    content_type=currency_content_type)
# # *****************
# new_group.permissions.add(permission)
# @receiver(post_save, sender=User)
# def add_user_to_group(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == "administrator":
#             administrator_group = Group.objects.get_or_create
#             order.total += instance.product.price * instance.quantity
#             order.save()
#
