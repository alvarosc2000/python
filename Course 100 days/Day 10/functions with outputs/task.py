def format_name(f_name, l_name):
    if(f_name == "" or l_name == ""):
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result {formated_f_name} {formated_l_name}"


print(format_name("JuAN", "YuLL"))


def function_1(text):
    return text + text

def function_2(text):
    return text.title()

outpout = function_2(function_1("hello"))
print(outpout)


print(format_name(input("What is your first name?: "), input("What is you last name?: ")))