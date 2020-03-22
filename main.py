
import phone_book
from decor_logger import decor_logger
from param_decor_logger import param_decor_logger


@decor_logger
def some_function(x, a):
    print(x, a)


some_function('очень весело', a='Ха-ха-ха')


@param_decor_logger('log.txt')
def some_function(x, text):
    print(x, text)


some_function('очень весело', text='Ха-ха-ха')


book = phone_book.PhoneBook('abc')
Anna = phone_book.Contact('Anna', 'Anna', '+79034567891')
book.add_contact(Anna)



