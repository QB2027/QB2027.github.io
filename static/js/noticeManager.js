export function loadNotices(jsonPath) {
  fetch(jsonPath)
      .then(response => response.json())
      .then(data => {
          const noticeList = document.getElementById('notice-list'); // 确保 ID 正确
          data.notices.forEach(notice => {
              const li = document.createElement('li');
              li.innerHTML = `<a href="${notice.file}" target="_blank">${notice.date} - ${notice.title}</a>`;
              noticeList.appendChild(li);
          });
      })
      .catch(error => console.error('加载公告列表失败:', error));
}
