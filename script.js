// GitHub Study 仓库的基础 URL
const studyRepoBaseUrl = "https://raw.githubusercontent.com/Qianban2027/Study/main/";

// 加载文件下载列表
fetch('data/files.json')
  .then(response => response.json())
  .then(data => {
    const fileList = document.getElementById('file-list');
    data.files.forEach(file => {
      const li = document.createElement('li');
      // 检查是否有外部 URL，如果没有，则拼接 Study 仓库的基础路径
      const fileUrl = file.url ? file.url : studyRepoBaseUrl + file.path;
      li.innerHTML = `<a href="${fileUrl}" target="_blank" rel="noopener noreferrer">${file.name}</a>`;
      fileList.appendChild(li);
    });
  })
  .catch(error => {
    console.error("加载文件下载列表时出错:", error);
  });

// 加载公告列表
fetch('data/announcements.json')
  .then(response => response.json())
  .then(data => {
    const announcementList = document.getElementById('announcement-list');
    const contentDiv = document.getElementById('announcement-content');
    const markdownDiv = document.getElementById('markdown-content');
    const backButton = document.getElementById('back-button');

    data.announcements.forEach(announcement => {
      const li = document.createElement('li');
      li.textContent = `${announcement.date} - ${announcement.title}`;
      li.addEventListener('click', () => {
        fetch(`data/announcements/${announcement.file}`)
          .then(response => response.text())
          .then(markdown => {
            markdownDiv.innerHTML = marked(markdown); // 使用 marked.js 解析 Markdown
            announcementList.style.display = 'none';
            contentDiv.classList.remove('hidden');
          })
          .catch(error => {
            console.error("加载公告内容时出错:", error);
          });
      });
      announcementList.appendChild(li);
    });

    backButton.addEventListener('click', () => {
      contentDiv.classList.add('hidden');
      announcementList.style.display = 'block';
    });
  })
  .catch(error => {
    console.error("加载公告列表时出错:", error);
  });