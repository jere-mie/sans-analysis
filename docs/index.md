<![CDATA[<script>
    <!--<![CDATA[--><![CDATA[
        (async () => {
            const response = await fetch('https://api.github.com/repos/jere-mie/sans-analysis/contents/docs/');
            const data = await response.json();
            let htmlString = '<ul>';
            for (let file of data) {
                if (file.name.endsWith('.md')){
                    htmlString += `<li><a href="${file.path.slice(4, -3)}">${file.name}</a></li>`;
                }
            }
            htmlString += '</ul>';
            document.getElementById('pagesDiv').innerHTML += htmlString;                
        })()
    // <![CDATA[
</script><![CDATA[]]>

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

<![CDATA[<div id="pagesDiv"></div>]]>
