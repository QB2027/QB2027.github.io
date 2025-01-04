export function loadFiles(jsonPath) {
    fetch(jsonPath)
      .then(response => response.json())
      .then(data => {
        const fileList = document.getElementById('file-list');
        data.files.forEach(file => {
          const li = document.createElement('li');

          // 如果是外部链接
          if (file.url) {
            li.innerHTML = `<a href="${file.url}" target="_blank">${file.name} (外部链接)</a>`;
          } else {
            // 内部路径处理，生成 GitHub Raw 下载链接
            const githubRawBase = "https://raw.githubusercontent.com/Qianban2027/Study/main/";
            const rawLink = `${githubRawBase}${file.path}`;
            li.innerHTML = `<a href="${rawLink}" target="_blank">${file.name}</a>`;
          }

          fileList.appendChild(li);
        });
      })
      .catch(error => console.error('加载文件列表失败:', error));
  }
