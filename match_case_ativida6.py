import os
os.system ("clear")

# entrada
valor_do_produto = float(input("Digite o valor do produto :"))
forma_de_pagamento = int(input("""
1 \t pagamento à vista
2 \t pagamento à prazo
                            
Digite a forma de pagamento"""))

match valor_do_produto:
    case 1: 
        # aplicacao de desconto de 10%
        desconto = valor_do_produto * 0.1
        print(f"Valor do produto:{valor_do_produto}")
        print(f"Forma de pagamento selecionada:{forma_de_pagamento}")
        print(f"valor total:{desconto}")
 


