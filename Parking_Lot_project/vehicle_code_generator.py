import random
def code_generator():
    Alfabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    integers="0123456789"
    final_code=""
    for i in range(4):
        final_code=final_code+random.choice(integers)
        final_code=final_code+random.choice(Alfabets)
        
    return final_code
# print(code_generator())    