def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Total Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()
            
def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)
    
def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40<= HDL_value <60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)
    
def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))
    
def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)
    
def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borerline high"
    elif 160 <= LDL_value < 190:
        return "High"
    else:
        return "Very high"
        
def output_LDL_result(ldl_value, charac):
    print("The results for an HDL value of {} is {}".format(ldl_value, charac))

def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)
    
def input_total_cholesterol():
    total_input = input("Enter the total cholesterol value:")
    return int(total_input)
    
def check_total_cholesterol(total_value):
    if total_value < 200:
        return "Normal"
    elif 200 <= total_value < 240:
        return "Borderline high"
    else:
        return "High"
        
def output_total_cholesterol_result(total_value, charac):
    print("The results for a total cholesterol value of {} is {}".format(total_value, charac))

def total_driver():
    total_value = input_total_cholesterol()
    answer = check_total_cholesterol(total_value)
    output_total_cholesterol_result(total_value, answer)

interface()
