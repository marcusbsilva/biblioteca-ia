# 📚 Biblioteca IA, Software & Computação

Uma coleção gratuita de **6 livros em português** sobre inteligência artificial, desenvolvimento de software e computação. Os livros começam do zero, com explicações simples e analogias do dia a dia, e aprofundam aos poucos até o nível técnico.

Os livros nasceram de um estudo extenso: centenas de aulas e vídeos de criadores brasileiros e internacionais (do CS50 de Harvard e IBM Technology a canais como Augusto Galego e Fernanda Kipper), artigos técnicos de referência (como o artigo original de RAG e o guia de engenharia de contexto da Anthropic) e o blog [AkitaOnRails](https://akitaonrails.com/). Todo esse material foi reorganizado em texto próprio, enriquecido com pesquisa atualizada até **outubro de 2026**, com diagramas e gráficos. Cada capítulo termina com uma tabela de fontes com links, e os autores estão na seção [Créditos](#créditos).

## Baixe e leia

| | Livro | Temas | PDF |
|---|---|---|---|
| <img src="assets/capa1.png" width="90"> | **Livro 1 — Fundamentos de IA e Modelos de Linguagem** | IA, machine learning, deep learning, LLMs, Transformers, Mistura de Especialistas (MoE), LoRA | [Baixar](livros/Livro1_Fundamentos_de_IA_e_Modelos_de_Linguagem.pdf) |
| <img src="assets/capa2.png" width="90"> | **Livro 2 — Construindo com LLMs** | Prompts para qualquer IA, engenharia de contexto, RAG, agentes e MCP | [Baixar](livros/Livro2_Construindo_com_LLMs.pdf) |
| <img src="assets/capa3.png" width="90"> | **Livro 3 — Programando com IA** | Ferramentas de código com IA, hardware e IA local, AI-Driven Engineer, desenvolvimento seguro e Pull Requests, segurança cloud-first | [Baixar](livros/Livro3_Programando_com_IA.pdf) |
| <img src="assets/capa4.png" width="90"> | **Livro 4 — Engenharia de Software e Ciência da Computação** | Arquitetura e boas práticas, algoritmos, dados e recomendação, engenharia reversa e segurança | [Baixar](livros/Livro4_Engenharia_de_Software_e_Ciencia_da_Computacao.pdf) |
| <img src="assets/capa5.png" width="90"> | **Livro 5 — IA, Negócios e Sociedade** | Negócios, carreira e governança, profissões, propriedade intelectual, polêmicas da IA, redes sociais | [Baixar](livros/Livro5_IA_Negocios_e_Sociedade.pdf) |
| <img src="assets/capa6.png" width="90"> | **Livro 6 — Cultura, Comunidade e História** | Comunidades e open-source, Linux, preservação de games, história dos videogames, pioneiros da computação | [Baixar](livros/Livro6_Cultura_Comunidade_e_Historia.pdf) |

Os livros são independentes: comece por qualquer um. Para quem está começando do zero, a ordem sugerida é 1 → 2 → 3.

## Por dentro

- **Para começar**: cada capítulo e seção abre com uma explicação para leigos.
- **Você sabia?**: curiosidades técnicas e os grandes nomes da tecnologia.
- **Fontes**: vídeos citados pelo título com link, e tabelas de fontes com URL completa.
- **Datas**: preços, planos e benchmarks refletem out/2026 e trazem a data de verificação.

## Gerar os PDFs a partir do código-fonte

```bash
pip install weasyprint
cd fonte
python build_vols.py        # gera os 6 livros em livros/
python build_vols.py 3      # gera só o Livro 3
```

Os capítulos estão em `fonte/capitulos/` (HTML) e as figuras em `fonte/img/`.

## Créditos

Esta coleção só existe graças a quem compartilha conhecimento gratuitamente. Obrigado a todos os autores abaixo. Os vídeos são citados pelo título, com link, ao longo dos livros, e cada capítulo traz a tabela completa de fontes.

### 🇧🇷 Criadores brasileiros

- [Augusto Galego](https://www.youtube.com/@GutoGalego)
- [Fernanda Kipper](https://www.youtube.com/@kipperdev)
- [Renato Augusto](https://www.youtube.com/@RenatoAugustoTech)
- [Attekita Dev](https://www.youtube.com/@attekitadev)
- [Área Tech Brasil](https://www.youtube.com/@areatechbrasil)
- [O Novo Programador](https://www.youtube.com/@ONovoProgramador)
- [ViktorKav](https://www.youtube.com/@VKav)
- [Ratos de IA](https://www.youtube.com/@ratosdeia)
- [Código Fonte TV](https://www.youtube.com/@codigofontetv)
- [Matheus Battisti - Hora de Codar](https://www.youtube.com/@MatheusBattisti)
- [IA em 6 minutos](https://www.youtube.com/@iaem6minutos)
- [Azev • Renda Online com IA](https://www.youtube.com/@azev300)
- [Anwar Hermuche | Engenheiro de IA](https://www.youtube.com/@anwarhermuche)
- [Waldemar Neto - Dev Lab](https://www.youtube.com/@WaldemarNetoDevLab)
- [Ronnald Hawk | Engenharia de IA](https://www.youtube.com/@ronnaldhawk)
- [Gabriel Kendy](https://www.youtube.com/@gabrielkendyia)
- [Sujeito programador](https://www.youtube.com/@Sujeitoprogramador)
- [Azevedo - Academy](https://www.youtube.com/@Azevedo.Academy)
- [Dev Aprender | Jhonatan de Souza](https://www.youtube.com/@DevAprender)
- [Daniel Bergholz](https://www.youtube.com/@DanielBergholzBR)
- [Fabio Akita — AkitaOnRails](https://akitaonrails.com/): posts sobre benchmarks de LLMs, IA local e programação com agentes

### 🌎 Criadores e instituições internacionais

- [IBM Technology](https://www.youtube.com/@IBMTechnology)
- [Anthropic](https://www.youtube.com/@anthropic-ai)
- [CS50](https://www.youtube.com/@cs50)
- [Corey McClain](https://www.youtube.com/@iamcoreymcclain)
- [Deep Tech with Amir Husain](https://www.youtube.com/@DeepTechWithAmir)
- [freeCodeCamp.org](https://www.youtube.com/@freecodecamp)
- [KodeKloud](https://www.youtube.com/@KodeKloud)
- [Tina Huang](https://www.youtube.com/@TinaHuang1)
- [David Ondrej](https://www.youtube.com/@DavidOndrej)
- [aiTrends](https://www.youtube.com/@aiTrends-channel)
- [Jorge Marfil](https://www.youtube.com/@Jorge_Marfil)

### Artigos, pesquisas e documentação

- **Anthropic**: *Effective context engineering for AI agents* e pesquisas de engenharia ([anthropic.com](https://www.anthropic.com/engineering))
- **Patrick Lewis et al. (2020)**: *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* ([arXiv](https://arxiv.org/abs/2005.11401))
- **Polo Club of Data Science, Georgia Tech**: [CNN Explainer](https://poloclub.github.io/cnn-explainer/)
- **TensorFlow Blog**: *Simulated Spotify* (recomendação com aprendizado por reforço)
- **Databricks Blog**: *How to Build an Online Recommendation System*
- **Notable Capital**: *The Anatomy of a Neural Network*
- **Pierre Rouhard (Medium)**: *Introduction to TensorFlow.js*
- **DataCamp**: *Deep Learning vs Machine Learning*
- **Simon Willison**, **Andrej Karpathy**, **METR**, **Video Game History Foundation**, **Stack Overflow**, **GitHub (Octoverse)**, **WEF**, **OIT**, **Stanford SIEPR** e os demais artigos, leis e reportagens listados nas tabelas de fontes de cada capítulo
- **Wikimedia Commons**: fotos históricas de consoles, computadores e pioneiros, com autor e licença indicados em cada legenda

> Os vídeos, artigos e posts pertencem aos respectivos autores. Os livros reorganizam e comentam esse conhecimento com texto próprio e sempre apontam para as fontes originais. Se você é autor de alguma referência e quer ajustar um crédito, abra uma *issue*.

## Licença

Texto e figuras próprias: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt_BR). As fotos do Wikimedia Commons mantêm as licenças indicadas nas legendas. Vídeos, artigos e posts citados pertencem aos respectivos autores.

O conceito **AI-Driven Engineer** descrito no PDF é experimental, e foi proposto por mim. ([@marcusbsilva](https://github.com/marcusbsilva)).
