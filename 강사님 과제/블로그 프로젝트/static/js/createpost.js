document.getElementById("createPostForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    category: document.getElementById("category").value,
    title: document.getElementById("title").value,
    content: document.getElementById("content").value
  };

  const response = await fetch("/cp/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  if (response.ok) {
    // 성공 시 → 블로그 메인으로 이동
    window.location.href = "/blog/";
  } else {
    const result = await response.json();
    document.getElementById("result").innerText = result.error || "작성 실패";
  }
});