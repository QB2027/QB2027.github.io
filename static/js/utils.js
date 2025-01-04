export async function loadHtml(containerSelector, htmlPath) {
    try {
      const response = await fetch(htmlPath);
      const html = await response.text();
      document.querySelector(containerSelector).innerHTML = html;
    } catch (error) {
      console.error(`加载 HTML 模块失败: ${htmlPath}`, error);
    }
  }
  