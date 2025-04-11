# kg to (파운드)1b 변환 함수 만들어 주세요
# 1kg = 2.20462 파운드(lb)
# while, try, except, break 사용

def kg_to_pound(kg):
    pound = kg * 2.20462
    return pound

while True:
    user_input = input("kg 값을 입력하세요 : ")
    try:
        kg = float(user_input)
        pound = kg_to_pound(kg)
        print(f"{kg}kg은 {pound}lb입니다.")
        break
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        
    