def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - Analyze HDL")
        print("2 - Analyze LDL")
        print("3 - Analyze Total Cholesterol")
        print("9 - Quit")
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()


def input_value(test_name):
    test_input = input("Enter the {} value:".format(test_name))
    return int(test_input)


def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"


def HDL_driver():
    test_name = "HDL"
    hdl_value = input_value(test_name)
    answer = check_HDL(hdl_value)
    output_result(test_name, hdl_value, answer)


def output_result(test_name, hdl_value, charac):
    print("The results for a {} value of {} is {}"
          .format(test_name, hdl_value, charac))


def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline high"
    elif 160 <= LDL_value < 190:
        return "High"
    else:
        return "Very high"


def LDL_driver():
    test_name = "LDL"
    ldl_value = input_value(test_name)
    answer = check_LDL(ldl_value)
    output_result(test_name, ldl_value, answer)


def check_total_cholesterol(total_value):
    if total_value < 200:
        return "Normal"
    elif 200 <= total_value < 240:
        return "Borderline high"
    else:
        return "High"


def total_driver():
    test_name = "Total Cholesterol"
    total_value = input_value(test_name)
    answer = check_total_cholesterol(total_value)
    output_result(test_name, total_value, answer)


if __name__ == "__main__":
    interface()
