class BombaCombustível:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        if valor <= 0:
            return "Valor deve ser maior que zero."
        
        litros = valor / self.valor_litro
        if litros > self.quantidade_combustivel:
            return f"Não há combustível suficiente. Disponível: {self.quantidade_combustivel} litros."
        
        self.quantidade_combustivel -= litros
        return f"Abastecido com {litros:.2f} litros. Total a pagar: R${valor:.2f}"

    def abastecer_por_litro(self, litros):
        if litros <= 0:
            return "Quantidade de litros deve ser maior que zero."
        
        valor = litros * self.valor_litro
        if litros > self.quantidade_combustivel:
            return f"Não há combustível suficiente. Disponível: {self.quantidade_combustivel} litros."
        
        self.quantidade_combustivel -= litros
        return f"Valor a pagar: R${valor:.2f}. Combustível restante: {self.quantidade_combustivel:.2f} litros."

    def alterar_valor(self, novo_valor):
        if novo_valor <= 0:
            return "O valor por litro deve ser maior que zero."
        
        self.valor_litro = novo_valor
        return f"Valor do litro alterado para R${novo_valor:.2f}."

    def alterar_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        return f"Tipo de combustível alterado para {novo_tipo}."

    def alterar_quantidade_combustivel(self, nova_quantidade):
        if nova_quantidade < 0:
            return "A quantidade de combustível não pode ser negativa."
        
        self.quantidade_combustivel = nova_quantidade
        return f"Quantidade de combustível alterada para {nova_quantidade:.2f} litros."


def menu():
    bomba = BombaCombustível("Gasolina", 5.50, 1000)
    while True:
        print("\n--- Menu da Bomba de Combustível ---")
        print("1. Abastecer por valor")
        print("2. Abastecer por litro")
        print("3. Alterar valor do litro")
        print("4. Alterar tipo de combustível")
        print("5. Alterar quantidade de combustível")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            valor = float(input("Digite o valor a ser abastecido: R$"))
            print(bomba.abastecer_por_valor(valor))
        
        elif escolha == '2':
            litros = float(input("Digite a quantidade de litros: "))
            print(bomba.abastecer_por_litro(litros))
        
        elif escolha == '3':
            novo_valor = float(input("Digite o novo valor do litro: R$"))
            print(bomba.alterar_valor(novo_valor))
        
        elif escolha == '4':
            novo_tipo = input("Digite o novo tipo de combustível: ")
            print(bomba.alterar_combustivel(novo_tipo))
        
        elif escolha == '5':
            nova_quantidade = float(input("Digite a nova quantidade de combustível: "))
            print(bomba.alterar_quantidade_combustivel(nova_quantidade))
        
        elif escolha == '6':
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()