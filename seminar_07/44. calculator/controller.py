from views import show_menu, get_rational, get_complex, show_result, show_result_c
from models import parse, calculate, calculate_c


def process_data():
    """ Процесс запроса, обработки и вывода результата """
    number_type = show_menu()
    user_input = ""
    if number_type == 'Q':
        user_input = get_rational()
        data = parse(user_input)
        result = calculate(data)
        show_result(result)
    else:
        user_input = get_complex()
        result = calculate_c(user_input)
        show_result_c(result)
    
