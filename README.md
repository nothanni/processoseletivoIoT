 Monitor de Temperatura com ESP32 – Processo Seletivo Intensivo Maker | IoT
Identificação do Candidato

- **Nome completo:** Paula Hânnia Rocha Santana
- **GitHub:** [nothanni](https://github.com/nothanni)

## 1- Visão Geral da Solução

O projeto consiste em um **sistema embarcado simulado de monitoramento de temperatura**, desenvolvido para o desafio técnico do processo seletivo Intensivo Maker | IoT.

**Objetivo:** simular a leitura de um sensor de temperatura e sinalizar visualmente por meio de LEDs quando a temperatura atinge um limiar crítico.

**Funcionamento:**
- A temperatura varia aleatoriamente ao longo do tempo, simulando a leitura de um sensor real.
- Quando a temperatura está **abaixo de 25°C**, o **LED verde** permanece aceso (condição normal).
- Quando a temperatura atinge ou ultrapassa **25°C**, o **LED vermelho** acende e o LED verde apaga (alerta de temperatura elevada).
- O sistema imprime continuamente no terminal o valor atual da temperatura e o estado dos LEDs.

**Interação com o usuário:** o sistema é autônomo, não requer interação direta. O usuário acompanha os dados pelo monitor serial da simulação Wokwi.

---

## 2️- Arquitetura do Sistema Embarcado

### Fluxo principal do programa (`main.py`)
nício
↓
Inicializa LEDs (vermelho no GPIO 23, verde no GPIO 22)
↓
Loop infinito:
├─ Atualiza temperatura com variação aleatória
├─ Limita temperatura entre 15°C e 35°C
├─ Exibe valor no terminal
├─ Se temp ≥ 25°C → liga LED vermelho, desliga verde
└─ Senão → liga LED verde, desliga vermelho
↓
Aguarda 1 segundo
↓
Repete


### Estrutura de estados

O sistema opera com dois estados lógicos implícitos, definidos pelo limiar de temperatura:

| Estado | Condição | LED Vermelho | LED Verde |
|--------|----------|:---:|:---:|
| Normal | temp < 25°C | OFF | ON |
| Alerta | temp ≥ 25°C | ON | OFF |

### Temporização

O programa utiliza `time.sleep(1)` para aguardar 1 segundo entre os ciclos de leitura, garantindo uma taxa de atualização estável e previsível.

---

## 3️- Componentes Utilizados na Simulação

| Componente | Tipo | Função |
|------------|------|--------|
| ESP32 DevKit C V4 | Placa microcontroladora | Executa o firmware e controla os LEDs |
| LED Vermelho | `wokwi-led` (pino 23) | Indica alerta de temperatura alta |
| LED Verde | `wokwi-led` (pino 22) | Indica temperatura normal |

### Conexões (`diagram.json`)

- LED Vermelho → GPIO 23 e GND
- LED Verde → GPIO 22 e GND
- Comunicação serial TX/RX configurada para o monitor serial

---

## 4️- Decisões Técnicas Relevantes

1. **Simulação de sensor:** optou-se por simular a variação de temperatura utilizando `random.uniform()` com tendência de retorno ao centro, evitando a necessidade de um sensor físico e mantendo o comportamento realista.

2. **Limiar fixo:** o valor de 25°C foi definido como constante de corte para alternância dos LEDs, seguindo referências comuns de conforto térmico.

3. **Limites de temperatura:** a temperatura foi limitada entre 15°C e 35°C (`max`/`min`) para evitar valores extremos irreais durante a simulação.

4. **Organização do código:** o código foi estruturado de forma linear e comentada, com inicialização clara dos periféricos e loop principal bem definido, facilitando a leitura e manutenção.

5. **Uso de GPIOs:** os pinos 22 e 23 foram escolhidos por serem GPIOs de uso geral disponíveis no ESP32 DevKit C V4.

---

## 5️- Resultados Obtidos

**Sistema funcional:** o código executa sem erros de sintaxe e implementa corretamente a lógica de controle de temperatura e LEDs.

**Diagrama correto:** o `diagram.json` contém todos os componentes necessários e as conexões nos pinos corretos, compatíveis com o `main.py`.

**Simulação Wokwi:** a simulação foi configurada e executada via GitHub Actions, com conexão bem-sucedida à API do Wokwi.

Problema: **Pipeline CI/CD:** o pipeline foi integralmente configurado (GitHub Actions + Secrets + Wokwi CLI). Houve instabilidade no parser TOML da ferramenta Wokwi CLI durante a execução automatizada, impedindo a validação final com *green check*, mas todas as etapas de build e configuração foram concluídas.


## 6️- Comentários Adicionais

- **Dificuldades encontradas:** a principal dificuldade foi a integração com o Wokwi CLI via GitHub Actions, especialmente em relação ao formato do arquivo `wokwi.toml` e à comunicação entre os ambientes Windows (desenvolvimento) e Linux ( Actions).

- **Aprendizados:** este desafio proporcionou um grande aprendizado sobre Git/GitHub (fork, clone, commit, push), configuração de secrets em ambientes de CI/CD, uso de GitHub Actions e simulação de hardware com Wokwi.

- **Melhorias futuras:** com mais tempo, seria interessante implementar uma máquina de estados formal, substituir o `time.sleep()` por temporização não-bloqueante (`millis()`), e adicionar uma histerese para evitar oscilações nos LEDs quando a temperatura estiver próxima ao limiar.