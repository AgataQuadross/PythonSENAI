# Trabalho feito por Ágata Quadros e Alvaro Ventura de Carvalho Rodrigues
# Ágata = 001203336@senaimgaluno.com.br
# Alvaro = 0001203783@senaimgaluno.com.br

# variavel -> nome_variavel
# função -> NomeFuncao
# docionario -> nome
# vetor -> nome


import os



def LimparTela():
    os.system('cls' if os.name == 'nt' else 'clear')



# ---- Login do Administrador ----
def LoginAdmin():
    LimparTela()
    print("---- Login do Administrador ----")

    # define as variaveis de login
    usuario_correto = "admin"
    senha_correta = "1234"

    # validação de loging por numero de tentativa
    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("\nAcesso Autorizado!")
            return True
        else:
            tentativas -= 1
            print(f"Credenciais incorretas. Você tem {tentativas} tentativa(s) restante(s).\n")

    print(" Acesso Bloqueado. Sistema encerrado.")
    return False



# ---- Cadastro de Peças (Área Admin) ----
def CatalogoPecas(catalogo):
    LimparTela()
    print("---- Cadastro de Peças ----")


    # validação de quantidade de peças a cadastrar
    try:
        numero_pecas = int(input("\nQuantas peças deseja cadastrar? "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")
        return
            
    
    # cadastrando as peças e adicionado elas ao dicionario
    for i in range(numero_pecas):
        print(f"\n-- Cadastrando a {i+1}ª peça --")
        nome_peca = input("Nome da peça: ").strip().title()

        try:
            preco_peca = float(input(f"Preço de '{nome_peca}': R$ ").replace(',', '.'))
            quant_peca = int(input(f"Quantidade em estoque: "))

            # Salvando preço e quantidade no dicionário aninhado
            catalogo[nome_peca] = {"preco": preco_peca, "quantidade": quant_peca}
            print("Peça cadastrada com sucesso!")

        except ValueError:
            print("Erro: Valor inválido. Esta peça não foi cadastrada.")


    # mostra o catalogo
    print("\n---- Catálogo Atualizado ----")

    for nome, dados in catalogo.items():
        print(f"{nome}: R$ {dados['preco']:.2f} | Estoque: {dados['quantidade']}")



# ---- Área de Vendas (Cliente) ----
def Carrinho(catalogo):
    LimparTela()
    print("---- Carrinho de Compras ----")
    
    # validade para o catalogo vazio
    if not catalogo:
        print("O catálogo está vazio. Volte mais tarde!")
        input("\nPressione Enter para voltar...")
        return 0

    total = 0.0
    continua = True


    # inicio do carrinho
    while continua:
        print("\n-- Peças Disponíveis --")

        # mostra o catalogo
        for nome, dados in catalogo.items():
            print(f"{nome}: R$ {dados['preco']:.2f} (Estoque: {dados['quantidade']})")
            
        # tira os espaços do fim e do começo do input, 
        # deixa todas as primeiras letras do input maiusculas
        compra_peca = input("\nQual peça você gostaria de comprar? ").strip().title()
        
        # peça fora do catalogo
        if compra_peca not in catalogo:
            print("Esta peça não existe no catálogo.")
        else:
            try:
                quant_compra = int(input(f"Quantas unidades de '{compra_peca}' você vai levar? "))
                
                estoque_disponivel = catalogo[compra_peca]["quantidade"]
                
                # valida estoque 
                if quant_compra <= 0:
                    print("Quantidade inválida.")

                elif quant_compra > estoque_disponivel:
                    print(f"Estoque insuficiente. Temos apenas {estoque_disponivel} unidades.")

                else:
                    # Deduz do estoque e soma no total
                    catalogo[compra_peca]["quantidade"] -= quant_compra
                    subtotal_item = catalogo[compra_peca]["preco"] * quant_compra
                    total += subtotal_item
                    
                    # confirmação de compra bem sucedida
                    print(f"{quant_compra}x '{compra_peca}' adicionado(s)! Subtotal do item: R$ {subtotal_item:.2f}")

            except ValueError:
                print("Por favor, digite um número inteiro para a quantidade.")


        # fecha o carrinho
        opcao = input("\nQuer comprar mais? (s/n): ").strip().lower()
        if opcao != "s":
            continua = False

    return total



# ---- Fechamento de Conta (Taxas e Descontos) ----
def Fechamento(total):
    if total == 0:
        return

    LimparTela()
    print("---- Nota Fiscal ----")
    print(f"Subtotal da compra: R$ {total:.2f}")

    # Acima de R$500 == 10% de desconto
    desconto = 0.0
    if total >= 500:
        desconto = total * 0.10
        print(f"Desconto (10%): - R$ {desconto:.2f}")
    
    total_com_desconto = total - desconto

    # 18% de imposto ICMS sobre o valor (com desconto aplicado)
    taxa_icms = total_com_desconto * 0.18
    print(f"Imposto ICMS (18%): + R$ {taxa_icms:.2f}")

    total_final = total_com_desconto + taxa_icms
    print("---------------------")
    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
    print("---------------------\n")
    
    input("Pressione Enter para voltar ao menu...")



# ---- Estrutura Principal ----
def MenuPrincipal():
    # O catálogo nasce aqui e é passado para as funções que precisam dele
    catalogo_loja = {} 

    while True:
        LimparTela()
        print("==== SISTEMA DA LOJA DE PEÇAS ====")
        print("1. Área do Administrador (Cadastrar Peças)")
        print("2. Área do Cliente (Comprar Peças)")
        print("3. Sair")
        print("==================================")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if LoginAdmin():
                CatalogoPecas(catalogo_loja)
        elif opcao == "2":
            total_compra = Carrinho(catalogo_loja)
            Fechamento(total_compra)
        elif opcao == "3":
            LimparTela()
            print("Sistema encerrado. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    MenuPrincipal()