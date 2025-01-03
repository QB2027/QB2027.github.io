document.addEventListener('DOMContentLoaded', function () {
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
      data.announcements.forEach(announcement => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="${announcement.file}" target="_blank">${announcement.date} - ${announcement.title}</a>`;
        announcementList.appendChild(li);
      });
    })
    .catch(error => {
      console.error("加载公告列表时出错:", error);
    });
});