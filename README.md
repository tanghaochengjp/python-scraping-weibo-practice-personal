# python-scraping-weibo-practice
A Python web scraping script for personal data collection（weibo version）

## 中文（CHINESE）

### 项目说明

这是一个用于**个人学习和 Python 编程练习**的小项目。

主要目的是练习：

* Python 基础语法
* 浏览器自动化
* 简单网页数据读取
* JSON 数据处理
* CSV 文件保存

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

## 免责声明

**本项目仅用于个人练习、编程练习和技术学习。**

本项目并非用于非法爬虫、商业数据采集、大规模自动化抓取或绕过网站安全机制。

使用本项目时，请遵守：

* 微博及其他目标网站的服务条款
* 网站的访问规则和技术限制
* 相关法律法规
* 个人信息和隐私保护要求
* 内容版权及其他第三方权利

本程序不用于绕过验证码、安全验证、登录限制、访问频率限制或其他网站保护措施。

如果网站出现验证码、安全验证或访问限制，应停止程序，并通过正常方式处理。

请合理控制访问频率，避免给网站服务器造成额外负担。

使用者应自行判断数据的合法使用范围，并自行承担运行或修改本程序产生的风险。

---

# English（英文）

## About This Project

This is a small project created for **personal learning and Python programming practice**.

The main purpose is to practice:

* Basic Python programming
* Browser automation
* Basic webpage data extraction
* JSON processing
* CSV file output

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

## Disclaimer

**This project is provided solely for personal learning, programming practice, and technical study.**

It is not intended for illegal scraping, commercial data collection, large-scale automated crawling, or bypassing website security mechanisms.

Users are responsible for complying with:

* The target website's Terms of Service
* Website access rules and technical restrictions
* Applicable laws and regulations
* Privacy and personal-data protection requirements
* Copyright and other third-party rights

This project is not intended to bypass CAPTCHAs, security verification systems, login restrictions, rate limits, or other technical protection measures.

If the website displays a CAPTCHA, security verification request, or access restriction, the program should be stopped and the issue should be handled through normal authorized methods.

Users should keep access frequency reasonable and avoid placing unnecessary load on website servers.

Users are responsible for determining whether their use of collected data is lawful and appropriate, and they assume responsibility for risks arising from running or modifying this project.
