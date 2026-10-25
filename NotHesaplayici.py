def average(midterm,final_exam):
    avg=(midterm*0.4)+(final_exam*0.6)
    return avg

def letter_grade(avg):
    if avg>=90:
        return "AA"
    elif avg>=85:
        return "BA"
    elif avg>=80:
        return "BB"
    elif avg>=75:
        return "CB"
    elif avg>=70:
        return "CC" 
    elif avg>=65:
        return "DC"
    elif avg>=60:
        return "DD"
    elif avg>=50:
        return "FD"
    elif avg<50:
        return "FF"

def is_passing(avg):
    if avg>=60:
        return True
    return False

for i in range(5):
    name=input("Adınızı giriniz: ")

    while(True):
        midterm=input("Vize notunuzu giriniz: ")
        final_exam=input("Final notunuzu giriniz: ")

        if midterm.isdigit() and final_exam.isdigit():
            midterm=int(midterm)
            final_exam=int(final_exam)

            if midterm>100 and final_exam>100:
                print("Geçersiz not girdiniz.Tekrar deneyin.")
            else:
                break
        else:
            print("Geçersiz giriş.Lütfen harf veya sembol girmeyiniz.")

        
            
    avg=average(midterm,final_exam)
    harf_notu=letter_grade(avg)
    passing=is_passing(avg)
    print(f"Öğrenci:{name:<5} Ortalama:{avg:<5}")
    print(" ")


   



    
        





