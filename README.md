# python-scraping-weibo-practice
A Python web scraping script for personal data collection（weibo version）
A simple Python-based data collection project demonstrating the approach I used during my undergraduate thesis research.

## 中文（CHINESE）

### 项目说明

本项目用于展示我在本科毕业论文研究过程中如何将 Python 应用于简单的数据收集，同时也是对 Python 编程和网页数据处理方法的一次实践整理。

我的本科毕业论文研究涉及网络公开信息的收集与后续数据分析。在这一过程中，我使用 Python 辅助完成部分数据获取与整理工作。

本仓库中的程序展示了一种简化的数据收集流程

程序会从微博搜索页面读取公开显示的信息，并保存：

* 发布时间
* 微博正文
* 原文链接

本项目仅用于个人学习和技术练习，不用于商业用途或大规模数据采集。

### 使用环境

* macOS
* Python 3
* Google Chrome
* AppleScript
* JavaScript

使用前需要：

1. 安装 Python 3 和 Google Chrome。
2. 正常登录微博。
3. 打开 Chrome。
4. 允许 Chrome 通过 Apple Events 执行 JavaScript。

### 输出

程序会生成 CSV 文件，例如：

```text
weibo_mydata_time_2023-2025.csv
```

CSV 中包含：

* 发布时间
* 原文正文
* 原文链接


# English（英文）

## About This Project

This is a small project created for **personal learning and Python programming practice**.
This repository presents a simplified implementation of the Python-based data collection approach I used during my undergraduate thesis research.

My undergraduate thesis involved the collection and subsequent analysis of publicly accessible online information. Python was used to assist with part of the data collection and organization process.

The program reads publicly visible information from Weibo search pages and saves:

* Publication time
* Post text
* Original post URL

This project is intended only for personal learning and technical practice. It is not designed for commercial or large-scale data collection.

## Environment

* macOS
* Python 3
* Google Chrome
* AppleScript
* JavaScript

Before running the program:

1. Install Python 3 and Google Chrome.
2. Log in to Weibo normally.
3. Keep a Chrome window open.
4. Allow JavaScript execution from Apple Events in Chrome.

## Output

The program generates a CSV file such as:

```text
weibo_mydata_time_2023-2025.csv
```

The CSV contains:

* Publication Time
* Post Text
* Original URL

## 详细使用规范与免责声明

本项目仅用于**个人学习、Python 编程练习和技术研究**。

本项目不是为非法爬虫、未经授权的数据采集、大规模自动化抓取、商业数据服务或规避网站安全机制而设计。

使用本项目的任何人均应自行确认其使用行为符合：

* 目标网站当前有效的服务条款、用户协议及平台规则；
* 网站设置的访问权限、访问频率和技术限制；
* 适用的法律法规；
* 个人信息、隐私和数据保护要求；
* 著作权及其他第三方合法权益。

本项目不用于绕过或规避：

* CAPTCHA 或验证码；
* 安全验证；
* 登录或身份验证限制；
* 访问频率限制；
* IP、账户或设备限制；
* 其他访问控制或技术保护措施。

如果目标网站出现验证码、安全验证、访问限制、异常访问提示或类似情况，应停止自动化操作，并通过网站提供的正常方式处理。

即使某些信息可以在网页上公开查看，也不代表这些信息可以被任意收集、保存、重新发布或用于其他目的。使用者应根据具体情况自行判断数据的合法和适当使用范围。

请合理控制访问频率，避免对目标网站服务器造成不必要的负担。

本项目按 **“AS IS（按现状）”** 提供。作者不保证程序能够持续正常运行，也不保证所获取数据的完整性、准确性或持续可用性。网站结构、访问规则及相关政策可能随时发生变化。

使用者应自行承担运行、修改和使用本项目所产生的风险，并对其数据获取、保存、使用、发布或共享行为负责。

在适用法律允许的范围内，作者不对因使用或修改本项目而产生的数据丢失、账户限制、访问限制或其他损失承担超出法律规定范围的责任。

本 README 中的内容仅用于说明项目用途和负责任使用原则，不构成法律意见。

---

## Responsible Use and Disclaimer

This project is intended solely for **personal learning, Python programming practice, and technical research**.

It is not designed for illegal scraping, unauthorized data collection, large-scale automated crawling, commercial data collection services, or circumvention of website security mechanisms.

Anyone using this project is responsible for ensuring that their use complies with:

* the current Terms of Service, user agreements, and policies of the target website;
* access permissions, rate limits, and technical restrictions imposed by the website;
* applicable laws and regulations;
* privacy and personal-data protection requirements; and
* copyright and other third-party rights.

This project is not intended to bypass or circumvent:

* CAPTCHAs;
* security verification systems;
* login or authentication restrictions;
* rate limits;
* IP, account, or device restrictions; or
* other access-control or technical-protection mechanisms.

If the target website displays a CAPTCHA, security verification request, access restriction, abnormal-access warning, or similar mechanism, automated activity should be stopped and the issue should be handled through the website's normal authorized process.

The fact that certain information is publicly visible on a webpage does not necessarily mean that it may be freely collected, stored, republished, or used for other purposes. Users are responsible for determining whether their intended use of collected data is lawful and appropriate.

Users should keep access frequency reasonable and avoid placing unnecessary load on the target website.

This project is provided **“AS IS.”** The author does not guarantee continued functionality, completeness or accuracy of collected data, or continued compatibility with the target website. Website structures, access rules, and policies may change at any time.

Users assume responsibility for the risks associated with running, modifying, or using this project and remain responsible for their own collection, storage, use, publication, or sharing of data.

To the extent permitted by applicable law, the author does not accept liability beyond what applicable law requires for data loss, account restrictions, access restrictions, or other losses arising from the use or modification of this project.

Nothing in this README constitutes legal advice.

## Copyright

Copyright © 2026 Tang Hao Cheng. All rights reserved.

No open-source license is granted for this repository.
This repository is made publicly available primarily for academic review,
personal learning, and portfolio demonstration.
