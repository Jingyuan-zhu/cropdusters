## Cropdusters

<div align="center">
<br />

[![license](https://img.shields.io/github/license/dec0dOS/amazing-github-template.svg?style=flat-square)](LICENSE)

[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/dec0dOS/amazing-github-template/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![made with hearth by dec0dOS](https://img.shields.io/badge/made%20with%20%E2%99%A5%20by-dec0dOS-ff1414.svg?style=flat-square)](https://github.com/dec0dOS)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [Cookiecutter template](#cookiecutter-template)
    - [Variables reference](#variables-reference)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

<table>
<tr>
<td>

Cropdusters project contains three main models with the following functionalities:
- Suggest ideal crop types based on location
- Predict end of season yields
- Calculate sale price based on historical data
This is all provided as we work to provide a useful modeling solution for smallholder farms who do not have the means to access such envrionmental consulting as the big players and allow them to make the best choices for thier financies, their communities, and themsevles. This is a work in progress, please feel free to open a pull request adding functionality along the lines of what is described. 

<details open>
<summary>Additional info</summary>
<br>

No additional info.

</details>

</td>
</tr>
</table>

## Getting Started

### Prerequisites

All the requirements and dependandies are specified in the pyproject.toml, please consult that when setting up your envrionment to properly run this project.

The easiest way to install any package is by running:

```sh
pip install [package_name]
```
If any package needs to be updated, run:

```sh
pip update [package_name]
```

### Usage

#### Cookiecutter template

We reccomend use of the Cookiecutter template for new installations of the project. After installing Cookiecutter, all you need to do is to run the following command:

```sh
cookiecutter gh:wustl-data/cropdusters_PR2
```

You will get an interactive prompt where you'll specify relevant options for your project (or the default value will be used). 
*NOTE* you will require properly setup permissions for the wustl-data organization in order to install using cookiecutter. The number of dependancies has been kept light to ensure an easy installation using pip or the package manager of your choice is a simple task. 


#### Variables reference

Please note that entered values are case-sensitive.
Default values are provided as an example to help you figure out what should be entered.

> On manual setup, you need to replace only values written in **uppercase**.

| Name                       | Default value      | Description                                                                 |
| -------------------------- | ------------------ | --------------------------------------------------------------------------- |
| PROJECT_NAME               | cropdusters        | The project name                                                            |
| REPO_SLUG                  | cropdusters_PR2    | URL slug within the wustl-data organization                                 |
| GITHUB_USERNAME            | JackWeitzner       | Corrosponding maintainer                                                    |
| FULL_NAME                  | Anton Young        | Corrosponding maintainer                                                    |
| FULL_NAME                  | Jingyuan Zhu       | Corrosponding maintainer                                                    |
| FULL_NAME                  | Jack Weitzner      |                                                                             |
| OPEN_SOURCE_LICENSE        | MIT license        | Copyright (c) 2023, WUSTL Data Wrangling                                    |

## Roadmap

See the [open issues](https://github.com/wustl-data/cropdusters_PR2/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/wustl-data/cropdusters_PR2/labels/enhancement) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/wustl-data/cropdusters_PR2/labels/bug) (Add your votes using the 👍 reaction)
- [Questions](https://github.com/wustl-data/cropdusters_PR2/labels/question)

## Contributing

First off, thanks for taking the time to contribute! Contributions are what makes projects like this possible. Any contributions you make will benefit the family farms we are focused on helping and are **greatly appreciated**.

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.

## Acknowledgements

*Thanks to everyone who contributed to this project including the origional maintainers:*
<br> Jack Weitzner (@JackWeitzner), Anton Young (@antonryoung02), and Jingyuan Zhu (@Jingyuan-zhu). 

<br>
Special thanks also to @schlich who led the course under which this project was developed. Your time spent reviewing our issues and providing helpful pull requests has made this project possible. 
