from django.contrib.auth import user_logged_in
from django.db.models.signals import post_save
from apps.address.models import Country
from django.dispatch import receiver

#عند تسجيل مستخدم جديد يتم إنشاء ملف شخصي خاص به تلقائيا
@receiver(post_save,sender=Country)
def alter_user_added_filed(sender,instance,created,**kwargs):
    if created:

         # new_profile.image = "/profile_pics/default_male.jpg"
         # تكون الصورة الشخصية مطابقة لجنس المستخدم الجديد

         instance.added_by = user_logged_in



@receiver(post_save,sender=Country)
def save_country(sender,instance,**kwargs):
    # if instance.gender == 'Male':
    #     instance.profile.image = "/profile_pics/default_male.jpg"
    # else:
    #     instance.profile.image = "/profile_pics/default_female.jpg"

    instance.save()

# Test to link session to user
# @receiver_second(user_logged_in)
# def remove_other_sessions(sender, user, request, **kwargs):
#     # remove other sessions
#     Session.objects.filter(usersession__user=user).delete()
#
#     # save current session
#     request.session.save()
#
#     # create a link from the user to the current session (for later removal)
#     UserSession.objects.get_or_create(
#         user=user,
#         session=Session.objects.get(pk=request.session.session_key)
#     )
# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     LoggedInUser.objects.get_or_create(user=kwargs.get('user'))
#
#
# @receiver(user_logged_out)
# def on_user_logged_out(sender, **kwargs):
#     LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
