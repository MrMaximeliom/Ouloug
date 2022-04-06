USER_TYPES = (
    ("customer", "Customer"),
    ("customer_administrator", "Administrator Customer"),
    ("agent", "Agent"),
    ("team_leader", "Team Leader"),
    ("administrator", "Administrator"),
    ("special_administrator", "Special Administrator"),
    ("monitor", "Monitor"),
)
USER_STATUS = (
    ("first_login","First Login"),
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("suspended", "Suspended"),
    ("blocked", "Blocked"),
    ("deleted", "Deleted"),
)

# list of available statuses for a country
COUNTRY_STATUS = (
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("suspended", "Suspended"),
    ("on_hold", "On Hold")
)

# list of available statuses for a state
STATE_STATUS = (
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("deleted", "Deleted")
)
# list of available statuses for a package
PACKAGE_STATUS = (
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("deleted", "Deleted")
)
CITY_STATUS = (
    (True,"Active"),
    (False,"Not Active")

)
# for telecom models

TELECOM_STATUS = (
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("deleted", "Deleted")
)

# for package models
PACKAGE_TYPE = (
    ("call_center", "Call Center"),
    ("communication", "Communication")
)

BILLING_TYPE = (
    ("daily", "Daily"),
    ("monthly", "Monthly"),
    ("quarterly", "Quarterly"),
    ("semi_annually", "Semi Annually"),
    ("annually", "Annually"),
)
# for customers models
CUSTOMER_PURCHASE_STATUS = (
    ('paid', 'Paid'),
    ("pending", "Pending"),
    ("trial", "Trial")
)
CUSTOMER_ACCOUNT_STATUS = (
    ("not_confirmed", "Not Confirmed"),
    ("active", "Active"),
    ("suspended", "Suspended"),
    ("closed", "Closed"),
    ("blocked", "Blocked"),
    ("dormant", "Dormant"),
    ("stopped", "Stopped")
)


SERVICE_STATUS = (
    ("active", "active"),
    ("not_active", "not active"),

)
AGENT_CHOICES = (
    ("active", "Active"),
    ("not_active", "Not Active"),

)
TELECOM_NUMBER_TYPE = (
    ("fix_line", "Fix-Line"),
    ("short_code4", "Short-Code4"),
    ("short_code5", "Short-Code5"),
    ("short_code6", "Short-Code6"),
    ("mobile", "Mobile")
)
TELECOM_NUMBER_STATUS = (
    ("available", "Available"),
    ("taken", "Taken"),
    ("withdraw", "Withdraw"),
)
CUSTOMER_TELECOM_NUMBER_STATUS = (
    ("active", "Active"),
    ("stop", "Stop"),
    ("withdraw", "Withdraw"),
)
LOGIN_STATUS = (
    ("login", "Login"),
    ("logout", "Logout"),
    ("break", "Break"),
    ("busy", "Busy"),
    ("on_leave", "On leave"),

)
CALL_DIRECTION = (
    ("inbound", "Inbound"),
    ("outbound", "Outbound")
)
CALL_TYPE = (
    ("normal", "Normal"),
    ("group", "Group")
)
CALL_STATUS = (
    ("complete", "Complete"),
    ("not_answered", "Not Answered"),
    ("rejected", "Rejected"),
    ("busy", "Busy"),
    ("waiting", "Waiting"),
    ("not_completed", "Not Completed"),
)