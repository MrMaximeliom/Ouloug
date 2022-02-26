from django.utils.translation import gettext_lazy as _

# registration form strings
FIRST_NAME_SYNTAX_ERROR = _("First Name Contains Only Alphanumeric Characters!")
SECOND_NAME_SYNTAX_ERROR = _("Second Name Contains Only Alphanumeric Characters!")
THIRD_NAME_SYNTAX_ERROR = _("Third Name Contains Only Alphanumeric Characters!")
FOURTH_NAME_SYNTAX_ERROR = _("Fourth Name Contains Only Alphanumeric Characters!")
FIRST_NAME_EMPTY_ERROR = _("First Name Cannot Be Empty!")
SECOND_NAME_EMPTY_ERROR = _("Second Name Cannot Be Empty!")
THIRD_NAME_EMPTY_ERROR = _("Third Name Cannot Be Empty!")
FOURTH_NAME_EMPTY_ERROR = _("Fourth Name Cannot Be Empty!")
EMAIL_SYNTAX_ERROR = _("Please Check Your Email Syntax!")
EMAIL_EMPTY_ERROR = _("Email Cannot Be Empty!")
PHONE_NUMBER_SYNTAX_ERROR = _("Please Check Your Phone Number Syntax!")
PHONE_PHONE_EMPTY_ERROR = _("Phone Number Cannot Be Empty!")
PASSWORDS_NOT_MATCH = _("Passwords are Not Match!")



# login form strings
USERNAME_EMPTY_ERROR = _("Username cannot be empty!")
PASSWORD_EMPTY_ERROR = _("Password cannot be empty!")
CONFIRM_PASSWORD_EMPTY_ERROR = _("Confirm Password cannot be empty!")
USERNAME_BAD_FORMAT = _("Username Contains at Least 6 Characters With Only Alphanumeric Characters and Underscores !")



# NO RECORDS FOUND STRINGS - Country Pages
NO_RECORDS_FOR_COUNTRY_MODEL_ADMIN_MESSAGE = _("There are no countries yet ... you can add new ones from ")
NO_RECORDS_FOR_COUNTRY_MODEL_MONITOR_MESSAGE = _("There are no countries yet to view")

# NO RECORDS FOUND STRINGS - City Pages
NO_RECORDS_FOR_CITY_MODEL_ADMIN_MESSAGE = _("There are no cities yet ... you can add new ones from ")
NO_RECORDS_FOR_CITY_MODEL_MONITOR_MESSAGE = _("There are no cities yet to view")