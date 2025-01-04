export function loadFiles(jsonPath) {
  fetch(jsonPath)
      .then(response => response.json())
      .then(data => {
          const fileList = document.getElementById('file-list');
          renderFileTree(data.files, fileList);
      })
      .catch(error => console.error('加载文件列表失败:', error));
}

function renderFileTree(files, parentElement, repo = '', branch = '') {
  files.forEach(file => {
      const li = document.createElement('li');

      if (file.children) {
          // 仓库节点
          li.textContent = `${file.repo} (分支: ${file.branch})`;
          const ul = document.createElement('ul');
          renderFileTree(file.children, ul, file.repo || repo, file.branch || branch);
          li.appendChild(ul);
      } else if (file.path && repo && branch) {
          // 仓库内文件
          const rawLink = `https://raw.githubusercontent.com/${repo}/${branch}/${file.path}`;
          const mirrorLink = `https://ghproxy.com/https://raw.githubusercontent.com/${repo}/${branch}/${file.path}`;
          li.innerHTML = `
              <span>${file.name}</span>
              <a href="${rawLink}" target="_blank" style="margin-left: 10px;">下载</a>
              <a href="${mirrorLink}" target="_blank" style="margin-left: 10px; color: green;">镜像下载</a>
          `;
      } else if (file.url) {
          // 直接链接文件
          li.innerHTML = `<a href="${file.url}" target="_blank">${file.name} (外部链接)</a>`;
      }

      parentElement.appendChild(li);
  });
}
