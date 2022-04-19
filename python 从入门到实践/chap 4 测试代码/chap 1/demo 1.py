# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/27 14:35


from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first =='q':
        break
    last = input("Please give me alst name:")
    if last =='q':
        break
    formatted_name = get_formatted_name(first,last)
    print("\tNeatly formatted name:" + formatted_name + '.')

