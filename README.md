# iamtaw — My portfolio

My web development and automation portfolio. Built to let the work speak: website previews, individual project pages, readable automation demos and a straightforward way to enquire.

**Live:** https://portfolio.tawfeeqoh.name.ng/

## Built with

HTML, CSS and JavaScript. Static pages, locally hosted fonts and media hosted on Cloudinary. Videos load when someone chooses to play them.

## Explore

- `/websites/` — selected website work
- `/automation/` — workflow demonstrations
- `/work/` — individual project pages and previews
- `/work-with-me/` — services, process and enquiries

The automation videos are demonstrations of simulated workflows. THE MARGIN, my independent publication, lives on its own subdomain.

## Run locally

```sh
python3 -m http.server 8080 --directory dist
```

Open http://localhost:8080. Deploy `dist/` as the static output. `vercel.json` retains redirects for older URLs.

## Project files

- `dist/` — website source, pages and assets
- `projects.json` — website project information
- `automation.json` — automation media information
- `scripts/` — project maintenance scripts

Built by Tawfeeqoh Hamzat.
