# Documentação do Perfil do Usuário e Sistema de Gamificação - GUIA.ME
**Data**: 12 de Outubro de 2025

## 1. Visão Geral

A tela de perfil do usuário do **GUIA.ME** foi projetada para ser mais do que uma simples página de informações pessoais. Ela é o centro de uma experiência gamificada que transforma a exploração turística de Brasília em uma jornada envolvente, recompensadora e social. O sistema de gamificação motiva os usuários a descobrirem novos locais, completarem desafios e compartilharem suas experiências.

## 2. Objetivos do Design

O design do perfil e sistema de gamificação foi desenvolvido com os seguintes objetivos estratégicos:

1. **Engajamento Contínuo**: Motivar usuários a retornarem ao app regularmente
2. **Exploração Incentivada**: Encorajar visitas a diferentes tipos de locais
3. **Progressão Visível**: Mostrar claramente o crescimento e conquistas do usuário
4. **Competição Saudável**: Criar senso de comunidade através de rankings
5. **Recompensa Imediata**: Feedback instantâneo para ações positivas

## 3. Estrutura da Interface

### 3.1. Header do Perfil

O cabeçalho estabelece o contexto e fornece acesso rápido a ações importantes.

#### Componentes

**Navegação**:
- Botão de voltar (←)
- Título "Meu Perfil"

**Ações Rápidas**:
- ✏️ **Editar Perfil**: Modificar informações pessoais
- ⚙️ **Configurações**: Preferências e privacidade
- 📤 **Compartilhar**: Compartilhar perfil nas redes sociais

### 3.2. Cabeçalho do Perfil

Seção hero com gradiente azul que apresenta as informações principais do usuário.

#### Elementos Visuais

**Avatar e Nível**:
- Avatar circular (120x120px)
- Badge de nível no canto inferior direito
- Borda branca destacada
- Sombra para profundidade

**Informações Principais**:
- **Nome**: Fonte grande e bold (32px)
- **Título**: Baseado no nível atual + cidade de origem
- **Ícone de Status**: Emoji representando conquista atual

**Estatísticas em Destaque**:

| Métrica | Descrição | Importância |
|---------|-----------|-------------|
| **Pontos** | XP acumulado total | Progresso geral |
| **Locais Visitados** | Número de check-ins | Exploração |
| **Conquistas** | Medalhas desbloqueadas | Realização |
| **Roteiros** | Roteiros completados | Engajamento |

#### Design Visual

```
┌─────────────────────────────────────────┐
│  [Avatar]     Maria Silva               │
│   [Lvl 12]    🏆 Exploradora Veterana   │
│               São Paulo, SP             │
│                                         │
│   2.450      28        15        8      │
│   Pontos   Locais  Conquistas Roteiros │
└─────────────────────────────────────────┘
```

### 3.3. Barra de Progresso de Nível

Componente crucial que mostra visualmente o progresso do usuário.

#### Características

**Informações Exibidas**:
- Nível atual e título
- XP atual / XP necessário
- Porcentagem de progresso
- Próximo nível e recompensa

**Design da Barra**:
- Altura: 32px
- Gradiente azul animado
- Efeito shimmer (brilho deslizante)
- Texto branco sobre a barra preenchida
- Transição suave de 1s

**Feedback Motivacional**:
> "Faltam 550 XP para alcançar o Nível 13 - Mestre Explorador 🎖️"

## 4. Sistema de Níveis

### 4.1. Hierarquia de Níveis

O sistema possui 20 níveis progressivos, cada um com título único:

| Nível | Título | XP Necessário | Recompensa |
|-------|--------|---------------|------------|
| 1-3 | Novato | 0-500 | Badge inicial |
| 4-6 | Explorador | 500-1.200 | Avatar especial |
| 7-9 | Aventureiro | 1.200-2.000 | Filtro exclusivo |
| 10-12 | Veterano | 2.000-3.000 | Título dourado |
| 13-15 | Mestre | 3.000-4.500 | Emblema raro |
| 16-18 | Lenda | 4.500-6.500 | Skin premium |
| 19-20 | Guardião | 6.500-10.000 | Conquista máxima |

### 4.2. Ganho de XP

Ações que concedem experiência:

| Ação | XP | Frequência |
|------|----|-----------| 
| Check-in em local | 50 XP | Ilimitado |
| Primeira visita a local | 100 XP | Uma vez por local |
| Avaliação com foto | 80 XP | Uma vez por local |
| Completar roteiro | 150 XP | Por roteiro |
| Desafio diário | 100-200 XP | Diário |
| Compartilhar descoberta | 30 XP | Ilimitado |
| Responder pergunta | 20 XP | Ilimitado |
| Conquistar medalha | 200-500 XP | Por conquista |

## 5. Sistema de Conquistas

### 5.1. Categorias de Conquistas

As conquistas são organizadas em categorias temáticas:

#### 🏛️ Monumentos e Arquitetura

| Conquista | Descrição | Ícone | Recompensa |
|-----------|-----------|-------|------------|
| **Primeiro Passo** | Visite seu primeiro monumento | 🏛️ | 100 XP |
| **Arquiteto** | Visite 10 monumentos | 🏛️ | 300 XP |
| **Niemeyer Fan** | Visite todas as obras de Niemeyer | 🏛️ | 1000 XP |

#### 🎨 Arte e Cultura

| Conquista | Descrição | Ícone | Recompensa |
|-----------|-----------|-------|------------|
| **Apreciador** | Visite 5 museus | 🎨 | 200 XP |
| **Conhecedor** | Visite 15 espaços culturais | 🎨 | 500 XP |
| **Patrono das Artes** | Participe de 10 eventos culturais | 🎨 | 800 XP |

#### 🍽️ Gastronomia

| Conquista | Descrição | Ícone | Recompensa |
|-----------|-----------|-------|------------|
| **Degustador** | Visite 5 restaurantes | 🍽️ | 150 XP |
| **Gourmet** | Visite 15 restaurantes | 🍽️ | 400 XP |
| **Crítico Gastronômico** | Avalie 30 restaurantes | 🍽️ | 700 XP |

#### 🌳 Natureza e Parques

| Conquista | Descrição | Ícone | Recompensa |
|-----------|-----------|-------|------------|
| **Ar Livre** | Visite 3 parques | 🌳 | 120 XP |
| **Natureza** | Visite 8 áreas verdes | 🌳 | 350 XP |
| **Eco Warrior** | Complete trilha ecológica | 🌳 | 600 XP |

#### 📸 Social e Compartilhamento

| Conquista | Descrição | Ícone | Recompensa |
|-----------|-----------|-------|------------|
| **Fotógrafo** | Compartilhe 50 fotos | 📸 | 250 XP |
| **Influencer** | Receba 100 curtidas | 📸 | 500 XP |
| **Embaixador** | Convide 5 amigos | 📸 | 800 XP |

#### 🏃 Atividade e Exploração

| Conquista | Descrição | Ícone | Recompensa |
|-----------|-----------|-------|------------|
| **Caminhante** | Caminhe 10km | 🏃 | 200 XP |
| **Maratonista** | Caminhe 50km | 🏃 | 600 XP |
| **Explorador Total** | Visite todas as regiões | 🏃 | 1500 XP |

### 5.2. Design dos Cards de Conquista

**Conquista Desbloqueada**:
- Fundo: Cinza claro (hover: branco)
- Ícone: Colorido, 48px
- Badge verde com ✓
- Nome em bold
- Descrição em cinza
- Efeito hover: Elevação e sombra

**Conquista Bloqueada**:
- Opacidade: 50%
- Ícone: Escala de cinza
- Sem badge
- Texto mais claro
- Cursor: Não permitido

## 6. Sistema de Desafios Diários

### 6.1. Mecânica de Desafios

Os desafios diários renovam a cada 24 horas e incentivam atividades específicas.

#### Tipos de Desafios

**Exploração**:
- Visite X locais de uma categoria
- Descubra um novo bairro
- Faça check-in em horário específico

**Social**:
- Compartilhe X fotos
- Avalie X locais
- Convide um amigo

**Atividade**:
- Caminhe X quilômetros
- Complete um roteiro
- Visite locais em sequência

### 6.2. Design dos Cards de Desafio

**Estrutura**:
```
┌─────────────────────────────────────┐
│ 🏛️ Explorador de Monumentos  +150XP│
│ Visite 3 monumentos históricos hoje │
│ ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░  2/3          │
└─────────────────────────────────────┘
```

**Elementos**:
- Ícone temático
- Título descritivo
- Badge de recompensa (dourado)
- Descrição clara
- Barra de progresso visual
- Contador numérico

**Estados**:
- **Em Progresso**: Barra parcialmente preenchida (verde)
- **Completo**: Barra cheia + animação de celebração
- **Expirado**: Opacidade reduzida

## 7. Ranking Semanal

### 7.1. Sistema de Ranking

O ranking cria competição saudável e senso de comunidade.

#### Características

**Período**: Semanal (reset toda segunda-feira)
**Critério**: Pontos XP ganhos na semana
**Posições Destacadas**:
- 🥇 **1º Lugar**: Badge dourado
- 🥈 **2º Lugar**: Badge prateado
- 🥉 **3º Lugar**: Badge bronze
- **Usuário Atual**: Destaque com borda azul

### 7.2. Design dos Itens de Ranking

**Estrutura**:
- Posição (círculo colorido)
- Avatar do usuário
- Nome e nível
- Pontos XP

**Usuário Atual**:
- Fundo: Gradiente azul claro
- Borda: 2px azul sólido
- Texto: "(Você)" após o nome

## 8. Linha do Tempo de Atividades

### 8.1. Registro de Atividades

Mostra as ações recentes do usuário em ordem cronológica.

#### Tipos de Atividade

- ✓ Conquista desbloqueada
- 📍 Local visitado
- ✅ Roteiro completado
- ⭐ Avaliação realizada
- 📈 Subida de nível
- 📸 Foto compartilhada
- 💬 Comentário postado

### 8.2. Design da Timeline

**Linha Vertical**:
- Cor: Cinza claro
- Largura: 2px
- Posição: Esquerda

**Marcadores**:
- Círculo azul (12px)
- Borda branca
- Sombra azul

**Conteúdo**:
- Ação em bold
- Detalhes em texto normal
- Timestamp em cinza claro

## 9. Paleta de Cores da Gamificação

### Cores por Elemento

| Elemento | Cor | Hex | Uso |
|----------|-----|-----|-----|
| **XP/Progresso** | Azul | `#0047AB` | Barras, badges |
| **Conquistas** | Dourado | `#D4AF37` | Medalhas, recompensas |
| **Desafios** | Verde | `#6B8E23` | Progresso de desafios |
| **Ouro (1º)** | Dourado | `#FFD700` | Primeiro lugar |
| **Prata (2º)** | Prateado | `#C0C0C0` | Segundo lugar |
| **Bronze (3º)** | Bronze | `#CD7F32` | Terceiro lugar |

## 10. Animações e Feedback

### 10.1. Animações Implementadas

**Entrada de Elementos**:
- Fade in up (0.6s)
- Observador de scroll
- Delay sequencial

**Barras de Progresso**:
- Preenchimento animado (1s)
- Efeito shimmer contínuo
- Transição suave

**Hover em Cards**:
- Elevação (-4px)
- Sombra aumentada
- Transição 0.3s

### 10.2. Feedback de Conquistas

Quando uma conquista é desbloqueada:

1. **Notificação Push**: "Nova conquista! 🎉"
2. **Modal de Celebração**: Card grande com animação
3. **Confete Animado**: Partículas coloridas
4. **Som de Vitória**: Feedback auditivo
5. **Atualização de XP**: Barra de progresso anima

## 11. Responsividade

### Adaptações por Dispositivo

**Desktop (> 1024px)**:
- Grid 2 colunas (2fr + 1fr)
- Todos os elementos visíveis
- Hover effects ativos

**Tablet (768px - 1024px)**:
- Grid 1 coluna
- Elementos empilhados
- Espaçamento ajustado

**Mobile (< 768px)**:
- Header de perfil vertical
- Estatísticas centralizadas
- Cards de conquista menores (100px)
- Fonte reduzida

## 12. Psicologia da Gamificação

### 12.1. Princípios Aplicados

**1. Progressão Clara**:
- Barra de nível sempre visível
- Feedback imediato de XP
- Próximo objetivo explícito

**2. Recompensas Variadas**:
- XP (quantitativo)
- Conquistas (qualitativo)
- Títulos (status social)
- Itens exclusivos (exclusividade)

**3. Desafios Balanceados**:
- Fáceis: Completáveis em minutos
- Médios: Requerem planejamento
- Difíceis: Objetivos de longo prazo

**4. Competição Social**:
- Ranking visível
- Comparação com pares
- Reconhecimento público

**5. Autonomia**:
- Escolha de desafios
- Personalização de perfil
- Controle de privacidade

### 12.2. Loops de Engajamento

**Loop Principal**:
```
Explorar Local → Ganhar XP → Subir Nível → 
Desbloquear Conquista → Compartilhar → 
Receber Reconhecimento → Explorar Mais
```

**Loop Diário**:
```
Abrir App → Ver Desafios → Completar Desafio → 
Ganhar Recompensa → Voltar Amanhã
```

**Loop Social**:
```
Ver Ranking → Comparar Posição → 
Querer Subir → Explorar Mais → 
Ganhar Pontos → Subir no Ranking
```

## 13. Métricas de Sucesso

### KPIs do Sistema de Gamificação

| Métrica | Objetivo | Medição |
|---------|----------|---------|
| **Taxa de Retenção** | > 60% (7 dias) | Usuários ativos |
| **Engajamento Diário** | > 3 ações/dia | Check-ins, avaliações |
| **Completude de Desafios** | > 40% | Desafios completados |
| **Conquistas por Usuário** | > 5 (30 dias) | Medalhas desbloqueadas |
| **Tempo no App** | > 15 min/sessão | Duração média |

## 14. Futuras Expansões

### Funcionalidades Planejadas

**1. Eventos Especiais**:
- Desafios temáticos mensais
- Conquistas sazonais
- Recompensas limitadas

**2. Sistema de Clãs**:
- Grupos de exploradores
- Desafios em equipe
- Ranking de clãs

**3. Loja de Recompensas**:
- Trocar XP por itens
- Avatares premium
- Filtros exclusivos

**4. Missões Narrativas**:
- Histórias interativas
- Descobertas guiadas
- Recompensas épicas

**5. Integração Social**:
- Desafiar amigos
- Compartilhar progresso
- Presentes virtuais

## 15. Acessibilidade

### Práticas Implementadas

1. **Contraste**: WCAG AAA em textos críticos
2. **Tamanhos**: Mínimo 44x44px para toques
3. **Feedback Visual**: Múltiplos indicadores de progresso
4. **Alternativas**: Texto para todos os ícones
5. **Navegação**: Suporte completo a teclado

## 16. Conclusão

O sistema de gamificação do **GUIA.ME** transforma a exploração turística de Brasília em uma experiência envolvente e recompensadora. Através de níveis, conquistas, desafios e rankings, os usuários são motivados a descobrir mais da cidade, compartilhar suas experiências e se tornarem verdadeiros exploradores da capital.

A interface do perfil não apenas exibe informações, mas conta a história da jornada de cada usuário, celebrando suas conquistas e incentivando novas descobertas. Este design cria um ciclo virtuoso de engajamento que beneficia tanto os usuários quanto o ecossistema turístico de Brasília.

---

## Referências

1. Chou, Y. (2015). *Actionable Gamification: Beyond Points, Badges, and Leaderboards*. Octalysis Media.
2. Deterding, S. et al. (2011). *From Game Design Elements to Gamefulness*. MindTrek.
3. Zichermann, G. & Cunningham, C. (2011). *Gamification by Design*. O'Reilly Media.
4. Duolingo. (2024). *Gamification Best Practices*. [https://design.duolingo.com/](https://design.duolingo.com/)
5. Fitbit. (2024). *Achievement System Design*. [https://www.fitbit.com/](https://www.fitbit.com/)

