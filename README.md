<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">EDGES-WEB</h1>
</p>
<p align="center">
    <em><code>► RESEARCH INFORMATION SYSTEM</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/vat1kan/edges-web?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/vat1kan/edges-web?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/vat1kan/edges-web?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/vat1kan/edges-web?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

This web application leverages the power of advanced neural networks, specifically HED (Holistically-Nested Edge Detection) and PiDiNet, to perform cutting-edge image processing tasks. Designed to cater to both enthusiasts and professionals in the field of computer vision, this app provides an intuitive interface for performing edge detection, adding synthetic noise, and calculating various performance metrics on images.

---

##  Features

► <b>Edge Detection</b>: Utilize the HED model for state-of-the-art edge detection, providing crisp and detailed edges in a variety of images.<br>
► <b>Noise Addition</b>: Integrate noise into images to simulate different conditions and test the robustness of image processing algorithms using our custom noise injection feature.<br>
► <b>Metric Calculation</b>: Evaluate the performance of edge detection and noise addition processes with built-in metrics, including precision, recall, and F1 score and FOM (Pratt Criteria)<br>
► <b>PiDiNet</b> Integration: Leverage the PiDiNet model for enhanced edge detection capabilities, especially in challenging visual scenarios. The network architecture used is the one that was presented by the [research team](https://github.com/hellozhuo/pidinet). The network has been restructured to allocate contours of only user pictures. The model can be replaced with any other model by placing it in the [/pidinet/trained_models](https://github.com/vat1kan/edges-web/tree/main/pidinet/trained_models) folder.

---

##  Repository Structure

```sh
└── edges-web/
    ├── app.py
    ├── HED
    │   ├── hed_edges.py
    │   └── model
    ├── pidinet
    │   ├── getEdges.py
    │   ├── LICENSE
    │   ├── models
    │   ├── trained_models
    │   └── utils.py
    ├── requirements.txt
    ├── static
    │   ├── 404_icon.png
    │   ├── 500_icon.png
    │   ├── background.gif
    │   ├── cnn.gif
    │   ├── favicon.ico
    │   ├── git.gif
    │   ├── hed.png
    │   ├── pidinet.png
    │   ├── scripts.js
    │   └── styles.css
    ├── templates
    │   ├── 404.html
    │   ├── about.html
    │   ├── form.html
    │   ├── index.html
    │   ├── layout.html
    │   ├── result.html
    │   └── traceback.html
    └── tools.py
```

---

##  Modules

| File                                                                                  | Summary                         |
| ---                                                                                   | ---                             |
| [app.py](https://github.com/vat1kan/edges-web/blob/master/app.py)                     | <code>► Main Flask file to handle request</code> |
| [requirements.txt](https://github.com/vat1kan/edges-web/blob/master/requirements.txt) | <code>► A list of needed libraries</code> |
| [tools.py](https://github.com/vat1kan/edges-web/blob/master/tools.py)                 | <code>► Auxiliary file for function calls </code> |

</details>

<details closed><summary>HED</summary>

| File                                                                              | Summary                         |
| ---                                                                               | ---                             |
| [hed_edges.py](https://github.com/vat1kan/edges-web/blob/master/HED\hed_edges.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>HED.model</summary>

| File                                                                                          | Summary                         |
| ---                                                                                           | ---                             |
| [deploy.prototxt](https://github.com/vat1kan/edges-web/blob/master/HED\model\deploy.prototxt) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pidinet</summary>

| File                                                                                | Summary                         |
| ---                                                                                 | ---                             |
| [getEdges.py](https://github.com/vat1kan/edges-web/blob/master/pidinet\getEdges.py) | <code>► INSERT-TEXT-HERE</code> |
| [utils.py](https://github.com/vat1kan/edges-web/blob/master/pidinet\utils.py)       | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pidinet.models</summary>

| File                                                                                                     | Summary                         |
| ---                                                                                                      | ---                             |
| [config.py](https://github.com/vat1kan/edges-web/blob/master/pidinet\models\config.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [convert_pidinet.py](https://github.com/vat1kan/edges-web/blob/master/pidinet\models\convert_pidinet.py) | <code>► INSERT-TEXT-HERE</code> |
| [ops.py](https://github.com/vat1kan/edges-web/blob/master/pidinet\models\ops.py)                         | <code>► INSERT-TEXT-HERE</code> |
| [pidinet.py](https://github.com/vat1kan/edges-web/blob/master/pidinet\models\pidinet.py)                 | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>templates</summary>

| File                                                                                        | Summary                         |
| ---                                                                                         | ---                             |
| [404.html](https://github.com/vat1kan/edges-web/blob/master/templates\404.html)             | <code>► INSERT-TEXT-HERE</code> |
| [about.html](https://github.com/vat1kan/edges-web/blob/master/templates\about.html)         | <code>► INSERT-TEXT-HERE</code> |
| [form.html](https://github.com/vat1kan/edges-web/blob/master/templates\form.html)           | <code>► INSERT-TEXT-HERE</code> |
| [index.html](https://github.com/vat1kan/edges-web/blob/master/templates\index.html)         | <code>► INSERT-TEXT-HERE</code> |
| [layout.html](https://github.com/vat1kan/edges-web/blob/master/templates\layout.html)       | <code>► INSERT-TEXT-HERE</code> |
| [result.html](https://github.com/vat1kan/edges-web/blob/master/templates\result.html)       | <code>► INSERT-TEXT-HERE</code> |
| [traceback.html](https://github.com/vat1kan/edges-web/blob/master/templates\traceback.html) | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the edges-web repository:
>
> ```console
> $ git clone https://github.com/vat1kan/edges-web
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd edges-web
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run edges-web using the command below:
> ```console
> $ python main.py
> ```


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/vat1kan/edges-web/issues)**: Submit bugs found or log feature requests for the `edges-web` project.
- **[Submit Pull Requests](https://github.com/vat1kan/edges-web/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/vat1kan/edges-web/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/vat1kan/edges-web
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/vat1kan/edges-web/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=vat1kan/edges-web">
   </a>
</p>
</details>

---

##  License

This project is protected under the [GNU General Public License v3.0]. For more details, refer to the [LICENSE](https://spdx.org/licenses/GPL-3.0-or-later.html) file.

---

[**Return**](#-overview)


