# Gincana-elevador
 Sistema de Elevadores Inteligentes — SENAC

Trabalho acadêmico desenvolvido para a **Gincana Python** da Faculdade SENAC, sob orientação da Profª Maristela. O projeto simula o controle de dois elevadores simultâneos em um prédio com 7 andares, priorizando eficiência no despacho e transporte de passageiros.

---

 Descrição

O sistema recebe chamadas de um andar de origem com múltiplos destinos, seleciona o elevador mais próximo com base no cálculo de distância (`abs()`), transporta os passageiros em lotes de até 8 pessoas e registra estatísticas de uso ao final. Ao ficar ocioso, cada elevador retorna ao seu andar de repouso padrão.

**Versões disponíveis:**
- `main.py` — Interface via terminal (CLI)
- `app.py` + `templates/index.html` — Interface web com Flask

---

 Estrutura do Prédio

| Andar | Descrição     |
|-------|---------------|
| 4     | 4º Andar      |
| 3     | 3º Andar      |
| 2     | 2º Andar      |
| 1     | 1º Andar      |
| 0     | Térreo        |
| -1    | Subsolo 1     |
| -2    | Subsolo 2     |

---

 Lógica de Funcionamento

1. **Seleção do elevador:** o sistema calcula qual elevador está mais próximo do andar de origem e o despacha primeiro.
2. **Lotação:** passageiros são agrupados em lotes de até 8. Se houver mais de 8 destinos, o segundo elevador é acionado em rodadas alternadas.
3. **Rota otimizada:** os destinos de cada lote são ordenados de forma a minimizar paradas (subindo ou descendo em sequência).
4. **Repouso:** após cada chamada atendida, o Elevador A retorna ao Térreo (0) e o Elevador B ao 2º Andar (2).
5. **Validação:** andares inexistentes e entradas não numéricas são rejeitados com mensagens de aviso.

---

  Como Executar

 Versão Terminal

```bash
python main.py
```

Siga as instruções no prompt: informe o andar de origem e os destinos separados por espaço.

### Versão Web (Flask)

**Pré-requisito:** Python 3.x e Flask instalados.

```bash
pip install flask
python app.py
```

Acesse `http://localhost:5000` no navegador.

---

  Tecnologias Utilizadas

- Python 3.x
- Flask (versão web)
- HTML/CSS/JavaScript (frontend da versão web)

---

 Funcionalidades

- [x] Controle de 2 elevadores simultâneos
- [x] Seleção automática do elevador mais próximo
- [x] Capacidade máxima de 8 passageiros por viagem
- [x] Suporte a múltiplos destinos por chamada
- [x] Validação de entradas
- [x] Modo de repouso automático
- [x] Estatísticas de viagens e passageiros transportados
- [x] Interface web animada (versão Flask)

---

  Equipe

> Diogo Gouvêa
  Eric Santos  
  Fábio Silveira
  Yuri Bering
---


