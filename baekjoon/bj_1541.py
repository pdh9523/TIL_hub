a=input()
# - 를 )-( 로 다 바꾸고, 양 옆에 () 치기

a = a.replace('-', ')-(')

print(eval(f"({a})"))