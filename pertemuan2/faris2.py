def bilangan_prima(n):
    if n < 2:
        return []
    
    prima = []
    
    for num in range(2, n + 1):
        is_prima = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prima = False
                break
        
        if is_prima:
            prima.append(num)
    
    return prima

n = 50
hasil_prima = bilangan_prima(n)

print(f"Bilangan prima dari 1 sampai {n}:")
print(hasil_prima)