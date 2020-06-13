def add_list(numbers:list = [], number:int = 0):
    try:
        numbers.append(number)
    except AttributeError:
        numbers = []
        numbers.append(number)
        except Exception: #buh turliin aldaa
    return numbers

nums = [1,2,3]
new = add_list(nums, 4)
print(new)