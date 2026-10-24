from pathlib import Path
from PIL import Image
import json,re,html
r=Path('/workspace/sites/iamtaw-portfolio');d=r/'dist';uploads=Path('/workspace/scratch/ed3c693fe4a3/upload')
data=[
('solitude','Solitude Apartments','01-Solitude-Apartments-UI-Portfolio-Mockup.png','Hospitality','A quieter approach to a city stay.','https://solitude-apartments-taw.vercel.app','Deep green, warm cream and generous photography make the apartments the focus. The pages move from discovering the spaces to choosing a stay.'),
('triptick','Triptick Logistics','02-1001375988.png','Logistics','Parcel dispatch for people and businesses.','https://triptick-logistics-taw.vercel.app','The opening explains the service straight away. Booking, parcel information and the business offering each have their own place in the page.'),
('make-me','Make Me Beauty Place','03-1001376002.png','Beauty','A salon website in black and gold.','https://makemebeauty-seven.vercel.app','Hair photography leads the design. Service cards, a gallery and appointment prompts give visitors different ways to explore the salon.'),
('zeste','ZestéFoods','04-1001375968.png','Food','Food, meal plans and everyday ordering.','https://zeste-foods-taw.vercel.app','The food appears early and often. Meal choices and plans are presented in separate sections, with clear routes towards the next step.'),
('aylustre','Aylustre Expressions','05-1001375975.png','Beauty','Bridal beauty and training.','https://aylustre-expressions-taw.vercel.app','Cobalt blue type and close-up photography give the pages a strong identity. Bridal services and training are presented as two distinct parts of the offering.'),
('dear-didi','Dear Didi Beauty','06-1001375987.png','Beauty','A bridal makeup portfolio.','https://dear-didi-beauty-taw.vercel.app','The layout gives the makeup work room to speak. Warm neutrals frame the portfolio, while services and enquiries are kept easy to find.'),
('ori','ORÍ','07-1001375962.png','Beauty','Hair services and a booking interaction.','https://ori-studio-taw.vercel.app','The salon concept pairs an editorial layout with a filterable service menu and booking preview. It is a frontend demonstration, not a live appointment system.'),
('topcars','Topcars Abuja','08-1001375972.png','Automotive','Vehicle discovery and dealer enquiries.','https://topcars-abuja-taw.vercel.app','A dark palette and lime accents frame the cars. The page connects vehicle discovery with purchase and selling enquiries.'),
('apricot','Apricot Apartments','09-1001375971.png','Hospitality','A city stay, with room to explore.','https://apricot-apartments-taw.vercel.app','The apartment catalogue and location choices do most of the explaining. Warm colours, spacious layouts and interior photography keep the focus on the stay.')]
projects=[]
for slug,name,filename,sector,summary,url,description in data:
 im=Image.open(uploads/filename).convert('RGB');im.thumbnail((1440,1440));w,h=im.size
 im.save(d/'assets'/f'{slug}-mockup.webp','WEBP',quality=87,method=6)
 projects.append(dict(slug=slug,name=name,source_filename=filename,sector=sector,summary=summary,url=url,description=description,width=w,height=h))
(r/'projects.json').write_text(json.dumps(projects,ensure_ascii=False,indent=2))

def card(p,i):
 n=html.escape(p['name']);slug=p['slug'];url=p['url']
 return f'''<article class="project project-{slug} has-mockup" data-category="Websites"><a class="project-art" href="/work/{slug}/" aria-label="View {n} project">View {n} project</a><div class="project-caption"><div><p class="eyebrow">{p['sector']} / Website</p><h3><a href="/work/{slug}/">{n}</a></h3></div><p>{p['summary']}</p></div><div class="project-actions"><a class="text-link" href="{url}" target="_blank" rel="noopener">Visit website <span class="sr-only"> (opens in a new tab)</span></a><a class="project-details" href="/work/{slug}/">View project</a></div></article>'''
# Retain the existing Graceyy entry, and replace ORÍ with the supplied mockup.
workpath=d/'work/index.html';work=workpath.read_text();oldcards=re.findall(r'<article class="project .*?</article>',work,re.S)
retained=[c for c in oldcards if 'project-graceyy' in c]
allcards=''.join(card(p,i) for i,p in enumerate(projects))+''.join(retained)
work=re.sub(r'(<div class="project-grid">).*?(</div></section>)',lambda m:m[1]+allcards+m[2],work,count=1,flags=re.S)
work=work.replace('All work <sup>03</sup>','All work <sup>11</sup>').replace('Websites <sup>02</sup>','Websites <sup>10</sup>')
work=work.replace('Original concepts are labelled throughout.<br>Each case study explains the scope and approach.','Explore each project or open its website.<br>Mockups show selected pages from the work.')
workpath.write_text(work)
# Five features provide variety while keeping the homepage focused.
homepath=d/'index.html';home=homepath.read_text();featured=['solitude','topcars','make-me','triptick','aylustre'];by={p['slug']:p for p in projects}
selected=''.join(card(by[s],i) for i,s in enumerate(featured))
home=re.sub(r'(<div class="project-grid">).*?(</div><a class="text-link" href="/websites/">)',lambda m:m[1]+selected+m[2],home,count=1,flags=re.S)
# Leave the hero screenshot composition intact; it links to the updated ORÍ project.
homepath.write_text(home)
# Use the current page chrome so the new pages share navigation, footer and branding.
base=(d/'work/graceyy/index.html').read_text()
for p in projects:
 n=html.escape(p['name']);slug=p['slug'];kind='Original portfolio concept' if slug=='ori' else 'Website portfolio'
 content=f'''<section class="case-intro wrap"><a class="text-link" href="/websites/">← Back to work</a><p class="eyebrow">{p['sector']} / {kind}</p><h1>{n}<em>.</em></h1><p class="case-sub">{p['summary']}</p><div class="case-top-actions"><a class="button" href="{p['url']}" target="_blank" rel="noopener">Visit website</a><button class="text-link" type="button" data-open-mockup>Enlarge mockup</button></div></section><figure class="case-image mockup-figure wrap"><button class="mockup-zoom" type="button" data-open-mockup aria-label="Enlarge {n} mockup"><img src="/assets/{slug}-mockup.webp" width="{p['width']}" height="{p['height']}" alt="{n} website mockup showing selected page layouts"></button><figcaption>Selected page layouts / {n} · Tap the mockup to enlarge</figcaption></figure><section class="case-story wrap"><div><p class="eyebrow">The project</p><h2>{p['sector']}<br><em>on the web.</em></h2></div><p>{p['description']}</p></section><section class="case-end wrap"><p class="small">This mockup presents selected page layouts. Visit the website to explore the implemented experience.</p><a class="button" href="{p['url']}" target="_blank" rel="noopener">Open {n} on Vercel</a><p class="small"><a class="text-link" href="/websites/">Explore more projects</a></p></section><dialog class="mockup-dialog" aria-labelledby="mockup-title"><div class="mockup-toolbar"><h2 id="mockup-title">{n}</h2><button type="button" data-close-mockup aria-label="Close enlarged mockup">Close ×</button></div><div class="mockup-scroll"><img src="/assets/{slug}-mockup.webp" width="{p['width']}" height="{p['height']}" alt="Enlarged {n} website mockup"></div><a href="{p['url']}" target="_blank" rel="noopener">Visit website</a></dialog>'''
 s=re.sub(r'<main id="main">.*?</main>',lambda m:'<main id="main">'+content+'</main>',base,count=1,flags=re.S)
 s=re.sub(r'<title>.*?</title>',lambda m:f'<title>{n} | iamtaw — Tawfeeqoh Hamzat</title>',s,count=1)
 s=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="https://portfolio.tawfeeqoh.name.ng/work/{slug}/">',s)
 out=d/'work'/slug/'index.html';out.parent.mkdir(exist_ok=True);out.write_text(s)
css=d/'style.css';s=css.read_text();s+='''
/* Portfolio mockups retain their complete composition. */
.project.has-mockup .project-art,.project.has-mockup:first-child .project-art{padding:0;background:transparent;border-radius:3px}.project.has-mockup .project-art img{width:100%;height:auto;box-shadow:none}.project-actions{display:flex;justify-content:space-between;align-items:center;gap:24px;margin-top:18px;border-top:1px solid var(--line);padding-top:8px}.project-actions .text-link{font-size:14px;border:0}.project-details{font-size:13px;text-decoration:underline;text-underline-offset:4px}.project-caption h3{font-size:clamp(26px,2.7vw,36px)}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap}.case-top-actions{display:flex;align-items:center;flex-wrap:wrap;gap:24px;margin-top:28px}.mockup-figure{background:transparent;padding-block:20px}.mockup-figure figcaption{color:var(--ink)}.mockup-zoom{display:block;border:0;padding:0;width:100%;background:transparent;cursor:zoom-in}.mockup-dialog{width:min(1500px,96vw);max-width:96vw;max-height:94dvh;padding:20px;border:0;background:var(--cream);color:var(--ink);overflow:auto}.mockup-dialog::backdrop{background:#211b29df}.mockup-toolbar{display:flex;align-items:center;justify-content:space-between;gap:20px;position:sticky;top:-20px;background:var(--cream);padding-block:15px;z-index:1}.mockup-toolbar h2{font-size:23px;letter-spacing:-.04em}.mockup-toolbar button{background:var(--mulberry);color:var(--cream);border:0;border-radius:30px;padding:10px 18px;min-height:44px}.mockup-scroll{overflow:auto}.mockup-scroll img{min-width:900px;width:100%;height:auto}.mockup-dialog>a{display:inline-block;font-size:14px;padding:15px 0;min-height:44px}@media(max-width:720px){.mockup-dialog{padding:12px}.mockup-toolbar{top:-12px}.mockup-toolbar h2{font-size:18px}.project-actions{margin-top:12px}.case-intro h1{font-size:clamp(48px,12vw,75px);overflow-wrap:break-word}.mockup-figure figcaption{font-size:11px}}
''';css.write_text(s)
js=d/'app.js';js.write_text(js.read_text()+'''
const mockupDialog=document.querySelector('.mockup-dialog');
if(mockupDialog){document.querySelectorAll('[data-open-mockup]').forEach(button=>button.addEventListener('click',()=>mockupDialog.showModal()));mockupDialog.querySelector('[data-close-mockup]').addEventListener('click',()=>mockupDialog.close());mockupDialog.addEventListener('click',event=>{if(event.target===mockupDialog){const bounds=mockupDialog.getBoundingClientRect();if(event.clientX<bounds.left||event.clientX>bounds.right||event.clientY<bounds.top||event.clientY>bounds.bottom)mockupDialog.close()}});mockupDialog.addEventListener('close',()=>{document.body.style.overflow=''});mockupDialog.addEventListener('toggle',()=>{document.body.style.overflow=mockupDialog.open?'hidden':''});}
''')
print('Added nine mockups, 10 gallery entries, five homepage features and nine project pages with website links.')
