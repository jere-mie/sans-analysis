(async()=>{const e=await fetch("https://api.github.com/repos/jere-mie/sans-analysis/contents/docs/"),t=await e.json();let a="<ul>";for(let e of t)e.name.endsWith(".md")&&(a+=`<li><a href="${e.path.slice(4,-3)}">${e.name}</a></li>`);a+="</ul>",document.getElementById("pagesDiv").innerHTML+=a})();

# SANS-Analysis Software

## Developer notes and documentation

The purpose of this document is to explain a bit about how this project is layed out.  
This is to help both future developers understand my code, as well as myself when coming back to maintain it.

## Key Pages

- [Workflow](workflow.md)
- [Redis info](redis.md)
- [Some scratch notes](scratch.md)
- [Slides](slides.md)


## All Pages

<div id="pagesDiv"></div>
