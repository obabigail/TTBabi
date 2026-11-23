# TTBabi
Tabletop Roleplaying games manager

### Checklist
## 1. Configuração e estrutura
- [x] Criar repositório Git com README e .gitignore
- [x] Configurar ambiente virtual Python e dependências
- [ ] Separar interface, modelos de dados, regras e serviços
- [ ] Definir o schema do personagem com Pydantic
- [ ] Definir sistema e versão das regras nos dados do personagem
- [ ] Criar tema visual inicial (cores, tipografia e componentes)

## 2. Interface e navegação
- [ ] Criar página inicial com opções de novo personagem e importar ficha
- [ ] Criar wizard de criação dividido em etapas
- [ ] Mostrar progresso e permitir avançar ou voltar
- [ ] Criar resumo persistente do personagem durante o processo
- [ ] Manter os dados preenchidos ao trocar de etapa
- [ ] Destacar campos obrigatórios, alertas e informações das regras
- [ ] Implementar layout responsivo e modo escuro
- [ ] Criar visualização final da ficha antes da exportação

## 3. Identidade e narrativa
- [ ] Nome do personagem e nome do jogador (opcional)
- [ ] Classe e nível inicial
- [ ] Espécie e antecedente
- [ ] Tendência e idiomas
- [ ] Idade, aparência e descrição física (opcionais)
- [ ] Personalidade, ideais, vínculos e defeitos (opcionais)
- [ ] História pessoal em texto livre
- [ ] Retrato ou avatar opcional

## 4. Atributos e mecânicas
- [ ] Implementar os seis atributos
- [ ] Oferecer conjunto padrão de atributos (Standard Array)
- [ ] Implementar Point Buy com validação dos 27 pontos
- [ ] Implementar geração por 4d6, descartando o menor
- [ ] Aplicar ajustes de atributos do antecedente
- [ ] Calcular modificadores automaticamente
- [ ] Calcular bônus de proficiência
- [ ] Calcular pontos de vida e dados de vida
- [ ] Calcular iniciativa, deslocamento e CA
- [ ] Calcular testes de resistência, perícias e percepção passiva
- [ ] Aplicar proficiências e características de classe/origem
- [ ] Permitir equipamentos iniciais e escolhas previstas nas opções implementadas

## 5. Classes e magia
- [ ] Implementar uma classe marcial completa de nível 1
- [ ] Implementar uma segunda classe para testar diferenças nas escolhas
- [ ] Implementar pelo menos uma classe conjuradora de nível 1
- [ ] Exibir características de classe e proficiências
- [ ] Permitir escolhas de perícias e opções de classe aplicáveis
- [ ] Permitir seleção de truques e magias aplicáveis
- [ ] Calcular atributos de conjuração e espaços de magia, quando houver
- [ ] Exibir descrições resumidas e referências das habilidades

## 6. Verificação de regras
- [ ] Criar funções puras e testáveis para os cálculos
- [ ] Validar limites e método escolhido de distribuição de atributos
- [ ] Validar quantidade e elegibilidade de proficiências
- [ ] Validar requisitos e escolhas de classe/origem
- [ ] Validar quantidade de magias permitidas, quando aplicável
- [ ] Detectar campos obrigatórios ausentes ou inconsistentes
- [ ] Diferenciar erro, aviso e escolha personalizada
- [ ] Exibir uma justificativa e a fonte para cada validação

## 7. Rolagem de dados
- [ ] Criar interface visual para d4, d6, d8, d10, d12, d20 e d100
- [ ] Implementar fórmulas como 2d6+3
- [ ] Mostrar resultados individuais e total
- [ ] Implementar vantagem e desvantagem para d20
- [ ] Integrar botões de rolagem aos atributos, perícias e testes de resistência
- [ ] Manter histórico de rolagens durante a sessão
- [ ] Limitar quantidade de dados e validar entradas inválidas

## 8. Fichas e exportação
- [ ] Construir visualização digital da ficha completa
- [ ] Criar modelo de PDF com organização tradicional de D&D
- [ ] Preencher automaticamente os campos do PDF
- [ ] Criar uma segunda opção de PDF com layout personalizado
- [ ] Exportar personagem em JSON para backup
- [ ] Importar JSON e restaurar o personagem
- [ ] Garantir que campos longos e habilidades não sejam cortados
- [ ] Exibir mensagens claras para campos não suportados pelo template

## 9. Persistência e robustez
- [ ] Criar modelo único do personagem, independente dos widgets
- [ ] Garantir continuidade entre etapas usando Session State
- [ ] Implementar restaurar/importar uma criação
- [ ] Permitir edição de um personagem já criado
- [ ] Impedir perda de informações durante recálculos e reruns
- [ ] Tratar falhas de leitura de arquivos e fontes de dados
- [ ] Escolher armazenamento persistente caso deseje salvar no servidor

## 10. Testes e entrega
- [ ] Testar funções de atributos, proficiências e cálculos
- [ ] Testar ao menos um personagem marcial e um conjurador
- [ ] Testar navegação entre todas as etapas
- [ ] Testar importação e exportação sem perda de dados
- [ ] Testar PDFs com textos curtos e longos
- [ ] Testar o fluxo completo no navegador
- [ ] Criar instruções de instalação e execução
- [ ] Disponibilizar uma versão demonstrável
