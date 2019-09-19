from banner import banner
banner("A BADLY NAMED PROGRAM", "Keegan Ross")

def a_poorly_named_function(this_is_a_bad_name_for_a_parameter):
    this_name_is_bad = "aeiou"
    what_is_this_for = 0
    for item in this_is_a_bad_name_for_a_parameter:
        if item.lower() in this_name_is_bad:
            what_is_this_for = what_is_this_for + 1
    return what_is_this_for

print("Welcome to a poorly named program.")
if a_poorly_named_function("Keegan") == 2:
    print("This function works!")
else:
    print("This function doesn't work!")