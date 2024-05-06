'''
### Explicação Objetiva do Código

**Importação de Tipos**
- `from typing import Generator` importa o tipo `Generator` para usar como anotação de tipo na função `fibo`.

**Função `fibo`**
- `fibo` é uma função geradora que retorna números da sequência de Fibonacci de forma assíncrona.
- O `while True` cria um loop infinito, gerando indefinidamente números da sequência.
- `valor, proximo = proximo, valor + proximo` calcula o próximo valor da sequência.
- `yield valor` retorna o próximo número de Fibonacci, mas mantém o estado da função para continuar de onde parou na próxima vez.

**Bloco Principal (`__main__`)**
- O bloco `if __name__ == '__main__':` garante que o código seja executado diretamente.
- `for n in fibo()` itera sobre a função geradora, imprimindo números até que `n` seja maior que 1000.
- `print('\nPronto')` imprime uma mensagem de conclusão.

### Uso Assíncrono
- **Gerador Assíncrono**: O uso do `yield` torna `fibo` assíncrona porque cada chamada à função produz um valor da sequência, 
    mas o loop pode ser interrompido e retomado a qualquer momento sem perder seu estado.
- Isso permite que os números sejam produzidos conforme necessário, ao invés de calcular toda a sequência de uma só vez, 
    tornando-o mais eficiente em termos de memória e processamento.
'''

from typing import Generator

# Define a função geradora 'fibo' que irá gerar números da sequência de Fibonacci
def fibo() -> Generator[int, None, None]:
    valor: int = 0      # Inicializa o primeiro valor da sequência
    proximo: int = 1    # Inicializa o próximo valor da sequência

    # O loop continuará gerando números infinitamente
    while True:
        valor, proximo = proximo, valor + proximo  # Atualiza 'valor' e 'proximo' para os próximos números da sequência
        yield valor    # Retorna o próximo valor da sequência ao chamador

# Quando este arquivo é executado diretamente, a partir do método __main__, executa-se o seguinte bloco
if __name__ == '__main__':
    # Itera sobre a função geradora 'fibo'
    for n in fibo():
        print(n, end=', ')   # Imprime cada número gerado seguido de uma vírgula
        if n > 1000:         # Condição de parada: interrompe o loop se o valor atual for maior que 1000
            break

# Após sair do loop, imprime a mensagem de finalização
print('\nPronto')
