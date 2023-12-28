# Big Data Analytics and Cloud Computing (PPOL 5206) Spring 2024 <a href='https://aa1603.georgetown.edu/ppol5206/'><img src='files/icon-512.png' align="right" height="139" /></a>

[PPOL 5206 • Spring 2024](https://aa1603.georgetown.edu/ppol5206/)  
[Amit Arora](https://www.linkedin.com/in/amit-arora-539120a/) • McCourt School of Public Policy • Georgetown University

------------------------------------------------------------------------

## How to build the site

1. Clone this repository.

1. Install [RStudio](https://www.rstudio.com/products/rstudio/download/#download) version 2022.07.1 or later since it has a [Quarto](https://quarto.org/) installation embedded in it. Otherwise, download and install [Quarto](https://quarto.org/) separately.

1. Install [VSCode](https://code.visualstudio.com/download).

1. Open the folder for this repository in VSCode.

1. Create a [Python virtual environment](https://code.visualstudio.com/docs/python/environments) for running the Python code in this repository. VSCode will automatically recognize the virtual environment and associate it with this repository's workspace so you would not have to manually activate the virtual environment every time you open this repository in VSCode.

1. To only render an individual `.qmd` file that you are working on click the `Render` button from the top right corner of the VSCode window. You would see a command line in the VSCode Terminal, and the website should render locally in your browser.  

1. You can do the same with the [`index.qmd`](index.qmd) file to render the entire website locally, but this has a problem, it will not render the slides as slides but as regular Quarto documents (which may be fine if you are not testing the slides).

1. To render the entire website locally (and avoid the problem with the slides not rendering correctly) run the `quarto render` command. This will re-build the entire website and the site will be available in the [`_site`](_site) folder. ***This is the recommended way for building and testing the entire site***.

1. Once the website is rendered locally you can take the contents of the [`_site`](_site) folder and upload it to your website. This website is currently hosted on [Georgetown Domains](https://georgetown.domains) and for now I manually SCP the contents to Georgetown Domains using WinSCP.

## Licenses

**Text and figures:** All prose and images are licensed under Creative
Commons ([CC-BY-NC
4.0](https://creativecommons.org/licenses/by-nc/4.0/))

**Code:** All code is licensed under the [MIT License](LICENSE).
