// app/static/js/post.js
document.addEventListener("DOMContentLoaded", () => {
  const editLink   = document.getElementById("editLink");
  const deleteLink = document.getElementById("deleteLink");
  const viewMode   = document.getElementById("viewMode");
  const editForm   = document.getElementById("editForm");

  const titleInput   = document.getElementById("editTitle");
  const categoryInput= document.getElementById("editCategory");
  const contentInput = document.getElementById("editContent");

  const saveBtn   = document.getElementById("saveBtn");
  const cancelBtn = document.getElementById("cancelBtn");

  if (editLink) {
    editLink.addEventListener("click", (e) => {
      e.preventDefault();
      viewMode.style.display = "none";
      editForm.style.display = "block";
    });
  }

  if (cancelBtn) {
    cancelBtn.addEventListener("click", () => {
      editForm.style.display = "none";
      viewMode.style.display = "block";
    });
  }

  if (saveBtn) {
    saveBtn.addEventListener("click", async () => {
      const payload = {
        title: titleInput.value.trim(),
        category: categoryInput.value.trim(),
        content: contentInput.value.trim()
      };

      const res = await fetch(`/post/${window.POST_ID}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        // 성공 시 페이지 새로고침(갱신)
        location.reload();
      } else {
        const data = await res.json().catch(() => ({}));
        alert(data.error || "수정 실패");
      }
    });
  }

  if (deleteLink) {
    deleteLink.addEventListener("click", async (e) => {
      e.preventDefault();
      if (!confirm("정말 이 글을 삭제하시겠어요?")) return;

      const res = await fetch(`/post/${window.POST_ID}`, {
        method: "DELETE"
      });

      if (res.ok) {
        // 삭제 후 블로그 메인으로 이동
        window.location.href = "/blog/";
      } else {
        const data = await res.json().catch(() => ({}));
        alert(data.error || "삭제 실패");
      }
    });
  }
});