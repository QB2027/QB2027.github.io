export function loadFiles(jsonPath) {
    fetch(jsonPath)
      .then(response => response.json())
      .then(data => {
        const fileList = document.getElementById('file-list');
        data.files.forEach(file => {
          const li = document.createElement('li');
          li.innerHTML = file.url
            ? `<a href="${file.url}" target="_blank">${file.name} (外部链接)</a>`
            : `<a href="data/${file.path}" target="_blank">${file.name}</a>`;
          fileList.appendChild(li);
        });
      })
      .catch(error => console.error('加载文件列表失败:', error));
  }
  