$(document).ready(function () {
  // 公告点击事件
  $('#announcement-list').on('click', 'a', function () {
    const filePath = $(this).data('file'); // 获取 data-file 中的文件路径
    const markdownDiv = $('#markdown-content');
    const announcementList = $('#announcement-list');
    const contentDiv = $('#announcement-content');

    console.log(`正在加载公告文件：${filePath}`);
    markdownDiv.html("加载中...");

    // 动态加载 Markdown 文件
    $.ajax({
      type: "get",
      url: filePath,
      dataType: "html",
      success: function (res) {
        markdownDiv.html(marked.parse(res)); // 渲染 Markdown
        MathJax.typeset(); // 渲染公式
        announcementList.hide();
        contentDiv.removeClass('hidden');
      },
      error: function (err) {
        console.error(`加载公告内容失败：${err.statusText}`);
        markdownDiv.html(`<p style="color: red;">加载失败：${err.statusText}</p>`);
      }
    });
  });

  // 返回按钮点击事件
  $('#back-button').on('click', function () {
    $('#announcement-content').addClass('hidden');
    $('#announcement-list').show();
  });
});