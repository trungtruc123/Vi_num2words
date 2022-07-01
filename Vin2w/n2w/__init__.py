from Vin2w.n2w.large_number import n2w_large_number
from Vin2w.n2w.single import process_n2w_single
from Vin2w.n2w.utils.base import pre_process_n2w


def n2w(number: str):
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return n2w_large_number(clean_number)


def n2w_single(number: str):
    # Xữ lý đặc thù dành cho số điện thoại
    if number[0:3] == '+84':
        number = number.replace('+84', '0')

    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return process_n2w_single(clean_number)
