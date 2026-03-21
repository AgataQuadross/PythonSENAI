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
