# Monitor de Temperatura com ESP32 – Processo Seletivo Intensivo Maker | IoT

## Identificação do Candidato
- **Nome completo:** Paula Hânnia Rocha Santana
- **GitHub:** [nothanni](https://github.com/nothanni)

---

## 1️⃣ Visão Geral da Solução

O projeto consiste em um **sistema embarcado simulado de monitoramento de temperatura**, desenvolvido para o desafio técnico do processo seletivo Intensivo Maker | IoT.

**Objetivo:** simular a leitura de um sensor de temperatura e sinalizar visualmente por meio de LEDs quando a temperatura atinge um limiar crítico.

**Funcionamento:**
- A temperatura varia aleatoriamente ao longo do tempo, simulando a leitura de um sensor real.
- Quando a temperatura está **abaixo de 25°C**, o **LED verde** permanece aceso (condição normal).
- Quando a temperatura atinge ou ultrapassa **25°C**, o **LED vermelho** acende e o LED verde apaga (alerta de temperatura elevada).
- O sistema imprime continuamente no terminal o valor atual da temperatura e o estado dos LEDs.

**Interação com o usuário:** o sistema é autônomo, não requer interação direta. O usuário acompanha os dados pelo monitor serial da simulação Wokwi.

---

## 2️⃣ Arquitetura do Sistema Embarcado

### Fluxo principal do programa (`main.py`)

Início
↓
Inicializa LEDs (vermelho no GPIO 23, verde no GPIO 22)
↓
Loop infinito:
├─ Atualiza temperatura com variação aleatória
├─ Limita temperatura entre 15°C e 35°C
├─ Exibe valor no terminal serial
├─ Se temp ≥ 25°C → liga LED vermelho, desliga verde
└─ Senão → liga LED verde, desliga vermelho
↓
Aguarda 1 segundo
↓
Repete

### Estrutura de estados

O sistema opera com dois estados lógicos definidos pelo limiar de temperatura:

| Estado | Condição | LED Vermelho | LED Verde |
|--------|----------|:---:|:---:|
| Normal | temp < 25°C | OFF | ON |
| Alerta | temp ≥ 25°C | ON | OFF |

### Temporização

O programa utiliza `time.sleep(1)` para aguardar 1 segundo entre os ciclos de leitura, garantindo uma taxa de atualização estável e previsível.

### Fluxo de dados

O dado de temperatura é gerado internamente via `random.uniform()` com tendência de retorno ao centro do intervalo, simulando o comportamento de um sensor físico com variações naturais. Esse valor é processado diretamente no loop principal, comparado ao limiar de 25°C, e então dois outputs são gerados simultaneamente: o acionamento dos GPIOs (LEDs) e a saída no monitor serial, que é também o mecanismo usado pelo Wokwi CI para validar o funcionamento do sistema.

---

## 3️⃣ Componentes Utilizados na Simulação

| Componente | Tipo | Função |
|------------|------|--------|
| ESP32 DevKit C V4 | Placa microcontroladora | Executa o firmware MicroPython e controla os LEDs |
| LED Vermelho | `wokwi-led` (GPIO 23) | Indica alerta de temperatura alta (≥ 25°C) |
| LED Verde | `wokwi-led` (GPIO 22) | Indica temperatura normal (< 25°C) |

### Conexões (`diagram.json`)
- LED Vermelho → GPIO 23 (anodo) e GND (catodo)
- LED Verde → GPIO 22 (anodo) e GND (catodo)
- Comunicação serial TX/RX configurada para o monitor serial do Wokwi

---

## 4️⃣ Decisões Técnicas Relevantes

1. **Simulação de sensor com tendência central:** a variação de temperatura usa `random.uniform()` com intervalos assimétricos dependendo do estado atual — quando acima de 25°C, a tendência é de queda; quando abaixo, de subida. Isso simula o comportamento de um ambiente com equilíbrio térmico, evitando que a temperatura fique presa em extremos.

2. **Limiar fixo de 25°C:** o valor foi definido como constante de corte para alternância dos LEDs, seguindo referências comuns de conforto térmico e facilitando a validação visual durante a simulação.

3. **Limites de temperatura:** a temperatura foi limitada entre 15°C e 35°C com `max()`/`min()` para evitar valores extremos e irreais durante a simulação contínua.

4. **Organização do código:** o código foi estruturado de forma linear e legível, com inicialização clara dos periféricos e loop principal bem definido, seguindo boas práticas de firmware embarcado mesmo em ambiente Python.

5. **Uso de GPIOs 22 e 23:** escolhidos por serem pinos de uso geral disponíveis no ESP32 DevKit C V4 sem conflito com funções especiais da placa.

6. **Firmware mesclado com `vfs_merge`:** para viabilizar a execução do `main.py` no Wokwi CI, foi necessário mesclar o binário do MicroPython com o arquivo `main.py` usando a ferramenta `vfs_merge`, que cria uma imagem LittleFS com os arquivos do projeto e a incorpora ao firmware final. Sem esse processo, o MicroPython inicializa sem o script no filesystem e cai no REPL interativo, impedindo a validação automática.

---

## 5️⃣ Resultados Obtidos

- **Sistema funcional:** o código executa sem erros e implementa corretamente a lógica de controle de temperatura e LEDs.
- **Diagrama correto:** o `diagram.json` contém todos os componentes necessários com conexões nos pinos corretos, compatíveis com o `main.py`.
- **Simulação Wokwi bem-sucedida:** a simulação foi executada com sucesso via GitHub Actions, com conexão à API do Wokwi, execução do firmware e validação do output serial com o texto esperado `"Monitor de Temperatura"`.
- **Pipeline CI/CD aprovado:** o pipeline passou com *green check* confirmado na aba Actions do repositório, após resolução dos desafios de integração entre MicroPython e o Wokwi CLI.

---

## 6️⃣ Comentários Adicionais

- **Dificuldades encontradas:** a principal dificuldade foi a integração com o Wokwi CLI via GitHub Actions. O maior desafio foi descobrir que o MicroPython inicializa sem o `main.py` no filesystem quando executado via CI — diferente do comportamento no simulador web, onde os arquivos são carregados automaticamente. A solução foi usar a ferramenta `vfs_merge` para criar um firmware mesclado que já contém o `main.py` embutido na imagem LittleFS, garantindo sua execução automática ao boot.

- **Limitações da solução:** a temperatura é gerada de forma aleatória, sem leitura de sensor real. Para uma aplicação real, seria necessário integrar um sensor físico como o DHT22 ou NTC e adaptar o código para leitura via protocolo adequado.

- **Melhorias futuras:** com mais tempo, seria interessante implementar uma máquina de estados formal, substituir o `time.sleep()` por temporização não-bloqueante, adicionar histerese para evitar oscilações nos LEDs quando a temperatura está próxima ao limiar, e registrar o histórico de temperaturas para análise posterior.

- **Aprendizados:** este desafio proporcionou aprendizado prático sobre Git/GitHub (fork, clone, commit, push), configuração de secrets em CI/CD, uso de GitHub Actions, simulação de hardware com Wokwi, e o funcionamento interno do MicroPython no ESP32 — especialmente como o filesystem é inicializado e como o firmware é estruturado para execução em CI.