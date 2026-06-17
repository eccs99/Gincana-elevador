from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sistema = {
    'elevador_a': 0,
    'elevador_b': 0,
    'viagens_a': 0,
    'viagens_b': 0,
    'pessoas_transportadas_a': 0,
    'pessoas_transportadas_b': 0
}

@app.route('/')
def index():
    return render_template('index.html', sistema=sistema)

@app.route('/chamar', methods=['POST'])
def chamar():
    dados = request.json
    
    try:
        origem = int(dados.get('origem'))
    except ValueError:
        return jsonify({'erro': '⚠️ ERRO: Digite um número de andar válido para origem.'})

    destinos_str = dados.get('destinos', '')
    andares_validos = [-2, -1, 0, 1, 2, 3, 4]
    capacidade_maxima = 8
    
    logs_iniciais = []
    # Agora temos apenas UMA lista de passos por elevador (Independência total)
    passos = {'A': [], 'B': []} 

    if origem not in andares_validos:
        return jsonify({'erro': f'⚠️ ERRO: Andar selecionado não existe. Os andares existentes são: {andares_validos}'})

    destinos_brutos = destinos_str.split() 
    fila_destinos = []
    
    for d_str in destinos_brutos:
        try:
            d = int(d_str)
            if d not in andares_validos:
                logs_iniciais.append(f"⚠️ AVISO: O destino '{d}' não existe. Ignorado.")
                continue
            if d == origem:
                logs_iniciais.append(f"⚠️ AVISO: O destino '{d}' é igual à origem. Ignorado.")
                continue
            fila_destinos.append(d)
        except ValueError:
            logs_iniciais.append(f"⚠️ AVISO: '{d_str}' não é válido e foi ignorado.")
            continue
            
    if len(fila_destinos) == 0:
        return jsonify({'erro': 'Nenhum destino válido inserido.'})

    logs_iniciais.append(f"📋 Total de pessoas aguardando no andar {origem}: {len(fila_destinos)}")

    distancia_a = abs(sistema['elevador_a'] - origem)
    distancia_b = abs(sistema['elevador_b'] - origem)

    ordem_elevadores = ['A', 'B'] if distancia_a <= distancia_b else ['B', 'A']
    rodada = 0 

    while len(fila_destinos) > 0:
        lote_atual = fila_destinos[:capacidade_maxima]
        fila_destinos = fila_destinos[capacidade_maxima:]
        
        elevador_escolhido = ordem_elevadores[rodada % 2]
        passageiros_na_cabine = lote_atual.copy() 
        
        indo_para_baixo = origem > lote_atual[0]
        rota = sorted(list(set(lote_atual)), reverse=indo_para_baixo)
        
        if elevador_escolhido == 'A':
            passos['A'].append({'andar': origem, 'acao': 'mover', 'msg': f"➡️ Movendo Elevador A de {sistema['elevador_a']} para {origem}..."})
            passos['A'].append({'acao': 'abrir_porta', 'passageiros': len(passageiros_na_cabine), 'msg': f"🚪 Embarcaram {len(lote_atual)} pessoas no Elevador A."})
            passos['A'].append({'acao': 'fechar_porta'})
            
            sistema['elevador_a'] = origem
            sistema['pessoas_transportadas_a'] += len(lote_atual)
            sistema['viagens_a'] += 1
            
            for parada in rota:
                passos['A'].append({'andar': parada, 'acao': 'mover', 'msg': f"Elevador A viajando para o andar {parada}..."})
                passageiros_na_cabine = [p for p in passageiros_na_cabine if p != parada]
                passos['A'].append({'acao': 'abrir_porta', 'passageiros': len(passageiros_na_cabine), 'msg': f"✅ Desembarque do Elevador A no {parada} concluído."})
                passos['A'].append({'acao': 'fechar_porta'})
                sistema['elevador_a'] = parada
                
        else:
            passos['B'].append({'andar': origem, 'acao': 'mover', 'msg': f"➡️ Movendo Elevador B de {sistema['elevador_b']} para {origem}..."})
            passos['B'].append({'acao': 'abrir_porta', 'passageiros': len(passageiros_na_cabine), 'msg': f"🚪 Embarcaram {len(lote_atual)} pessoas no Elevador B."})
            passos['B'].append({'acao': 'fechar_porta'})
            
            sistema['elevador_b'] = origem
            sistema['pessoas_transportadas_b'] += len(lote_atual)
            sistema['viagens_b'] += 1
            
            for parada in rota:
                passos['B'].append({'andar': parada, 'acao': 'mover', 'msg': f"Elevador B viajando para o andar {parada}..."})
                passageiros_na_cabine = [p for p in passageiros_na_cabine if p != parada]
                passos['B'].append({'acao': 'abrir_porta', 'passageiros': len(passageiros_na_cabine), 'msg': f"✅ Desembarque do Elevador B no {parada} concluído."})
                passos['B'].append({'acao': 'fechar_porta'})
                sistema['elevador_b'] = parada
        
        rodada += 1 

    # --- O REPOUSO AGORA É ANEXADO DIRETAMENTE NA LISTA DO ELEVADOR ---
    if sistema['elevador_a'] != 0:
        passos['A'].append({'andar': 0, 'acao': 'mover', 'msg': f"🔋 Recolhendo Elevador A para o Térreo (Repouso)."})
        sistema['elevador_a'] = 0
        
    if sistema['elevador_b'] != 2:
        passos['B'].append({'andar': 2, 'acao': 'mover', 'msg': f"🔋 Recolhendo Elevador B para o 2º Andar (Repouso)."})
        sistema['elevador_b'] = 2

    return jsonify({
        'sistema': sistema, 
        'logs_iniciais': logs_iniciais, 
        'passos': passos
    })

if __name__ == '__main__':
    app.run(debug=True)