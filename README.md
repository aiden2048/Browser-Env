## Browser-Env
Web crawlers use the real browser environment.

本项目不重复造轮子, 而是对已有的开源项目进行封装和集成, 使其适用于复杂多样的 Spider 项目需求.

依赖要求:
Python 3.6+
selenium 3.4.0+
Chrome 浏览器应用版本 99+

本人实测的依赖版本:
selenium==4.0.0
selenium-wire==4.6.3
undetected-chromedriver==3.1.5.post4

# browserenv
基础的浏览器环境, 用于高度模拟 真实浏览器环境 执行js脚本
或对付 SecurityWorker, jsmvp 类型加固

# wirebrowserenv
在 browserenv 基础上, wirebrowserenv 功能更加强大, 支持拦截网络请求 的浏览器环境
作用:
    捕获的 HTTP 和 HTTPS 请求
    拦截请求和响应
    即时修改标题、参数、正文内容

轮子来源于: https://github.com/wkeeling/selenium-wire

# wirebrowserenv_uc
    对 undetected-chromedriver 的集成,
    优化的 Selenium Chromedriver 补丁,
    不会触发 Distill Network / Imperva / DataDome / Botprotect.io 等反僵尸服务,
    自动下载驱动程序二进制文件并对其进行修补。

# v8env
适用于 Python 的最小的现代嵌入式 V8 引擎
作用:
    执行js脚本

轮子来源于: https://github.com/sqreen/PyMiniRacer