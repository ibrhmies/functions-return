# def topla():
#     print(f"toplamı:{10+30}")
# topla()
#bu şekilde printle yazdırdığımızda fonksiyonu çağırınca program çalışıyor 
# def topla():
#     return f"toplamı {10+30}"
# topla()
#bu şekilde returnle fonksiyonu döndürdüğümüzde topla fonksiyonu çağırdığımızda program çalışmaz
def topla():
    return f"toplamı:{10+30}"
a = topla()
print(a)
#returnle döndürdüğümüz fonksiyonlarda bir değişken atayıp bu değişkende 
#fonksiyonu çağırdığımızda program çalışır