const toggle=document.querySelector('.menu-toggle');const menu=document.querySelector('#navigation');
toggle?.addEventListener('click',()=>{const expanded=toggle.getAttribute('aria-expanded')==='true';toggle.setAttribute('aria-expanded',String(!expanded));menu.classList.toggle('is-open',!expanded)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.classList.contains('is-open')){menu.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');toggle.focus()}});
const form=document.querySelector('#enquiry');
if(form){const selected=new URLSearchParams(location.search).get('service');const options=[...form.querySelectorAll('input[name="service"]')];const match=options.find(input=>input.value===selected);if(match)match.checked=true;
form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const values=new FormData(form);const name=String(values.get('name')).trim();const email=String(values.get('email')).trim();const service=String(values.get('service'));const body=`Hi Tawfeeqoh,\n\nI'm ${name}. I'd like to discuss ${service.toLowerCase()}.\n\n${String(values.get('message')).trim()}\n\nBudget: ${values.get('budget')}\nTimeline: ${String(values.get('timeline')).trim()||'Flexible / to discuss'}\n\nMy email: ${email}\n\n${name}`;
const uri=`mailto:hello@tawfeeqoh.name.ng?subject=${encodeURIComponent('Project enquiry: '+service)}&body=${encodeURIComponent(body)}`;const result=document.querySelector('#enquiry-result');result.hidden=false;document.querySelector('#email-draft').href=uri;document.querySelector('#brief-output').value=body;location.href=uri;});
document.querySelector('#copy-brief').addEventListener('click',async()=>{const output=document.querySelector('#brief-output');const status=document.querySelector('#copy-status');try{await navigator.clipboard.writeText(output.value);status.textContent='Brief copied. Paste it into your email.'}catch{output.focus();output.select();status.textContent='Select and copy the brief below.'}});}

const mockupDialog=document.querySelector('.mockup-dialog');
if(mockupDialog){document.querySelectorAll('[data-open-mockup]').forEach(button=>button.addEventListener('click',()=>mockupDialog.showModal()));mockupDialog.querySelector('[data-close-mockup]').addEventListener('click',()=>mockupDialog.close());mockupDialog.addEventListener('click',event=>{if(event.target===mockupDialog){const bounds=mockupDialog.getBoundingClientRect();if(event.clientX<bounds.left||event.clientX>bounds.right||event.clientY<bounds.top||event.clientY>bounds.bottom)mockupDialog.close()}});mockupDialog.addEventListener('close',()=>{document.body.style.overflow=''});mockupDialog.addEventListener('toggle',()=>{document.body.style.overflow=mockupDialog.open?'hidden':''});}

// No video URL is assigned until a deliberate play action.
document.querySelectorAll('[data-play-video]').forEach(button=>{
 button.addEventListener('click',async()=>{
  const video=document.getElementById(button.dataset.playVideo);
  document.querySelectorAll('.video-shell video').forEach(other=>{if(other!==video)other.pause()});
  if(!video.src){video.src=video.dataset.src;video.load()}
  video.hidden=false;button.hidden=true;video.focus();
  const error=video.closest('.demo-media').querySelector('.video-error');
  video.addEventListener('error',()=>{error.hidden=false},{once:true});
  try{await video.play()}catch{error.hidden=false}
 });
});
document.querySelectorAll('.video-shell video').forEach(video=>{
 video.addEventListener('play',()=>document.querySelectorAll('.video-shell video').forEach(other=>{if(other!==video)other.pause()}));
});
