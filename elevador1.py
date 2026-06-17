def iniciar_sistema():
    print("=== 🏢 Sistema de Elevadores da Faculdade SENAC ===")
    
    elevador_a = 0
    elevador_b = 0
    andares_validos = [-2, -1, 0, 1, 2, 3, 4]
    capacidade_maxima = 8

    viagens_a = 0
    viagens_b = 0
    pessoas_transportadas_a = 0
    pessoas_transportadas_b = 0

    while True:
        print("\n" + "="*50)
        print(f"📍 [STATUS] Elevador A: andar {elevador_a} | Elevador B: andar {elevador_b}")
        print("="*50)
        
        origem_str = input("Digite o seu andar atual: ")
            
        try:
            origem = int(origem_str)
        except ValueError:
            print("⚠️ ERRO: Digite um número de andar válido.")
            continue 

        if origem not in andares_validos:
            print(f"⚠️ ERRO: Andar selecionado não existe. Os andares existentes são: {andares_validos}")
            continue 

        print("\nDica: Digite os andares separados por espaço (Ex: 2 4 -1 4 3)\nLembre-se: O elevador tem capacidade máxima de 8 pessoas por viagem.\n")
        destinos_str = input("Digite seu andar de destino: ")
        
        destinos_brutos = destinos_str.split() 
        fila_destinos = []
        
        for d_str in destinos_brutos:
            try:
                d = int(d_str)
                if d not in andares_validos:
                    print(f"⚠️ AVISO: O destino '{d}' não existe. Esse usuário foi ignorado.")
                    continue
                if d == origem:
                    print(f"⚠️ AVISO: O destino '{d}' é igual à origem. Usuário ignorado.")
                    continue
                
                fila_destinos.append(d)
                
            except ValueError:
                print(f"⚠️ AVISO: '{d_str}' não é um número válido e foi ignorado.")
                continue
                
        if len(fila_destinos) == 0:
            print("⚠️ ERRO: Nenhum destino válido foi inserido para viajar.")
            continue

        print(f"\n📋 Total de pessoas aguardando no andar {origem}: {len(fila_destinos)}")

        distancia_a = abs(elevador_a - origem)
        distancia_b = abs(elevador_b - origem)

        if distancia_a <= distancia_b:
            ordem_elevadores = ['A', 'B'] 
        else:
            ordem_elevadores = ['B', 'A'] 

        rodada = 0 

        while len(fila_destinos) > 0:
            lote_atual = fila_destinos[:capacidade_maxima]
            fila_destinos = fila_destinos[capacidade_maxima:]
            
            elevador_escolhido = ordem_elevadores[rodada % 2]
            
            indo_para_baixo = origem > lote_atual[0]
            rota = sorted(list(set(lote_atual)), reverse=indo_para_baixo)

            if elevador_escolhido == 'A':
                print(f"\n➡️  [SISTEMA] Elevador A despachado (Lote {rodada + 1})")
                print(f"   Movendo Elevador A de {elevador_a} para {origem}...")
                elevador_a = origem
                
                pessoas_transportadas_a += len(lote_atual)
                viagens_a += 1
                
                print(f"   🚪 Embarcaram {len(lote_atual)} pessoas. (Sobraram na fila: {len(fila_destinos)})")
                
                for parada in rota:
                    print(f"   Elevador A viajando para o andar {parada}...")
                    elevador_a = parada
                    print(f"   ✅ Desembarque no {parada} concluído.")
                    
            else:
                print(f"\n➡️  [SISTEMA] Elevador B despachado (Lote {rodada + 1})")
                print(f"   Movendo Elevador B de {elevador_b} para {origem}...")
                elevador_b = origem
                
                pessoas_transportadas_b += len(lote_atual)
                viagens_b += 1
                
                print(f"   🚪 Embarcaram {len(lote_atual)} pessoas. (Sobraram na fila: {len(fila_destinos)})")
                
                for parada in rota:
                    print(f"   Elevador B viajando para o andar {parada}...")
                    elevador_b = parada
                    print(f"   ✅ Desembarque no {parada} concluído.")
            
            rodada += 1 

        print("\n🎉 Todas as pessoas foram transportadas com sucesso!")

        print("\n⏳ Sistema sem chamadas. Ativando modo de repouso.")
        
        if elevador_a != 0:
            print(f"   🔋 Recolhendo Elevador A do andar {elevador_a} para o Térreo (0).")
            elevador_a = 0
            
        if elevador_b != 2:
            print(f"   🔋 Recolhendo Elevador B do andar {elevador_b} para o 2º Andar.")
            elevador_b = 2

        print("-" * 50)
        opcao = input("Pressione [ENTER] para aguardar nova chamada ou digite 'sair' para desligar o sistema e ver as estatísticas: ")
        
        if opcao.strip().lower() == 'sair':
            print("\n" + "*"*50)
            print("📊 ESTATÍSTICAS FINAIS DE USO DO SISTEMA")
            print("*"*50)
            print(f"Elevador A: {viagens_a} viagens realizadas | {pessoas_transportadas_a} usuários transportados.")
            print(f"Elevador B: {viagens_b} viagens realizadas | {pessoas_transportadas_b} usuários transportados.")
            print(f"Total Geral: {pessoas_transportadas_a + pessoas_transportadas_b} usuários atendidos.")
            print("Sistema encerrado com sucesso. Até logo!")
            break

if __name__ == "__main__":
    iniciar_sistema()