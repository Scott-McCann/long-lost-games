from titlecase import titlecase
from collections import OrderedDict

def pretty_age(age):
    age_fields = OrderedDict([
        ("year", age.years),
        ("month", age.months),
        ("day", age.days),
        ("hour", age.hours),
        ("minute", age.minutes)
    ])

    first = None
    second = None

    for f in age_fields.keys():
        if age_fields[f]:
            plural = f + "" if age_fields[f] == 1 else f + "s"
            if not first:
                first = "{0} {1}".format(age_fields[f], plural)
            else:
                second = "{0} {1}".format(age_fields[f], plural)
                break

    if first and second:
        return "{0}, {1}".format(first, second)
    elif first:
        return "{0}".format(first)
    else:
        return "recently"

def title_Case(title):
    return titlecase(title)


def check_Name(name):
    newName = title_Case(name)
    puncts = ['.,?[]}{;:\/|!@&%><']
    for sym in puncts:
        safeName = newName.replace(sym,' ')

    return safeName

def get_next(objset, idn):
    next_id = None
    all_things = objset

    for i in range(len(all_things)):
        if all_things[i].id == idn:
            if i == len(all_things)-1:
                next_id = None
            else:
                next_id = all_things[i+1].id


    return next_id

def get_previous(objset, idn):
    previous_id = None
    all_things = objset

    for i in range(len(all_things)):
        if all_things[i].id == idn:
            if i == 0:
                previous_id = None
            else:
                previous_id = all_things[i-1].id

    return previous_id
