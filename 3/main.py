import json
import os

def read_data():
    with open(os.path.join(os.path.dirname(__file__), "dados.json")) as f:
        return json.load(f)

def main():
    data = read_data()
    
    min = float('inf')
    max = 0
    total = 0
    num_days = len(data)
    days_above_average = 0

    for i in data:
        value = i['valor']
        if value > max:
            max = value
        
        if value < min:
            min = value
        
        total += value
    
    average = total / num_days
    
    for i in data:
        if i['valor'] > average:
            days_above_average += 1
    
    print("Menor valor de faturamento em um dia:", min)
    print("Maior valor de faturamento em um dia:", max)
    print("Média de faturamento:", average)
    print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", days_above_average)
    

if __name__ == "__main__":
    main()