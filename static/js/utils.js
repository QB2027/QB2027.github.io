/**
 * 动态加载 HTML 模块到指定容器
 * @param {string} containerSelector - 容器的 CSS 选择器
 * @param {string} htmlPath - HTML 文件的路径
 */
export async function loadHtml(containerSelector, htmlPath) {
  try {
      const response = await fetch(htmlPath);
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }
      const html = await response.text();
      document.querySelector(containerSelector).innerHTML = html;
  } catch (error) {
      console.error(`加载 HTML 模块失败: ${htmlPath}`, error);
  }
}

/**
* 格式化日期为指定格式
* @param {Date} date - 日期对象
* @param {string} format - 日期格式，例如 'YYYY-MM-DD'
* @returns {string} 格式化后的日期字符串
*/
export function formatDate(date, format = 'YYYY-MM-DD') {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');

  return format
      .replace('YYYY', year)
      .replace('MM', month)
      .replace('DD', day);
}

/**
* 获取 URL 查询参数
* @param {string} param - 查询参数的名称
* @returns {string|null} 查询参数的值
*/
export function getQueryParam(param) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
}

/**
* 创建一个 DOM 元素并设置属性
* @param {string} tagName - 元素标签名
* @param {Object} attributes - 属性对象，例如 { id: "myId", class: "myClass" }
* @returns {HTMLElement} 创建的 DOM 元素
*/
export function createElement(tagName, attributes = {}) {
  const element = document.createElement(tagName);
  for (const [key, value] of Object.entries(attributes)) {
      element.setAttribute(key, value);
  }
  return element;
}
