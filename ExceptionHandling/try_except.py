
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#     except ValueError:
#         print("Value error ..")
#     except KeyboardInterrupt:
#         print("KeyboardInterrupt error ..")
#     except:
#         print("other exception")

# There are scenarios where you might want to stop
# your program by raising an exception if a condition occurs.
# You can do this with the raise keyword:
# number = int(input("Please enter a number: "))
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

try:
    print("first print")
    fp = open('corrupt_file123.txt','r')
    print("second print")
    print(fp)
    print("after fp variable")
    bad_var = 1
    var = bad_var
    c = 3/bad_var
    raise NameError
    # import qwertyqw123

except NameError:
    print("Variable name not defined")
except FileNotFoundError:
    print("file not found")
except ZeroDivisionError:
    print("cant print infinity")
except:
    print("unknown error")

else:
    print("inside eles, No exception was met")
finally:
    # fp.close()
    print("inside finally We have completed try...")

# print("yghlsdjvkls")
# fp = open('corruptfile.txt')
# print("wertyuiop")
# var = bad_var
# else:
#     pass
# finally:
#     pass

#
# try:
#     f = open('corruptfile.txt')
#     # if f.name == 'currupt_file.txt':
#     #     raise Exception
# except IOError as e:
#     print("IOError occured")
#     print('First!')
#     print(e)
# except Exception as e:
#     print('Second')
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing Finally...")
#
# print('End of program')
#
# try:
#     ##code block where exception can occur
#     a = input("Enter the number 1 ")
#     b = int(input("Enter the number 2 "))
#     print("before division")
#     # c = a / b
#     print("after division")
#     d = a * b
#     e = a + b
#
# except NameError as e:
#     print("The user have not defined the variable")
#     print(e)
# except ZeroDivisionError:
#     print("Please provide number greater than 0")
# except TypeError as e1:
#     print("Try to make the datatype similar")
#     print(e1)
# except Exception as ex:
#     print(ex)
# else:
#     print(c)
#     print(d)
#     print(e)
# finally:
#     print("good you are done!")
#
#
#
#
#
# Custom Exception
# class Error(Exception):
#     print("New type of error has occured")
#
# class dobException(Error):
#     pass
#
# class customgeneric(Error):
#     pass