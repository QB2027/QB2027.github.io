// 加载文件下载列表
fetch('data/files.json')
  .then(response => response.json())
  .then(data => {
    const fileList = document.getElementById('file-list');
    data.files.forEach(file => {
      const li = document.createElement('li');
      const fileUrl = file.url ? file.url : `https://raw.githubusercontent.com/Qianban2027/Study/main/${file.path}`;
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

    // 遍历 JSON 数据，生成公告列表
    data.announcements.forEach(announcement => {
      const li = document.createElement('li');
      li.textContent = `${announcement.date} - ${announcement.title}`;
      li.style.cursor = "pointer";
      li.addEventListener('click', () => {
        markdownDiv.innerHTML = "加载中...";
        fetch(`data/${announcement.file}`)
          .then(response => {
            if (!response.ok) {
              throw new Error(`无法加载公告文件：${announcement.file}`);
            }
            return response.text();
          })
          .then(markdown => {
            markdownDiv.innerHTML = marked(markdown); // 使用 marked.js 渲染 Markdown
            MathJax.typeset(); // 渲染 LaTeX 公式
            announcementList.style.display = 'none';
            contentDiv.classList.remove('hidden');
          })
          .catch(error => {
            console.error(`加载公告内容失败：${error.message}`);
            markdownDiv.innerHTML = `<p style="color: red;">加载失败：${error.message}</p>`;
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