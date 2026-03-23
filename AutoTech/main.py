# Primeiramente fazer o registro das peças que seram inseridas no catálogo 
# Deve ter a quantidade de cada peça que será registrada
# Juntamente com o valor de cada peça
# Utilizar dicionários para facilitar a busca da peça juntamente com seu respectivo valor
import os

def LimparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

#---- Login do Administrador ----
def LoginAdmin():
    LimparTela()
    print("---- Login do Administrador ----")

    usuario_correto = "admin"
    senha_correta = "1234"

    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("\n Acesso Autorizado!")
            return True
        else:
            tentativas -= 1
            print(f" Credenciais incorretas. Você tem {tentativas} tentativa(s) restante(s). \n")

    print(" Acesso Bloqueado. Sistema encerrado.")
    return False

#---- Catálogo de peças ----
def CatalogoPecas():
    LimparTela()

    catalogo = {}

    try:
        numero_pecas = int(input("\nQuantas peças deseja cadastrar? "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")
        return
    
    for i in range(numero_pecas):
        print(f"\n---- Cadastrando a {i+1}ª peça ----")

        nome_peca = input("Nome da peça: ").strip().title()

        try:
            preco_peca = float(input(f"Preço da peça '{nome_peca}': R$ ").replace(',', '.'))

            catalogo[nome_peca] = preco_peca
            print("Peça cadastrada com sucesso!")

        except ValueError:
            print("Erro: Preço inválido. Esta peça não foi cadastrada.")

    print("\n---- Catálogo Finalizado ----")
    for nome, preco in catalogo.items():
        print(f"{nome}: R$ {preco:.2f}")

if __name__ == "__main__":
    
    if LoginAdmin():
     
        CatalogoPecas()


def Carrinho():
    # roda em while
    # acessaa lista de peças
    # calcula total por quantidade da peça
    # apresentar o total
    continua = True
    while continua == True:
        compra_peca = input("Qual peça você gostaria de comprar? (digite uma por vez) ")
        quant_compra = input("Quantas dessa peça você vai levar? ")
        total = 0

        pecas = ListaPecas()
        carrinho = dict.fromkeys(compra_peca, quant_peca)
        
        for peca in pecas == compra_peca:
            peca = pecas.get(compra_peca, "Essa peça não existe")

            total = peca * quant_compra

        nota_fiscal = [{carrinho}, total]
            
        opcao = input("quer comprar mais?")
        if opcao == "s":
            continue
        elif opcao =="n":
            return nota_fiscal
            continua = False
        else:
            print("opção invalida")





def Desconto():
    # acima de 500 == 10% de desconto
    # 18% de imposto icms
    total = Carrinho(total)
    desconto = total

    if total >= 500:
        desconto = total * 100 / 0.10
    
    taxa = desconto * 100 / 0.18
    
    total_desc_taxa = total + taxa

    return total_desc_taxa

