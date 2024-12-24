import random

def GEN_PAS(col_simv_v_pas):
    string_pas = ''
    for i in range (col_simv_v_pas):
        s_1 = random.choice([
                str(random.randint(0, 9)), 
                chr(random.randint(97, 122)), 
                chr(random.randint(65, 90)),
                random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'])  
        ])
        string_pas += s_1

    return string_pas;

col_simv_v_pas = int(input("Number of characters in the password: "))

print(GEN_PAS(col_simv_v_pas))

 



        


    
    


