
<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Nuke Python Tools</h3>

  <p align="center">
    Tools to speed up workflows and repetitive tasks!
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

During my time working on projects inside and outside of University, I found myself having to do the same repetitive tasks. either inside of my own scripts or other people's. I couldn't find any simplistic plugins to do what I wanted, so I made my own

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone or Download the repo
   ```sh
   git clone https://github.com/Danb106632/NukePythonTools.git
   ```
2. Move Dan'sToolkit to your .nuke folder.
   - Windows: C:\Users\USER\.nuke
   - Linux: /home/USER/.nuke

4. Update or add menu.py
   - If no menu.py exists in /.nuke, copy menu.py to /.nuke
   - If menu.py does exists, add the following command to the bottom of the file
     ```py
     nuke.pluginAddPath("Dan'sToolkit")
     ```
     
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Some of these command have keybinds. They can all be used and accessed from the Nodes Menu and the Tab Menu

1. WriteRead (Ctrl+R)
   - Select a Write Node and execute the command. A read node will be created underneath with the same write settings e.g. ColorTransform, Raw, AutoAlpha etc.
2. WriteReadReplace (Ctrl+Alt+R)
   - Does the same as WriteRead but replaces the write node
3. PostageReplace
   - Replaces duplicate Reads with PostageStamps
   1. Select the Read you want to get rid of duplicates of (will be used for PostageStamp connections)
   2. Run command
   3. Will be prompted for names for created PostageStamps. Make sure this is unique
   4. Reads will be deleted and replaced


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add option for NoOp's instead of PostageStamps to speed up performance
- [ ] Add support for other Read formats: 3D, Deep


<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Email  - daniel.beeching@outlook.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/daniel-beeching
