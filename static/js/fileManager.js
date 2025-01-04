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
        const li = document.createElement('li');

        if (file.children) {
            // 文件夹逻辑：显示仓库名称而不是分支
            li.textContent = file.repo ? `${file.repo}` : parentRepo;
            const ul = document.createElement('ul');
            renderFileTree(file.children, ul, file.repo || parentRepo, file.branch || parentBranch);
            li.appendChild(ul);
        } else if (file.path) {
            // 仓库文件：生成原始下载和镜像下载链接
            const repo = file.repo || parentRepo;
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
    });
}
