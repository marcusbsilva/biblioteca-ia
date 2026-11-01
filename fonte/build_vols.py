import re,sys
from weasyprint import HTML
VOLS=[
 ("Livro 1","Fundamentos de IA e Modelos de Linguagem","Do que é inteligência artificial e aprendizado de máquina até como funcionam os grandes modelos de linguagem, Transformers, Mistura de Especialistas e LoRA.",["01","02"]),
 ("Livro 2","Construindo com LLMs","Como conversar com qualquer IA, engenharia de contexto, RAG e agentes com MCP: o essencial para criar soluções com modelos de linguagem.",["13","03","04","05"]),
 ("Livro 3","Programando com IA","Ferramentas de programação com IA, hardware e IA local, o conceito AI-Driven Engineer, desenvolvimento seguro, Pull Requests e segurança cloud-first.",["06","07","14","15","22"]),
 ("Livro 4","Engenharia de Software e Ciência da Computação","Arquitetura e boas práticas, algoritmos e estruturas de dados, dados e sistemas de recomendação, engenharia reversa e segurança.",["08","09","10","11"]),
 ("Livro 5","IA, Negócios e Sociedade","Negócios, carreira e governança, o futuro das profissões, propriedade intelectual, as polêmicas da IA e o impacto das redes sociais.",["12","17","18","21","23"]),
 ("Livro 6","Cultura, Comunidade e História","Comunidades e open-source, Linux, a preservação dos games, a história dos videogames e os pioneiros da computação.",["19","16","20","24"]),
]
css=open('style.css').read()
def fix_tables(h):
    def one(m):
        t=m.group(0); rows=t.count('<tr')
        if 'class="src"' in t:
            t=re.sub(r'<table class="src">\s*(<tr>.*?</tr>)',lambda k:'<table class="src"><colgroup><col style="width:34%"><col style="width:26%"><col style="width:13%"><col style="width:27%"></colgroup><thead>'+k.group(1)+'</thead>',t,count=1,flags=re.S)
        elif rows<=14 and t.startswith('<table>'): t='<table class="short">'+t[7:]
        return t
    return re.sub(r'<table[^>]*>.*?</table>',one,h,flags=re.S)
def clean(c,k):
    c=re.sub(r'<span class="num">Capítulo \d+\s*·?\s*</span>',f'<span class="num">Capítulo {k} · </span>',c,count=1)
    c=re.sub(r'(<h[23][^>]*>)\s*\d+(\.\d+)*\.?\s+',r'\1',c)
    c=re.sub(r'Figura \d+[A-Za-z0-9]*\.\d+\s*[—–-]\s*','',c)
    return fix_tables(c)
only=sys.argv[1:] 
for vi,(vl,title,desc,chs) in enumerate(VOLS,1):
    if only and str(vi) not in only: continue
    cs=[clean(open(f'capitulos/{n}.html',encoding='utf-8').read(),k) for k,n in enumerate(chs,1)]
    ts=[re.sub('<[^>]+>','',re.search(r'<h1>.*?</span>(.*?)</h1>',c,re.S).group(1)) for c in cs]
    ids=[re.search(r'<section class="chapter" id="([^"]+)"',c).group(1) for c in cs]
    toc=''.join(f'<li><a href="#{i}">{k}. {t}</a></li>' for k,(i,t) in enumerate(zip(ids,ts),1))
    others=''.join(f'<li>{a} — {b}</li>' for a,b,_,_ in VOLS)
    html=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>{vl} — {title}</title><style>{css}</style></head><body>
<div class="cover"><div class="ct">BIBLIOTECA IA, SOFTWARE &amp; COMPUTAÇÃO · {vl.upper()}</div><h1 class="title">{title}</h1><p class="sub">{desc}</p><p class="date">Edição de outubro de 2026</p></div>
<section class="front"><h1>Sobre esta coleção</h1>
<div class="box intro"><b>Para começar</b> Esta coleção explica inteligência artificial, desenvolvimento de software e computação do zero. Cada capítulo começa em linguagem simples, com analogias do dia a dia, e aprofunda aos poucos. Os livros podem ser lidos separadamente.</div>
<p>O conteúdo reorganiza o que ensinam centenas de aulas e vídeos (do CS50 de Harvard a canais como IBM Technology, Anthropic e muitos outros), artigos técnicos de referência e o blog <a href="https://akitaonrails.com/">AkitaOnRails</a>, complementados com pesquisa atualizada. Os vídeos aparecem pelo título, com link; cada capítulo termina com a tabela de fontes. Caixas <i>Você sabia?</i> trazem curiosidades e grandes nomes da tecnologia.</p>
<h2>Os livros da coleção</h2><ol class="vols">{others}</ol>
<div class="box warn"><b>Datas</b> IA muda depressa. Preços, planos, benchmarks e nomes de modelos refletem outubro de 2026. Figuras marcadas como "ilustrativas" mostram a ideia, não medições.</div></section>
<nav class="toc"><h1>Sumário</h1><ol>{toc}</ol></nav>
{''.join(cs)}</body></html>'''
    open(f'vol{vi}.html','w',encoding='utf-8').write(html)
    name=f"Livro{vi}_"+re.sub(r'[^A-Za-z0-9]+','_',__import__('unicodedata').normalize('NFKD',title).encode('ascii','ignore').decode()).strip('_')+'.pdf'
    HTML(f'vol{vi}.html',base_url='.').write_pdf('../livros/'+name); print(name)
