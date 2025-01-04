export function loadFiles(jsonPath) {
    fetch(jsonPath)
        .then(response => response.json())
        .then(data => {
            const fileList = document.getElementById('file-list');
            renderFileTree(data.files, fileList);
        })
        .catch(error => console.error('加载文件列表失败:', error));
}

function renderFileTree(files, parentElement, parentRepo = "", parentBranch = "main") {
    files.forEach(file => {
        if (file.children && file.children.length > 0) {
            // 递归处理非空的子文件夹
            renderFileTree(file.children, parentElement, file.repo || parentRepo, file.branch || parentBranch);
        } else if (file.path || file.url) {
            const li = document.createElement('li');
            if (file.path) {
                // 仓库文件：生成原始下载和镜像下载链接
                const repo = parentRepo;
                const branch = file.branch || parentBranch;
                const rawLink = `https://raw.githubusercontent.com/${repo}/${branch}/${file.path}`;
                const mirrorLink = `https://ghproxy.com/https://raw.githubusercontent.com/${repo}/${branch}/${file.path}`;
                li.innerHTML = `
                    <span>${file.name}</span>
                    <a href="${rawLink}" target="_blank" style="margin-left: 10px;">原始下载</a>
                    <a href="${mirrorLink}" target="_blank" style="margin-left: 10px; color: green;">镜像下载</a>
                `;
            } else if (file.url) {
                // 外部链接文件
                li.innerHTML = `<a href="${file.url}" target="_blank">${file.name} (外部链接)</a>`;
            }
            parentElement.appendChild(li);
        }
    });
}