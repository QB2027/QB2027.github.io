import { loadHtml } from './utils.js';
import { loadFiles } from './fileManager.js';
import { loadNotices } from './noticeManager.js';

document.addEventListener('DOMContentLoaded', async () => {
  // 加载 Header 和 Footer
  await loadHtml('#header', 'static/html/header.html');
  await loadHtml('#footer', 'static/html/footer.html');

  // 加载文件下载区域
  await loadHtml('#downloads', 'static/html/fileList.html');
  loadFiles('data/files.json');

  // 加载公告区域
  await loadHtml('#announcements', 'static/html/noticeList.html');
  loadNotices('data/notices.json');
});
