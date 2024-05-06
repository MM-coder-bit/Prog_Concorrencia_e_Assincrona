'''
### Resumo Simples

Este código usa a biblioteca `asyncio`, que ajuda a lidar com tarefas assíncronas (tarefas que podem acontecer ao mesmo tempo). Ele faz o seguinte:

1. **Define uma função especial**: A função `diz_oi` é especial porque pode ser executada de forma assíncrona, 
    o que significa que outras tarefas podem ser executadas enquanto ela espera para ser concluída.
   
2. **Prepara o loop de eventos**: O loop de eventos é como um "gerente" que coordena o que acontece e quando.

3. **Executa a função `diz_oi`**: O loop de eventos faz com que a função `diz_oi` seja executada.

4. **Fecha o loop**: Depois de executar a função, o loop de eventos é fechado.

Em termos mais simples, o programa está configurado para preparar um sistema de execução de tarefas assíncronas e executa uma tarefa simples que imprime 
"Olá, Mundo!" na tela.
'''

import asyncio

# Define uma função assíncrona chamada 'diz_oi'
async def diz_oi_demorado():
    print("Olá, Mundo!")  # Esta função imprime "Olá, Mundo!"
    await asyncio.sleep(2) # aguarda 2 segundos com await
    print('Tudo certo!')

# Obtém o loop de eventos do asyncio
event_loop = asyncio.get_event_loop()

# Executa a função 'diz_oi' até a conclusão usando o loop de eventos
event_loop.run_until_complete(diz_oi_demorado())

# Fecha o loop de eventos
event_loop.close()
