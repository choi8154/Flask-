document.getElementById("signinForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
        login_id: document.getElementById("login_id").value,
        password: document.getElementById("password").value
    };

    const response = await fetch("/signin/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

if (response.ok) {
    // 로그인 성공 시 → /blog/ 로 이동
    window.location.href = "/blog/";
} else {
    const result = await response.json();
    document.getElementById("result").innerText = result.error;
}});