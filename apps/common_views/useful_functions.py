def get_filtered_query(foreign_key, filter_condition, field_name, field_value,
                       foreign_key_second_field=None,deep_foreign_key=False,foreign_key_third_field=None,value=None,**args):
    from django.db.models import Q
    if value:
        query_string = ''
        for item in args:
            query_string += f'{item}__'
        query_string += filter_condition
        kwargs = {
            query_string : value
        }
        return Q(**kwargs)
    if foreign_key:
        kwargs = {
            '{0}__{1}__icontains'.format(field_name, foreign_key_second_field): field_value
        }
        return Q(**kwargs)
    if deep_foreign_key:
        kwargs = {
            '{0}__{1}__{2}__icontains'.format(field_name, foreign_key_second_field,foreign_key_third_field): field_value
        }
        return Q(**kwargs)
    # lodo = ''
    # # country=Sudan,state=Khartoum,city=omdurman
    # for item in range(len(kwargs)):



    if filter_condition == "contains":
        kwargs = {
            '{0}__icontains'.format(field_name): field_value
        }
        return Q(**kwargs)
    if filter_condition.strip() == "starts_with":
        kwargs = {
            '{0}__istartswith'.format(field_name): field_value
        }
        return Q(**kwargs)
    if filter_condition.strip() == "equal":
        kwargs = {
            '{0}__iexact'.format(field_name): field_value

        }
        return Q(**kwargs)
    if filter_condition.strip() == "not_equal":
        kwargs = {
            '{0}__iexact'.format(field_name): field_value
        }
        return ~Q(**kwargs)
